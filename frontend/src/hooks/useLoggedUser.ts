import { useState, useEffect } from "react";
import { getLoggedUser } from "../services/auth-service";
import type { User } from "../types/user";

export function useLoggedUser() {
  const [user, setUser] = useState<User>();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    async function loadItems() {
      try {
        setLoading(true);
        setError(null);

        const data = await getLoggedUser();

        if (!cancelled) {
          setUser(data);
        }


      } catch (error) {
        if (!cancelled) {
          setError(
            error instanceof Error
              ? error.message : "",
          );
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }
    loadItems();

    return () => {
      cancelled = true;
    };
  }, [])

  return {
    user,
    loading,
    error,
  };
}
