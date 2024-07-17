from core.server.modify import app
import uvicorn
from core.config.data import configs


uvicorn.run(
    app=app,
    host=configs.app_host,
    port=configs.app_port
)
