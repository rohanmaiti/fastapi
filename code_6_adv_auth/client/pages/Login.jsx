import React, { useRef, useState } from "react";
import { axios_instance } from "../src/utils/axios";
import { useNavigate } from "react-router-dom";

export const Login = ({ get_auth_user }) => {
  const emailRef = useRef();
  const passwordRef = useRef();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handle_login = async () => {
    const email = emailRef.current.value;
    const password = passwordRef.current.value;
    
    if (!email || !password) {
      setError("Please enter both email and password");
      return;
    }
    
    setLoading(true);
    setError("");
    
    try {
      const res = await axios_instance.post("/auth/login", {
        email,
        password,
      });
      localStorage.setItem("accessToken", res.data.access_token);
      localStorage.setItem("refreshToken", res.data.refresh_token);
      await get_auth_user();
      navigate("/dashboard");
    } catch (err) {
      setError(err?.response?.data?.detail || "Login failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      {error && <div style={{ color: "red" }}>{error}</div>}
      <input type="email" ref={emailRef} placeholder="enter email" />
      <input type="password" ref={passwordRef} placeholder="enter password" />
      <button onClick={handle_login} disabled={loading}>
        {loading ? "Logging in..." : "Login"}
      </button>
    </div>
  );
};
