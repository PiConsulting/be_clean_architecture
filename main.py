import uvicorn
from app import create_app

app = create_app()

# Run server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
