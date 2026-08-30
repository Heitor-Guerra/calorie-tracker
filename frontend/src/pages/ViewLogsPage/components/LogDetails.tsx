import {
  Box,
  Typography,
  List,
  ListItem,
  Button,
  Stack,
  Alert,
  Divider
} from "@mui/material";
import type { DailyLog } from "../../../types/daily-log";
import EntryDetails from "./EntryDetails";
import { formatDate } from "../../../utils/formatDate";


interface LogDetailsProps {
  log: DailyLog,
  onClose: () => void,
}


function LogDetails({
  log,
  onClose,
}: LogDetailsProps) {
  const entryCount = log.entries.length;
  const date:string = formatDate(log.date);

  return (
    <Box
      component="section"
      className="mx-auto max-w-3xl p-6"
    >
      <Stack spacing={3}>
        <Stack component="section">
          <Box>
            <Typography
              component="h1"
              variant="h4"
              className="font-bold tracking-tight text-slate-900"
            >
              {date}
            </Typography>

            <Typography className="text-sm text-slate-500">
              {entryCount} {entryCount === 1 ? "entry" : "entries"}
            </Typography>
          </Box>

          <Button
            variant="outlined"
            onClick={onClose}
            className="rounded-lg normal-case"
          >
            Back
          </Button>
        </Stack>

        {!entryCount ? (
          <Alert severity="info">
            This log has no entries.
          </Alert>
        ) : (
          <List
            disablePadding
            className="rounded-xl border border-slate-200 bg-white px-5"
          >
            {log.entries.map((entry, index) => (
              <Box key={`${entry.food.name}-${index}`}>
                <ListItem disableGutters className="py-4 p-3">
                  <EntryDetails entry={entry} />
                </ListItem>

                {index < log.entries.length - 1 && <Divider />}
              </Box>
            ))}
          </List>
        )}
      </Stack>
    </Box>
  );

}

export default LogDetails;
