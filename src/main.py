from fastapi.applications import FastAPI
import uvicorn
import blabinha_api.routes as core_routes

app_runner = FastAPI(title="Blabinha API")

app_runner.include_router(core_routes.router)

if __name__ == "__main__":
    uvicorn.run(app_runner)
