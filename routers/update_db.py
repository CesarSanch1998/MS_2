from fastapi import APIRouter
from fastapi import HTTPException
from schema.model_client import first_structure_update
#/////////////Scripts//////////////////////////////////////////
from scripts.update_db_request import update_client_send
import os
from dotenv import load_dotenv

load_dotenv()
update_db = APIRouter()

@update_db.post("/update-client-db")
def update_client_db(data: first_structure_update):
    # Api key smartolt ----------------------
    if data.api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    # response = "aceptado"
    response = update_client_send(data.data)
    return HTTPException(status_code=202, detail=response)
