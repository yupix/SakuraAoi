import importlib
import re

import sympy as sympy
import yaml
from mi.ext import commands
from mi.ext.commands import Context
from mi.note import NoteContent

with open('word.yml', mode='r', encoding='utf-8') as f:
    word_file = yaml.safe_load(f.read())
    word_list: dict = dict(word_file.get('word', {}))
    regex_list: dict = dict(word_file.get('regex', {}))


class ChatCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name='数式')
    async def hello(self, ctx: Context, formula, *args):
        arg = formula + ''.join(args)
        await NoteContent(text=f'{formula} の答えは {sympy.sympify(arg)} です！',
                          reply_id=ctx.message.id).send()

    @commands.Cog.listener()
    async def on_mention(self, ws, ctx):
        action_list = [{'list': regex_list[i], 'name': i} for i in regex_list
                       if re.search(i, ctx.text)]
        action_list.extend(
            [{'list': word_list[i], 'name': i} for i in word_list if
             i == ctx.text])
        for action in action_list:
            action_base = action.get('list')
            func = action_base.get('func', None)
            if func is None:
                replay = action.get('replay')
                await Note(text=replay, reply_id=ctx.id).send()
            else:
                module = importlib.import_module(func['path'])
                await getattr(module, func['name'])(action_base, ctx)


def setup(bot):
    bot.add_cog(ChatCog(bot))
