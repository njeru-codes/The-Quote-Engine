from fastapi import FastAPI
from .config import Settings
from .routes import quotes

app = FastAPI()

# routes
app.include_router(quotes.router)


@app.get('/home')
@app.get('/')
async def index():
    return {"home page"}