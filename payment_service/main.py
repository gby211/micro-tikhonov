import mongoengine
from fastapi import FastAPI

from deps import init_tracer
from router import router
from auth.router import router as router_auth
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator




app = FastAPI(

)

DB_NAME = 'mydb'


@app.on_event("startup")
async def startup():
    mongoengine.connect(host=f"mongodb://mongo_product:27017/{DB_NAME}", alias=DB_NAME)
    Instrumentator().instrument(app).expose(app)
    init_tracer()


@app.on_event("shutdown")
async def shutdown():
    mongoengine.disconnect(alias=DB_NAME)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/_health')
async def health_check():
    return {
        'status': 'Ok'
    }

app.include_router(router, prefix='/v1')

app.include_router(router_auth, prefix='/v1')
