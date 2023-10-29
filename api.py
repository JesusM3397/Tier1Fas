from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests

app = FastAPI()
app.mount("/templates", StaticFiles(directory="templates"), name="templates")


@app.get("/", response_class=HTMLResponse)
def index():
    with open("templates/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/clientrequest", response_class=HTMLResponse)
def clientrequest():
    with open("templates/clientrequest.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/clientship", response_class=HTMLResponse)
def clientship():
    with open("templates/clientship.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/clientsell", response_class=HTMLResponse)
def clientsell():
    with open("templates/clientsell.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2perequest", response_class=HTMLResponse)
def t2perequest():
    with open("templates/t2perequest.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2peship", response_class=HTMLResponse)
def t2peship():
    with open("templates/t2peship.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2pesell", response_class=HTMLResponse)
def t2pesell():
    with open("templates/t2pesell.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2pewarehouse", response_class=HTMLResponse)
def t2pewarehouse():
    with open("templates/t2pewarehouse.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2pcrequest", response_class=HTMLResponse)
def t2pcrequest():
    with open("templates/t2pcrequest.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2pcship", response_class=HTMLResponse)
def t2pcship():
    with open("templates/t2pcship.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2pcsell", response_class=HTMLResponse)
def t2pcsell():
    with open("templates/t2pcsell.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2pcwarehouse", response_class=HTMLResponse)
def t2pcwarehouse():
    with open("templates/t2pcwarehouse.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/logship", response_class=HTMLResponse)
def logship():
    with open("templates/logship.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


class UpdateQuantity(BaseModel):
    screens: int = 0
    cameras: int = 0
    batteries: int = 0
    processors: int = 0


@app.post("/update-quantities")
def update_quantities(request: Request, update_data: UpdateQuantity):
    data = {
        "screens": update_data.screens,
        "cameras": update_data.cameras,
        "batteries": update_data.batteries,
        "processors": update_data.processors,
    }

    main_api_url = "http://localhost:8001/update-quantities"

    response = requests.post(main_api_url, json=data)

    if response.status_code == 200:
        print("Datos enviados con éxito a main.py")
    else:
        print("Error al enviar datos a main.py")


class UpdatePlasticParts(BaseModel):
    chasis: int = 0
    buttons: int = 0
    back_cover: int = 0
    internal_coatings: int = 0


@app.post("/update-plastic-parts")
def update_plastic_parts(request: Request, update_data: UpdatePlasticParts):
    data = {
        "chasis": update_data.chasis,
        "buttons": update_data.buttons,
        "back_cover": update_data.back_cover,
        "internal_coatings": update_data.internal_coatings,
    }

    main_api_url = "http://localhost:8002/update-plastic-parts"

    response = requests.post(main_api_url, json=data)

    if response.status_code == 200:
        return {"message": "Datos enviados con éxito a main.py en el puerto 8002"}
    else:
        return {"error": "Error al enviar datos a main.py en el puerto 8002"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
