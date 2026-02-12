import React from "react";
import { Outlet, Navigate, Link, useNavigate } from "react-router-dom";

export const Protected = ({ authUser, setAuthuser }) => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.clear();
    setAuthuser(null);
    navigate("/login");
  };

  if (authUser) {
    return (
      <div>
        <h2>JWT Refresh Token Demo</h2>
        <Link to="/dashboard/home"> Home </Link>
        <Link to="/dashboard/about"> About </Link>
        <Link to="/dashboard/contact"> Contact </Link>
        <button onClick={handleLogout}>Logout</button>
        <Outlet />
      </div>
    );
  }
  
  return <Navigate to="/login" replace />;
};
