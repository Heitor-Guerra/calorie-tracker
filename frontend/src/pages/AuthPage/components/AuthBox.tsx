import { useState } from "react";
import {
  Box,
  Typography,
  Paper,
  Tab,
  Tabs,
  Alert
} from "@mui/material";
import LoginForm from "./LoginForm";

function AuthBox() {
  const [isLogin, setIsLogin] = useState(true);
  const [error, setError] = useState<string | null>(null);

  return (
    <Box
      className="min-h-screen flex items-center justify-center bg-gray-100 p-4"
    >
      <Paper elevation={3} className="w-full max-w-md p-4 rounded-xl">
        <Box className="text-center mb-6">
          <Typography variant="h4" className="font-bold">
            {isLogin ? "Welcome Back" : "Create Account"}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {isLogin ? "Please enter your details to sign in" : "Join our community today"}
          </Typography>
        </Box>

        <Tabs
          value={isLogin ? 0 : 1}
          onChange={(_, newValue) => setIsLogin(newValue === 0)}
          centered
          className="mb-6"
        >
          <Tab label="Login" />
          <Tab label="Register" />
        </Tabs>

        {error && (
          <Alert severity="error" className="mb-4">
            {error}
          </Alert>
        )}

        <LoginForm isLogin={isLogin} onError={(err) => setError(err)}/>
      </Paper>
    </Box>
  );
}

export default AuthBox;
