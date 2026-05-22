from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from db import Base, engine



app = FastAPI(debug=True)

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def homepage (request:Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )

@app.get("/register")
def register_page(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={}
    )
