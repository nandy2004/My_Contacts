from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from supabase import create_client

db_url="https://wtjcezmhzeufdjzobedw.supabase.co"
db_key="sb_publishable_CrEWTvxmk-40zJpyLv3F2Q_QPeaL21_"
db = create_client(db_url, db_key)

app=FastAPI()

@app.get('/contacts')
def get_all_contacts():
    result= db.table('Contacts').select('*').execute()
    contacts = result.data
    return contacts

@app.get('/contact/{contact_id}')
def get_any_contact_by_id(contact_id :int):
    result1= db.table('Contacts').select('*').eq('id', contact_id).execute()
    data= result1.data
    return data

@app.post('/contacts/add')
async def add_contacts(request: Request):
    info = await request.json()
    result2 = db.table('Contacts').insert(info).execute()
    return "Data added successfully"

@app.put('/contacts/update/{contact_id}')
async def update_contacts_data(request: Request,contact_id: int):
    info1= await request.json()
    result3 = db.table('Contacts').update(info1).eq('id',contact_id).execute()
    return "Data updated sucessfully"

@app.delete('/contacts/delete/{contact_id}')
def delete_any_contact(contact_id):
    result4= db.table('Contacts').delete().eq('id',contact_id).execute()
    return "Data deleted Successfully"
