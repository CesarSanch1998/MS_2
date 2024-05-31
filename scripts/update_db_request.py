from db.connection import session
from models.update_db import client_db
from scripts.add_db_request import add_client_db

def update_client_send(data):
    print(f"{data.contract} fspid:{data.fsp}/{data.onu_id} sn:{data.sn}")
    # print(data.contract)
    # request = session.query(client_db).filter(client_db.contract == data.contract).delete()
    # session.commit()
    try:
        request = session.query(client_db).filter(client_db.contract == data.contract).first()
        if request == None:
            add_client_db(data)
            return "Cliente no econtrado en la db agregando en la db"
        else:
            # session.query(client_db).filter(client_db.contract == data.contract).update(data.dict())
            #UPDATE DATA IN POSGRESTSQL DEFINITIOS
            request.contract = data.contract
            request.frame = data.frame
            request.slot = data.slot
            request.port  = data.port
            request.onu_id = data.onu_id
            request.olt = data.olt
            request.fsp = data.fsp
            request.fspi = data.fspi
            request.name_1 = data.name_1
            request.name_2 = data.name_2
            request.state = data.state
            request.sn = data.sn
            request.device = data.device
            request.plan_name = data.plan_name
            request.spid = data.spid

            #Mandar valores a guardar
            session.add(request)
            session.commit()
            session.refresh(request) 
        return 'Client Update Successfully'
    except Exception as e:
        session.rollback()
        raise e  # o maneja la excepción de otra manera (registra el error, devuelve un mensaje, etc.)
    finally:
        session.close() 