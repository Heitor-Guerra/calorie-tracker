import type { UserRegister, User, UserLogin } from "../types/user"

import { getCsrfToken, getCookie } from "./csrf-service"

const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000/user";

export async function csrf(): Promise<string> {
  await getCsrfToken();

  const csrfToken = getCookie("csrftoken");

  if (!csrfToken) {
    throw new Error("CSRF token was not found");
  }
  return csrfToken;
}


export async function getLoggedUser(): Promise<User> {
  const csrfT = await csrf();

  const response = await fetch(`${API_URL}/logged-user`,  {
    credentials: "include",
    method: "GET",
    headers: {
      "X-CSRFToken": csrfT,
    }
  });

  if (!response.ok) {
    throw new Error("The user is not logged.");
  }

  return response.json() as Promise<User>;
}

export async function login(user: UserLogin): Promise<object> {
  const csrfT = await csrf();

  const response = await fetch(`${API_URL}/login`,  {
    credentials: "include",
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfT,
    },
    body: JSON.stringify(user)
  });

  if (!response.ok) {
    throw new Error("Failed to login. The user might not be registered");
  }

  return response.json() as Promise<object>;
}

export async function register(user: UserRegister): Promise<object> {
  const csrfT = await csrf()

  const response = await fetch(`${API_URL}/create`,  {
    credentials: "include",
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfT,
    },
    body: JSON.stringify(user)
  });

  if (!response.ok) {
    throw new Error("Failed to register.");
  }

  return response.json() as Promise<object>;
}

export async function logout(): Promise<object> {
  const csrfT = await csrf();

  const response = await fetch(`${API_URL}/login`,  {
    credentials: "include",
    method: "GET",
    headers: {
      "X-CSRFToken": csrfT,
    },
  });

  if (!response.ok) {
    throw new Error("The user is not logged.");
  }

  return response.json() as Promise<object>;
}
