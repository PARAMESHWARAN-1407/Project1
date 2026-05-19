from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from api.core.parse import parse_document
from api.core.state import init_db, create_run, get_run
from api.core.pulse import PULSE
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="PRISM AI",
    description="AI Powered Document Reader",
    version="1.0"
)

# templates folder inside api
templates = Jinja2Templates(directory="api/templates")

@app.on_event("startup")
async def startup():
    await init_db()
@app.get("/config")
def config():
    return {
        "environment": os.getenv("ENVIRONMENT")
    }

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    run_id = await create_run()

    content = await file.read()
    text = content.decode("utf-8")

    pulse = PULSE()
    result = await pulse.run(run_id, text)

    return {
        "run_id": run_id,
        "result": result
    }

    return {
        "message": "Analysis started",
        "run_id": run_id,
        "result": result
    }

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/health")
def health():
    return {"status": "PRISM Running"}
@app.get("/runs/{run_id}")
async def run_status(run_id: str):
    run = await get_run(run_id)

    if not run:
        return {"error": "Run not found"}

    return {
        "run_id": run[0],
        "status": run[1],
        "feature_spec": run[2]
    }


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = content.decode("utf-8")

        result = parse_document(text)

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
    return {
    "message": "Run created",
    "run_id": run_id
}