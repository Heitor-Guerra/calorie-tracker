import {
  Box,
  Typography,
  List,
  ListItem,
  Alert,
} from "@mui/material";
import { usePastLogs } from "../../../hooks/usePastLogs";
import LogItem from "./LogItem";
import type { DailyLog } from "../../../types/daily-log";
import { useState } from "react";
import LogDetails from "./LogDetails";
import { Navigate, useLocation } from "react-router-dom";


function LogList() {
  const { logs, loading, error } = usePastLogs()

  const [openedLog, setOpenedLog] = useState<DailyLog | null>(null)

  const location = useLocation()

  if (loading) {
    return (
      <Box
        component="section"
        className="mx-auto max-w-3xl p-6"
        aria-live="polite"
      >
        <Typography className="text-sm text-slate-500">
          Loading logs…
        </Typography>
      </Box>
    );
  }

  if (error) {
    return <Navigate to="/" replace state={{ from: location }} />;
  }

  if (openedLog) {
    return (
      <LogDetails
        log={openedLog}
        onClose={() => setOpenedLog(null)}
      />
    );
  }

  return (
    <Box component="section" className="mx-auto max-w-3xl p-6">
      <Typography variant="h4" component="h1" className="font-bold tracking-tight text-slate-900" gutterBottom>
        Past logs
      </Typography>
      {!logs?.length ? (
        <Alert severity="info">You do not have any past logs yet.</Alert>
      ) : (
        <List disablePadding>
          {logs.map((log) => (
            <ListItem key={log.id ?? log.date.toString()} disableGutters>
              <LogItem
                log={log}
                onOpenLog={(logO) => setOpenedLog(logO)}
              />
            </ListItem>
          ))}
        </List>
      )}

    </Box>
  );

}

export default LogList;
