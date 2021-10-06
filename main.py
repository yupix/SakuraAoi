import argparse
import asyncio
import os
import sys

from dbmanager.dbmanager import DbManager
from dotenv import load_dotenv
from loguru import logger
from mi import Follow, Note, Router, commands
from mi.utils import check_multi_arg

from db import session
from sakuraAoi.modules.auto_migrate import AutoMigrate
from sakuraAoi.modules.webhook import run_webhook
from sakuraAoi.sql.models.user import User

EXTENSION_LIST = ['sakuraAoi.cogs.chat']

parser = argparse.ArgumentParser()
parser.add_argument('--db', action='store_true')
parser.add_argument('-i', action='store_true')
args = parser.parse_args()


async def migrate():
    await AutoMigrate().generate().upgrade()


class SakuraAoi(commands.Bot):
    def __init__(self, command_prefix, **kwargs):
        super().__init__(command_prefix, **kwargs)
        for extension in EXTENSION_LIST:
            self.load_extension(extension)

    async def on_ready(self, ws):
        logger.info(f'{self.i.username}にログインしました')
        if check_multi_arg(args.db, args.i):
            await AutoMigrate().generate().upgrade()
        await Router(ws).channels(['home'])  # globalタイムラインに接続

    async def on_message(self, ctx: Note):
        print('koko')
        logger.info(f'{ctx.author.username}さんがノートしました。{ctx.text}')
        logger.warning(ctx.author.get_profile().is_followed)

    async def on_mention(self, ws, ctx: Note):
        print(f'{ctx.author.username}さんにメンションされました: {ctx.text}')

    async def on_follow(self, ws, ctx: Follow):
        await db_manager.commit(User(username=ctx.user.username))


if __name__ == '__main__':
    db_manager = DbManager(session=session)
    loop = asyncio.new_event_loop()
    loop.run_in_executor(None, run_webhook)
    bot = SakuraAoi(command_prefix='tu!')
    load_dotenv(verbose=True)
    env = os.environ
    bot.run(token=os.environ.get('TOKEN'), uri=env.get('URI'))
