from constants.secrets import settings
from fastapi import FastAPI
from routes import RouteManager
app = FastAPI()

route_manager = RouteManager(app)
route_manager.register_routes()
