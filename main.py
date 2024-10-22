#Definimos el modelo
from typing import Optional
from pydantic import BaseModel, EmailStr
#Modelos
class Blog(BaseModel):
    id: Optional[int]=None
    user: str
    mensaje: str
#API
from fastapi import FastAPI, HTTPexeption
app = FastAPI()

#Base de datos simulada con un array

blog_db =[]

#Crear Blog con post se crea algo
@app.post("/blogs/",response_model =Blog)
def crear_blog(blogs:Blog):
    blogs.id = len(blog_db) +1
    blog_db.append(blogs)
    return blogs