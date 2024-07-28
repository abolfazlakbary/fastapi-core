from core.server.modify import app, run_server
import uvicorn
from core.config.data import configs
import asyncio


async def main():
    await run_server()
    config = uvicorn.Config(
        app=app,
        host=configs.app_host,
        port=configs.app_port
    )
    server = uvicorn.Server(config)
    await server.serve()
    


if __name__ == "__main__":
    asyncio.run(main())
