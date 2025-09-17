from fastapi import FastAPI
from app.controllers import order_controller
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

app = FastAPI()
app.include_router(order_controller.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)

