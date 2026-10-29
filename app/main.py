
from fastapi import FastAPI

app = FastAPI(
    title="CloudDeploy API",
    description="API for the CloudDeploy CI/CD deployment platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "project": "CloudDeploy",
        "message": "Containerized CI/CD Deployment Platform",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "0.1.1", "service": "clouddeploy-api"}
