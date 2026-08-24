from fastapi import FastAPI

app = FastAPI(
    title="Universal FastAPI Backend Starter",
    version="Final"
)

@app.get("/health")
def health():
    return {"status": "healthy"}
