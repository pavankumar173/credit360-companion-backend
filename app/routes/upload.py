
import io
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(io.BytesIO(contents))
        elif file.filename.endswith(".json"):
            df = pd.read_json(io.BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Parsing failed: {str(e)}")

    return {
        "filename": file.filename,
        "preview": df.head().to_dict(orient="records")
    }
