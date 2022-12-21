from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

    
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/hello")
async def say_hello(name: str):
    return {"message": f"Hello Michael"}


@app.get("/inputs")
async def getInputs():
    x = ["graduacao","especializacao","mestrado","doutorado","idioma","conhecimento","competencia","certificacao","capacitacao","experiencia"]
    y = [        3.0,             3.0,       1.0,        1.0,     2.0,           4.0,          4.0,           4.0,          3.0,          4.0]
    dip = {"inputs": [{"name": k, "value": v} for k,v in dict(zip(x, y)).items()]}
    return json.dumps(dip)
