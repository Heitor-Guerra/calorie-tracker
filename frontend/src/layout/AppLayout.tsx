import Header from "./Header"

import { Box } from '@mui/material';
import { Navigate, Outlet, useLocation } from "react-router-dom";
import { useLoggedUser } from "../hooks/useLoggedUser";



function AppLayout() {
  const { loading, error } = useLoggedUser()

  const location = useLocation()
  if (loading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <Navigate to="/login" replace state={{ from: location }} />;
  }

  return (
    <>
      <Box component="header" className="fixed left-0 right-0 top-0 z-40 h-16">
        <Header />
      </Box>


      <Box component="main" className="min-h-screen p-4 pt-20">
        <Outlet />
      </Box>
    </>
  )

}

export default AppLayout
