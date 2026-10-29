from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers.patient_routers import router as patient_router

app = FastAPI(
    title="University Patient Management API",
    description="FastAPI In-Memory CRUD assignment for managing university patient records.",
    version="1.0.0"
)

app.include_router(patient_router)


@app.get("/", tags=["Root"])
def root():
    return RedirectResponse(url="/docs")
