import { Outlet } from "react-router-dom";
export const IfNotLogin = ({ authUser }) => {
  if (authUser === null) return <Outlet />;
  return ;
};
