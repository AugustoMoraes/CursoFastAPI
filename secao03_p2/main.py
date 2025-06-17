from fastapi import FastAPI
from routes import usuario_router, cursos_router
from secao03_p2.routes import cursos_router

app = FastAPI()

app.include_router(cursos_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])


if __name__ == '__main__': 
    
    import uvicorn

    uvicorn.run("main:app", host="0.0.0", port=8000, reload=True)