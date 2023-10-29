from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class UpdateQuantity(BaseModel):
    screens: int = 0
    cameras: int = 0
    batteries: int = 0
    processors: int = 0

@app.post("/update-quantities")
def update_quantities(request: Request, update_data: UpdateQuantity):
    print('Datos recibidos desde api.py:')
    print(f"Screens: {update_data.screens}")
    print(f"Cameras: {update_data.cameras}")
    print(f"Batteries: {update_data.batteries}")
    print(f"Processors: {update_data.processors}")
    return {"mensaje": "Cantidades actualizadas correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
