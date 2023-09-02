from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
# async def welcome() -> dict:
#     return {
#         "message": "Hello World"
#     }

async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }

app.include_router(todo_router)