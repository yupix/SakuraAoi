import importlib

import yaml
from mi import Note, commands

with open('word.yml', mode='r', encoding='utf-8') as f:
    word_list: dict = dict(yaml.safe_load(f.read())['word'])


class ChatCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name='ｺﾝﾆﾁﾜ')
    async def hello(self, ctx):
        await Note(text='ｺﾝﾆﾁﾜ').send()

    @commands.Cog.listener()
    async def on_mention(self, ws, ctx):
        func = word_list[ctx.text]['func']
        module = importlib.import_module(func['path'])
        await getattr(module, func['name'])(word_list[ctx.text], ctx)


def setup(bot):
    bot.add_cog(ChatCog(bot))
