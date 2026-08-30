import { Button, CircularProgress, TextField } from "@mui/material";
import { useState } from "react";
import { login, register } from "../../../services/auth-service"
import { useNavigate } from "react-router-dom";



type LoginFormProps = {
  isLogin: boolean;
  onError: (err: string | null) => void;
}

function LoginForm({ isLogin, onError }: LoginFormProps) {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const [formData, setFormData] = useState({
    email: "",
    password: "",
    username: "",
    full_name: "",
  });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    onError(null);

    try {
      if (isLogin) {
        await login(formData)
      } else {
        await register(formData)
        await login(formData)
      }
      navigate("/");
    } catch (err: any) {
      onError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4">
      {!isLogin && (
        <>
          <TextField
            label="Full Name"
            name="full_name"
            value={formData.full_name}
            onChange={handleChange}
            required
            fullWidth
          />
          <TextField
            label="Username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            fullWidth
          />
        </>
      )}

      <TextField
        label="Email Address"
        name="email"
        type="email"
        value={formData.email}
        onChange={handleChange}
        required
        fullWidth
      />

      <TextField
        label="Password"
        name="password"
        type="password"
        value={formData.password}
        onChange={handleChange}
        required
        fullWidth
      />

      <Button
        type="submit"
        variant="contained"
        fullWidth
        disabled={loading}
        className="py-3 mt-2"
        endIcon={loading && <CircularProgress size={20} color="inherit" />}
      >
        {loading ? "Processing..." : isLogin ? "Log In" : "Sign Up"}
      </Button>
    </form>
  );

}

export default LoginForm;
