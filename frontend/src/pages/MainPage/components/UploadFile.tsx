import type { ChangeEvent } from "react";
import { useState } from "react";
import {
  Box,
  Button,
  Typography,
} from "@mui/material";
import { uploadImageToLog } from "../../../services/logs-service";
import type { DailyLog } from "../../../types/daily-log";
import LogDetails from "../../ViewLogsPage/components/LogDetails";


function UploadFile() {
  const [log, setLog] = useState<DailyLog | null>(null);
  const [file, setFile] = useState<File | null>(null);

  const selectFile = (selectedFile?: File) => {
    if (!selectedFile) return;

    setFile(selectedFile);
  };

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    selectFile(event.target.files?.[0]);
  };


  const uploadImage = async () => {
    if (!file) return;

    const log = await uploadImageToLog(file);
    setLog(log);
  };

  return (
      <Box component="section" className="border border-stone-400 w-fit">
        <Box className="px-6 py-7">
          <Typography variant="h5">
            Upload an image
          </Typography>
        </Box>

        <Box className="p-6">
          {!log ? (
            <Box className=" rounded-2xl">
              <Typography className="my-2 text-sm text-slate-500">
                Click to browse files
              </Typography>

              <input type="file" className="border border-stone-400 mt-3 mb-3 p-3 flex w-fit cursor-pointer" onChange={handleFileChange} />
              <Button
                variant="contained"
                className=""
                onClick={uploadImage}>
                Choose image
              </Button>
            </Box>
          ) : (
            <LogDetails log={log} onClose={() => setLog(null)} />
          )}
        </Box>
      </Box>
  );
}


export default UploadFile;
