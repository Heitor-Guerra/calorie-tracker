import type { FoodEntry } from "../../../types/food";
import {
  Box,
  Stack,
  Typography,
} from "@mui/material";

interface EntryDetailsProps {
  entry: FoodEntry,
}


function EntryDetails({
  entry,
}: EntryDetailsProps) {

  return (
    <Box component="article" className="w-full">
      <Typography
        component="h2"
        variant="h6"
        className="font-semibold text-slate-900"
      >
        {entry.food.name}
      </Typography>

      <Stack spacing={0.25} className="mt-1">
        <Typography className="text-sm text-slate-500">
          {entry.quantity_g.toLocaleString()} g consumed
        </Typography>

        <Typography className="text-sm text-slate-500">
          {entry.food.calories_per_100g.toLocaleString()} calories per 100 g
        </Typography>
      </Stack>
    </Box>
  );

}

export default EntryDetails;
