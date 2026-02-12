import { Outlet, Navigate } from "react-router-dom";

export const IfNotLogin = ({ authUser }) => {
  if (authUser === null) return <Outlet />;
  return <Navigate to="/dashboard" replace />;
};
