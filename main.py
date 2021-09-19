import json
import os

from dotenv import load_dotenv
from loguru import logger
from mi import Bot, Note, Router

load_dotenv(verbose=True)


class SakuraAoi(Bot):
    async def on_ready(self, ws):
        logger.info(f'{bot.i.username}にログインしました')
        await Router(ws).channels(['global'])


    async def on_message(self, ws, ctx: Note):
        logger.info(f'{ctx.author.username}さんがノートしました。{ctx.text}')


if __name__ == '__main__':
    bot = SakuraAoi()
    bot.run(token=os.environ.get('TOKEN'), uri=os.environ.get('URI'))
