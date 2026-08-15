from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.api import router as api_router
from routes.customers import router as customers_router
from routes.pages import router as pages_router
from routes.payments import router as payments_router
from routes.orders import router as orders_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(customers_router)
app.include_router(api_router)
app.include_router(pages_router)
app.include_router(orders_router)
app.include_router(payments_router)
app.include_router(customers_router)