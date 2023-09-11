from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
from extractor1 import extract1
from extractor2 import extract2
import uuid
import os

app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_doc(
        file_format: str = Form(...),
        file: UploadFile = File(...),
):
    contents = file.file.read()

    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf"

    with open(file_path, "wb") as f:
        f.write(contents)

    try:
        if file_format == 'vr':
            data = extract1(file_path, file_format)
        elif file_format == 'mh':
            data = extract2(file_path, file_format)
        else:
            data = extract(file_path, file_format)
    except Exception as e:
        data = {
            'error': str(e)
        }

    if os.path.exists(file_path):
        os.remove(file_path)

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
