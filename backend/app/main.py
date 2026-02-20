from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
import pandas as pd
import io
import tempfile
import os
from fastapi.middleware.cors import CORSMiddleware
from .pdf_generate import build_pdf_from_df
from .csv_validate import validate_topics_df

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:5173",
        "https://pdf-template-black.vercel.app", # Vercel deployment
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate",
    response_class=FileResponse,
    responses={200: {"content": {"application/pdf": {}}}},
          )
async def generate(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
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

    background_tasks.add_task(os.remove, tmp_path)

    return FileResponse(
        path=tmp_path,
        media_type="application/pdf",
        filename="lesson-notes.pdf",
        background=background_tasks,
    )