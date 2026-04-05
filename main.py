from fastapi import FastAPI

from middleware import MiddlewareManager
from api import RouteManager

app = FastAPI()

middleware_manager = MiddlewareManager(app)
middleware_manager.register_middlewares()

route_manager = RouteManager(app)
route_manager.register_routes()
