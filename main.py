from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates



app = FastAPI(debug=True)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def homepage (request:Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )



