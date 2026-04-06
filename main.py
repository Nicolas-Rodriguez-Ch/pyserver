from fastapi import FastAPI

from middleware import MiddlewareManager
from api import RouteManager

app = FastAPI()
route_manager = RouteManager(app)
route_manager.register_routes()

middleware_manager = MiddlewareManager(app)
middleware_manager.register_middlewares()
