import React from "react";
import { Outlet, Navigate, Link } from "react-router-dom";

export const Protected = ({authUser}) => {
  if (authUser) {
    return <div>
     <h2>JWT Refresh Token Demo</h2>
    <Link to="/home" > Home </Link>
    <Link to="/about" > About </Link>
    <Link to="/contact" > Contact </Link>
    <Link>Logout</Link>
    <Outlet/>
    </div>
  }
  else 
  return ;
  
};
