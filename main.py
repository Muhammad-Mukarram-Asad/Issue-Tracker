from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI();

app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(issues_router)


@app.get("/", tags=["root"])
async def root():
    """Landing endpoint with a pointer to the interactive API docs"""
    return {
        "message": "Welcome to the FastAPI Issue Tracker API",
        "docs": "/docs",
        "redoc": "/redoc",
    }
