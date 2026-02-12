import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api";

export const axios_instance = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
});

let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
  failedQueue.forEach((prom) => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });
  failedQueue = [];
};

axios_instance.interceptors.request.use((config) => {
  const accessToken = localStorage.getItem("accessToken");
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
});

axios_instance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const original_request = error.config;
    
    // Skip retry for refresh endpoint to prevent infinite loop
    if (original_request.url && original_request.url.includes("/auth/refresh")) {
      isRefreshing = false;
      processQueue(error, null);
      localStorage.clear();
      window.location.href = "/login";
      return Promise.reject(error);
    }
    
    if (error?.response?.status === 401 && !original_request._retry) {
      if (isRefreshing) {
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject });
        })
          .then((token) => {
            original_request.headers.Authorization = `Bearer ${token}`;
            return axios_instance(original_request);
          })
          .catch((err) => {
            return Promise.reject(err);
          });
      }

      original_request._retry = true;
      isRefreshing = true;

      try {
        const res = await axios_instance.post("/auth/refresh", {
          refresh_token: localStorage.getItem("refreshToken"),
        });
        const new_access_token = res.data.access_token;
        const new_refresh_token = res.data.refresh_token;
        
        localStorage.setItem("accessToken", new_access_token);
        localStorage.setItem("refreshToken", new_refresh_token);

        original_request.headers.Authorization = `Bearer ${new_access_token}`;
        
        processQueue(null, new_access_token);
        isRefreshing = false;
        
        return axios_instance(original_request);
      } catch (refreshError) {
        processQueue(refreshError, null);
        isRefreshing = false;
        localStorage.clear();
        window.location.href = "/login";
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  },
);
