from fastapi import FastAPI

app = FastAPI() 

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