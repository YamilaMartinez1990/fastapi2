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
#Ver Blog por id
@app.get("/blogs{blogs_id}",response_model =Blog)
def obtener_blogs(blogs_id:int):
    for blogs in blog_db:
        if blogs.id == blogs_id:
            return blogs
        raise HTTPexeption(status_code=404, detail="Blog no encontrado")
    #Listar mensajes asi nos trae todo
@app.get("/blogs/",response_model =list[Blog])
def listar_blog():
    return blog_db
#Actualizar Blog
@app.put("/blogs/{blogs_id}",response_model =Blog)
def actualizar_blog(blogs_id: int,blogs:Blog):
    for index, blogs in enumerate(blog_db):
        if blogs.id == blogs_id:
            blog_db[index] = blogs
            return blogs
    raise HTTPexeption(status_code=404, detail="Blog no encontrada")
#Eliminar Blog
@app.delete("/blogs/{blogs_id}",response_model =Blog)
def eliminar_blog(blogs_id: int):
    for index, blogs in enumerate(blog_db):
        if blogs.id == blogs_id:
            del blog_db[index] 
            return {"detail":"Mensaje eliminado"}
    raise HTTPexeption(status_code=404, detail="Blog no encontrado")
