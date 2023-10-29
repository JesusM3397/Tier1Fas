from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class UpdatePlasticParts(BaseModel):
    chasis: int = 0
    buttons: int = 0
    back_cover: int = 0
    internal_coatings: int = 0

@app.post("/update-plastic-parts")
def update_plastic_parts(request: Request, update_data: UpdatePlasticParts):
    print('Datos recibidos desde api.py (Piezas Plásticas):')
    print(f"Chasis: {update_data.chasis}")
    print(f"Buttons: {update_data.buttons}")
    print(f"Back Cover: {update_data.back_cover}")
    print(f"Internal Coatings: {update_data.internal_coatings}")
    return {"mensaje": "Cantidades de piezas plásticas actualizadas correctamente"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
