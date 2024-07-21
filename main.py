from core.server.modify import app, run_server
import uvicorn
from core.config.data import configs
import asyncio


if __name__ == "__main__":
    asyncio.run(
        run_server(),
        uvicorn.run(
        app=app,
        host=configs.app_host,
        port=configs.app_port
     )
    )
