import os
from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url=os.getenv("DB_URL"),
        modules={"models": ["app.models"]} 
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()
