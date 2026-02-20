from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import pandas as pd
import io
import tempfile
import os

from .pdf_generate import build_pdf_from_df
from .csv_validate import validate_topics_df

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    # Basic file check
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a .csv file")

    # 1) Read uploaded file bytes (in memory)
    raw_bytes: bytes = await file.read()

    # 2) Convert bytes -> file-like object for pandas
    try:
        df = pd.read_csv(io.BytesIO(raw_bytes))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not read CSV: {e}")

    # 3) Validate + clean
    try:
        df = validate_topics_df(df)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 4) Build PDF into a temp file
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    tmp_path = tmp.name
    tmp.close()

    build_pdf_from_df(df, output_path=tmp_path)

    # 5) Return as a download
    return FileResponse(
        path=tmp_path,
        media_type="application/pdf",
        filename="lesson-notes.pdf",
    )