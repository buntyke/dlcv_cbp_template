# import modules
import os
import sys
import logging
from pathlib import Path

# import third party imports
import uvicorn
from fastapi import FastAPI, File, UploadFile

# instantiate fastapi app
app = FastAPI()

# setup logger for debugging
logging.basicConfig(level=logging.INFO)

### load model here ###

logging.info("Model loaded successfully")

@app.get("/health")
def health_check():
    """
    Health check endpoint
    
    Returns:
        Dict: Message indicating the API is up and running
    """
    return {"message": "Image Classifier API is up and running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Prediction endpoint

    Args:
        file (UploadFile): Image file to classify

    Returns:
        Dict: Predicted class
    """

    ### perform inference here ###
    return {"prediction": ""}

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
