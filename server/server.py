import uvicorn

from fastapi import FastAPI, File
from fastapi.staticfiles import StaticFiles
from swapper import swap_faces

import cv2
import numpy as np

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# falsification + face = faceficate
@app.post("/func/faceficate")
async def faceficate(src_url: str, file: bytes = File(...)):
    arr = np.asarray(bytearray(file), dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    output_url = swap_faces(src_url, img)
    return {'result': output_url}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8888, log_level="info")
