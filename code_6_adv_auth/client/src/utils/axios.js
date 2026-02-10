import axios from "axios";

export const axios_instance = axios.create({
  baseURL: "http://localhost:8000/api",
  withCredentials: true,
});

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
    if (error?.response.status === 401 && !original_request._retry) {
      original_request._retry = true;
      try {
        const res = await axios_instance.post("/refresh", {
          refresh_token: localStorage.getItem("refreshToken"),
        });
        const new_access_token = res.data.access_token;
        localStorage.setItem("accessToken", new_access_token);

         original_request.headers.Authorization =
          `Bearer ${new_access_token}`;

          return axios_instance(original_request);
      } catch (error) {
        localStorage.clear();
        window.location.href = "/login";
      }
    }
    return Promise.reject(error);
  },
);
