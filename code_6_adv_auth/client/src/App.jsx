import { useEffect, useState } from "react";
import { IfNotLogin } from "../layouts/IfNotLogin";
import { Protected } from "../layouts/Protected";
import { Dashboard } from "../pages/Dashboard";
import { Login } from "../pages/Login";
import { ProtectedDashboard } from "../pages/ProtectedDashboard";
import { Signup } from "../pages/Signup";
import "./App.css";
import { Navigate, Route, Routes } from "react-router-dom";
import { axios_instance } from "./utils/axios";

function App() {
  const [loading, setLoading] = useState(false);
  const [authUser, setAuthuser] = useState(null);


  const get_auth_user = async () => {
    try {
      const res = await axios_instance.post("/auth/me");
      setAuthuser(res.data);
    } catch (error) {
      console.log("error occured", error?.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    (() => get_auth_user())();
  }, []);

  if (loading) return <h1>Loading ...</h1>;
  return (
    <>
      <Routes>
        <Route element={<IfNotLogin authUser={authUser} />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/login" element={<Login get_auth_user={get_auth_user} />} />
          <Route path="/signup" element={<Signup />} />
        </Route>

        <Route path="/dashbaord" element={<Protected authUser={authUser} />}>
          <Route index element={<ProtectedDashboard />} />
          <Route path="home" element={<h1>Home</h1>} />
          <Route path="about" element={<h1> About </h1>} />
          <Route path="contact" element={<h1> Contact </h1>} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
