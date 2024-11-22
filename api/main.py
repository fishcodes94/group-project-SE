import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .routers import menu, menu_item, order_details, orders, payment, recipes, resources, sandwiches
from .models import model_loader
from .dependencies.config import conf

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize models
model_loader.index()

# Include the routers
app.include_router(menu.router)
app.include_router(menu_item.router)
app.include_router(order_details.router)
app.include_router(orders.router)
app.include_router(payment.router)
app.include_router(recipes.router)
app.include_router(resources.router)
app.include_router(sandwiches.router)

# Load the index route
indexRoute.load_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
