from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI() 

ACCESS_ORIGIN = [
    'http://localhost3000'
]

@app.get('/')
def home():
    return {'mensaje':'mifastapp'}


@app.get8("/users")
def get_user():
    return {"base lista de usuario":"users"}

@app.post("register")
def create_user():
    return{"boddy":[]}

@app.post("/loging")
def logging_user():
    return{}

if __name__ == '__main__':
    import uvicorn
uvicorn.run(
    'app:app',
    host='0.0.0.0',
    port=8000,
    reload=True
    
)    