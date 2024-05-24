from pydantic import BaseModel
from typing import Optional
from typing import ClassVar

# ----------------------------------------------------------------------
# Clases actualizar usuario en DB
# ----------------------------------------------------------------------
class update_client(BaseModel):
    """Datos necesarios para actualizar el usuario en la db  ."""
    contract : str
    frame : int
    slot : int
    port  : int
    onu_id : int
    olt : int
    fsp : str
    fspi : str
    name_1 :  str
    name_2 : str
    status : str
    state : str
    sn : str
    device :  str
    plan_name : str
    spid : int

class first_structure_update(BaseModel):
    """Estructura superior de la consulta ."""
    api_key:str
    data:update_client

# ----------------------------------------------------------------------
# Clases Agregar usuario en DB
# ----------------------------------------------------------------------

class add_client(BaseModel):
    """Datos necesarios para actualizar el usuario en la db  ."""
    contract : str
    frame : int
    slot : int
    port  : int
    onu_id : int
    olt : int
    fsp : str
    fspi : str
    name_1 :  str
    name_2 : str
    status : str
    state : str
    sn : str
    device :  str
    plan_name : str
    spid : int

class first_structure_add(BaseModel):
    """Estructura superior de la consulta ."""
    api_key:str
    data:add_client