from enum import StrEnum

from fastapi import FastAPI

app = FastAPI()


# ===STANDARD PARAMETERS===


@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id": item_id}


# ---


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get(
    "/users/{user_id}"
)  # NOTE: this must be AFTER the declared paths like "me", because it will evaluate "me" to the "{user_id}".
async def read_user(user_id: str):
    return {"user_id": user_id}


# ---


@app.get(
    "/characters"
)  # NOTE: Only this, the first, one will work since the path matches first!
async def read_characters():
    return ["Rick", "Morty"]


@app.get("/characters")  # NOTE: And this will NEVER work!
async def read_characters2():
    return ["Hornet", "Lace"]


# === PREDIFINED VALUES ===


class ModelName(StrEnum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images."}

    return {"model_name": model_name, "message": "Have some residuals."}


# ===PATH CONVERTOR===


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
