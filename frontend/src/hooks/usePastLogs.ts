import { useState, useEffect } from "react"
import {getUsersLogs} from "../services/logs-service"
import type { DailyLog } from "../types/daily-log";

export function usePastLogs() {
  const [logs, setLogs] = useState<DailyLog[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false

    async function getData() {
      try {
        setLoading(true);
        setError(null);

        const data = await getUsersLogs();

        if (!cancelled) {
          setLogs(data);
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

    getData();
    return () => {
      cancelled = true;
    };
  }, []);


  return {
    logs,
    loading,
    error,
  };
}
