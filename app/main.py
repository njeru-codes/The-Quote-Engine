from fastapi import FastAPI



app = FastAPI()


@app.get('/home')
@app.get('/')
async def index():
    return {"home page"}