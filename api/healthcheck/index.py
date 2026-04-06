from fastapi import APIRouter
from ..base_router import BaseRouter


class HealthcheckRouter(BaseRouter):
    prefix = "/healthcheck"
    tags = ["Healthcheck"]
    responses = {404: {"description": "service not available"}}

    def setup_routes(self):
        @self.router.get("/")
        async def healthcheck():
            return {"description": "Server running healthy"}


router = HealthcheckRouter().router
