import React, { useRef, useState } from "react";
import { axios_instance } from "../src/utils/axios";
import { useNavigate } from "react-router-dom";

export const Signup = ({ get_auth_user }) => {
  const emailRef = useRef();
  const passwordRef = useRef();
  const nameRef = useRef();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const navigate = useNavigate();

  const handle_signup = async () => {
    const email = emailRef.current.value;
    const password = passwordRef.current.value;
    const name = nameRef.current.value;

    if (!email || !password) {
      setError("Email and password are required");
      return;
    }

    setLoading(true);
    setError("");
    setSuccess("");

    try {
      await axios_instance.post("/auth/signup", {
        email,
        password,
        name,
      });
      setSuccess("Account created successfully! Redirecting to login...");
      setTimeout(() => navigate("/login"), 2000);
    } catch (err) {
      setError(
        err?.response?.data?.detail || "Signup failed. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Signup</h2>
      {error && <div style={{ color: "red" }}>{error}</div>}
      {success && <div style={{ color: "green" }}>{success}</div>}
      <input type="text" ref={nameRef} placeholder="enter name (optional)" />
      <input type="email" ref={emailRef} placeholder="enter email" />
      <input type="password" ref={passwordRef} placeholder="enter password" />
      <button onClick={handle_signup} disabled={loading}>
        {loading ? "Creating account..." : "Signup"}
      </button>
    </div>
  );
};
