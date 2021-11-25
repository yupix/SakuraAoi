import argparse
import asyncio
import datetime
import math
import os
import subprocess
import tarfile
import time

from dbmanager.dbmanager import DbManager
from dotenv import load_dotenv
from loguru import logger
from mega import Mega
from mi import Emoji, Router
from mi.ext import commands, tasks
from mi.next_utils import check_multi_arg
from mi.note import Note, NoteContent

from db import session
from sakuraAoi.modules.auto_migrate import AutoMigrate
from sakuraAoi.modules.webhook import run_webhook

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

    @tasks.loop(3600)
    async def backup(self):
        mega_email = env.get('MEGA_EMAIL')
        mega_password = env.get('MEGA_PASSWORD')
        file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
        pg_user_name = env.get('PG_USER_NAME')
        pg_user_password = env.get('PG_USER_PASSWORD')
        pg_host = env.get('PG_HOST')
        pg_port = env.get('PG_PORT')
        pg_db_name = env.get('PG_DB_NAME')
        logger.info('データベースのバックアップを開始します')
        await Note('データベースのバックアップを開始します').send()
        start_time = time.time()
        subprocess.Popen(f'pg_dump postgresql:'
                         f'//{pg_user_name}'
                         f':{pg_user_password}'
                         f'@{pg_host}:{pg_port}/{pg_db_name} > ./backup'
                         f'/{file_name}',
                         shell=True
                         )
        with tarfile.open(f'./backup/{file_name}.tar.gz', 'w:gz') as tr:
            tr.add(f'./backup/{file_name}')
        mega = Mega()
        m = mega.login(mega_email, mega_password)
        m.upload(os.path.abspath(f"./backup/{file_name}.tar.gz"))
        logger.success(f'MEGAへのバックアップのアップロードが完了しました')
        elapsed_time = math.floor(time.time() - start_time)
        await Note(f'データベースのバックアップが完了しました 処理時間: {elapsed_time}秒').send()

    async def on_ready(self, ws):
        logger.info(f'{self.i.username}にログインしました')
        if check_multi_arg(args.db, args.i):
            await AutoMigrate().generate().upgrade()
        await Router(ws).channels(['home', 'global'])  # globalタイムラインに接続
        self.backup.start()

    async def on_message(self, ctx: NoteContent):
        logger.info(f'{ctx.author.username}さんがノートしました。{ctx.content}')

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
