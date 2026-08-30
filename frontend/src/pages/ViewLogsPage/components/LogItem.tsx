import type { DailyLog } from "../../../types/daily-log";
import {
  Box,
  Typography,
  Button,
  Card,
  CardContent,
  Stack,
} from "@mui/material";
import { formatDate } from "../../../utils/formatDate";

interface LogItemProps {
  log: DailyLog,
  onOpenLog: (log: DailyLog) => void;
}


function LogItem({
  log,
  onOpenLog,
}: LogItemProps) {
  const count:number = log.entries.length;
  const date: string = formatDate(log.date);

  const sumCalories = (log: DailyLog) => {
    let total: number = 0;
    for (const entry of log.entries) {
      total += entry.quantity_g * entry.food.calories_per_100g / 100;
    }
    return total;
  }

  const totalCalories: number = sumCalories(log);

  return (
    <Card
      variant="outlined"
      className="w-full rounded-xl border-slate-200 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
    >
      <CardContent className="p-5 last:pb-5">
        <Stack
          component="div"
          direction="row"
          className="flex justify-between"
          spacing={2}
        >
          <Box>
            <Typography
              component="h2"
              variant="h6"
              className="font-semibold text-slate-900"
            >
              {date}
            </Typography>

            <Typography className="text-sm text-slate-500">
              {count} {count === 1 ? "item" : "items"} consumed
            </Typography>
            <Typography className="text-sm text-slate-500">
              {totalCalories} calories consumed
            </Typography>
          </Box>

          <Button
            variant="contained"
            onClick={() => onOpenLog(log)}
            className="rounded-lg normal-case shadow-none hover:shadow-none">
            View log
          </Button>
        </Stack>
      </CardContent>
    </Card>
  );
}

export default LogItem;
