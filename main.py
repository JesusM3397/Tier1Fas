from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_bienvenido():
    return {"mensaje": "Bienvenido al api de ...."}
