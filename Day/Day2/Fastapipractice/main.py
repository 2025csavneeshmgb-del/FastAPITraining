from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():

    return {"page": "Home"}

@app.get("/about")
def about():
    return {"page": "About","author": "Ayaan"}

@app.get("/health")
async def health():
    result = await db.command("ping")
    return {"mongodb" : "Connected", "ping" : result["ok"]}

#POST request
@app.post("/create")
def create_something():
        return {"message": "Created successfully"}

#path parameters
@app.get("/student/{usn}")
def get_student(usn):
    return {"Result":"Distinction","usn": usn}

#path parameters with type hint
@app.get("/candidate/{rollno}")
def get_candidate(rollno:int):
    return {"Result":"Distinction","rollno": rollno,"type":str(type(rollno))}

#Pydantic model
class Item(BaseModel):
    name: str
    price: float
    is_stock: bool = True

@app.post("/item")
def create_item(item: Item):
    return {"recieved": item, "total_price": item.price*1.8}