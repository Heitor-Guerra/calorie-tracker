import type { DailyLog } from "../types/daily-log"

import { getCsrfToken, getCookie } from "./csrf-service"

const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8080/logs";

export async function csrf(): Promise<string> {
  await getCsrfToken();

  const csrfToken = getCookie("csrftoken");

  if (!csrfToken) {
    throw new Error("CSRF token was not found");
  }
  return csrfToken;
}


export async function getUsersLogs(): Promise<DailyLog[]> {
  const csrfT = await csrf();

  const response = await fetch(`${API_URL}`,  {
    credentials: "include",
    method: "GET",
    headers: {
      "X-CSRFToken": csrfT,
    }
  });

  if (!response.ok) {
    throw new Error("The user is not logged.");
  }

  return response.json() as Promise<DailyLog[]>;
}


export async function uploadImageToLog(file: File): Promise<DailyLog> {
  const csrfT = await csrf();

  const formData: FormData = new FormData();
  formData.append("image", file);

  const response = await fetch(`${API_URL}/upload`,  {
    credentials: "include",
    method: "POST",
    headers: {
      "X-CSRFToken": csrfT,
    },
    body: formData,
  });


  if (!response.ok) {
    throw new Error("The user is not logged.");
  }

  return response.json() as Promise<DailyLog>;
}
