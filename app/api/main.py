import uvicorn
from fastapi import FastAPI
from api.routes import login, users,quotes
app = FastAPI()

# routes
app.include_router(quotes.router)
app.include_router(users.router)
app.include_router(login.router)









'''
@app.on_event("startup")
async def startup_event():
    try:
        db_conn = db_connection()
        db_users = db_conn.db_quotes.users
        # db_users.create_index("username", unique=True)
        # db_users.create_index('email', unique=True)
    except Exception as error:
        print(error)
    finally:
        db_conn.close()

'''