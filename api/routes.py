from api import healthcheck, games


class RouteManager:
    def __init__(self, app):
        self.app = app

    def register_routes(self):
        self.app.include_router(healthcheck)
        self.app.include_router(games)
