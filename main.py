from fastapi import FastAPI, Request
from pydantic import BaseModel
import time
app = FastAPI()

class UpdateQuantity(BaseModel):
    cameras: int = 0
    biometric_sensors: int = 0
    baseband: int = 0
    power_management: int = 0
    processor: int = 0
    nand: int = 0
    dram: int = 0
    accelerometer: int = 0
    battery: int = 0
    microphone: int = 0
    speakers: int = 0

@app.post("/update-quantities")
def update_quantities(request: Request, update_data: UpdateQuantity):
    time.sleep(5)
    print('Datos recibidos desde api.py:')
    print(f"Cameras: {update_data.cameras}")
    print(f"Biometric Sensors: {update_data.biometric_sensors}")
    print(f"Baseband: {update_data.baseband}")
    print(f"Power Management: {update_data.power_management}")
    print(f"Processor: {update_data.processor}")
    print(f"NAND: {update_data.nand}")
    print(f"DRAM: {update_data.dram}")
    print(f"Accelerometer: {update_data.accelerometer}")
    print(f"Battery: {update_data.battery}")
    print(f"Microphone: {update_data.microphone}")
    print(f"Speakers: {update_data.speakers}")
    
    return {"mensaje": "Cantidades actualizadas correctamente"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

