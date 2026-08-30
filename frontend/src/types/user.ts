export interface User{
  email: string;
  username: string;
  full_name: string;
  is_staff: string;
}

export interface UserLogin{
  email: string;
  password: string;
}

export interface UserRegister{
  email: string;
  password: string;
  username: string;
  full_name: string;
}
