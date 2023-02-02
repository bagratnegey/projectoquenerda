
import asyncpg
from data import config
import asyncio

class Database:
    def __init__(self):
        loop=asyncio.get_event_loop()
        self.pool:asyncio.pool.Pool=loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                database=config.DBNAME,
                password=config.PGPASSWORD,
                host=config.IP,
                port=config.DBPORT,
                loop=loop
            )
        )


    @staticmethod
    def format_args(sql,partmeters:dict):
        sql+='AND'.join([
            f'{item}=${num}'for num,item in enumerate(partmeters,start=1)
        ])
    async def create_table_users(self):
        await self.pool.execute('''
        CREATE TABLE IF NOT EXISTS users( 
        id INT NOT NULL,
        phone_number VARCHAR(255) NOT NULL,
        CONSTRAINT "user_pk" PRIMARY KEY("id"))
        WITH (
        OIDS=FALSE
        ); ''')
    async def add_user(self,id,phone_number):
        sql='INSERT INTO users(id,phone_number)VALUES(1&,2&)'
        try:
            await self.pool.execute(sql,id,phone_number)
        except asyncpg.exceptions.UniqueViolationError:

            pass