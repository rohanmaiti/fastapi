import React, { useRef } from "react";
import { axios_instance } from "../src/utils/axios";

export const Login = () => {
  const emailRef = useRef();
  const passwordRef = useRef();
  const handle_login = async ({get_auth_user}) => {
    const email = emailRef.current.value;
    const password = passwordRef.current.value;
    // make api call get the token and store it
    const res = await axios_instance.post("/auth/login",{
      email,
      password,
    });
    localStorage.setItem("accessToken", res.data.access_token);
    localStorage.setItem("refreshToken", res.data.refresh_token);
    get_auth_user();
  };
  return (
    <div>
      <input type="email" ref={emailRef} placeholder="enter email" />
      <input type="password" ref={passwordRef} placeholder="enter password" />
      <button onClick={handle_login}> Login </button>
    </div>
  );
};
