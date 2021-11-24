import argparse
import asyncio
import datetime
import os
import subprocess

from dbmanager.dbmanager import DbManager
from dotenv import load_dotenv
from loguru import logger
from mi import Emoji, Router
from mi.ext import commands, task
from mi.next_utils import check_multi_arg
from mi.note import Note, NoteContent

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

    @task.loop(3600)
    async def backup(self):
        pg_user_name = env.get('PG_USER_NAME')
        pg_user_password = env.get('PG_USER_PASSWORD')
        pg_host = env.get('PG_HOST')
        pg_port = env.get('PG_PORT')
        pg_db_name = env.get('PG_DB_NAME')
        file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")

        subprocess.call(f'pg_dump postgresql://{pg_user_name}'
                        f':{pg_user_password}'
                        f'@{pg_host}:{pg_port}/{pg_db_name} > ./backup'
                        f'/{file_name}', shell=True)

    async def on_ready(self, ws):
        logger.info(f'{self.i.username}にログインしました')
        if check_multi_arg(args.db, args.i):
            await AutoMigrate().generate().upgrade()
        await self.backup.start()
        await Router(ws).channels(['home'])  # globalタイムラインに接続

    async def on_message(self, ctx: NoteContent):
        print('koko')
        logger.info(f'{ctx.author.username}さんがノートしました。{ctx.text}')
        logger.warning(ctx.author.get_profile().is_followed)

    async def on_emoji_add(self, ctx: Emoji):
        await Note(f':{ctx.name}:が追加されたようです!\n`:{ctx.name}:`').send()

    async def on_mention(self, ctx: NoteContent):
        print(f'{ctx.author.username}さんにメンションされました: {ctx.text}')

    async def on_follow(self, ctx):
        # await db_manager.commit(User(username=ctx.user.username))
        pass


if __name__ == '__main__':
    db_manager = DbManager(session=session)
    loop = asyncio.new_event_loop()
    loop.run_in_executor(None, run_webhook)
    bot = SakuraAoi(command_prefix='tu!')
    load_dotenv(verbose=True)
    env = os.environ
    bot.run(token=os.environ.get('TOKEN'), uri=env.get('URI'))
