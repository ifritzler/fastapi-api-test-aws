from fastapi import FastAPI
from app.constants.doc_tags import GLOBAL_TAG

app = FastAPI()


@app.get('/', tags=[GLOBAL_TAG])
def hello(name: str):
    return {
        "payload": f"Hello {name}"
    }
