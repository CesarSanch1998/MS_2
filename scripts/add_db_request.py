from db.connection import session
from models.update_db import client_db

def add_client_db(data):
    client = client_db(contract=data.contract,
                       frame=data.frame,
                       slot=data.slot,
                       port=data.port,
                       onu_id=data.onu_id,
                       olt=data.olt,
                       fsp=data.fsp,
                       fspi=data.fspi,
                       name_1=data.name_1,
                       name_2=data.name_2,
                       state=data.state,
                       sn=data.sn,
                       device=data.device,
                       plan_name = data.plan_name,
                       spid = data.spid)
    
    
    #Mandar valores a guardar
    session.add(client)
    session.commit()
     
    return 'Client Add Successfully'