import {
  AppBar,
  Box,
  Button,
  Toolbar,
  Typography,
} from "@mui/material";
import { Link as RouterLink } from "react-router-dom";
import { logout } from "../services/auth-service"



function Header() {

  return (
    <AppBar
      position="static"
      className="shadow-md"
    >
      <Toolbar className="mx-auto flex w-full justify-between gap-4 px-4 sm:px-6">
        {/* Logo */}
        <Typography
          component={RouterLink}
          to="/"
          className="whitespace-nowrap font-bold text-white no-underline"
          variant="h6"
        >
          Calorie Tracker
        </Typography>

        <Box className="hidden items-center gap-1 sm:flex">
          <Button
            component={RouterLink}
            variant="outlined"
            to="/logs"
            color="inherit"
            className="text-white"
          >
            Logs
          </Button>

          <Button
            component={RouterLink}
            variant="outlined"
            onClick={logout}
            to="/login"
            color="inherit"
            className="text-white"
          >
            Logout
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );

}


export default Header;
