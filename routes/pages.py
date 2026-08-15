from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})


@router.get("/payments-page")
def payments_page(request: Request):
    return templates.TemplateResponse(request, "payments.html", {"request": request})

@router.get("/customer-pages")
def customer_pages(request: Request):
    return templates.TemplateResponse(request, "customers.html", {"request": request})