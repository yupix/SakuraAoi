from mi import Note


async def good_morning(word, ctx):
    print(ctx)
    text = word['replay'].format(ctx.author.name or ctx.author.username, 'さん')
    await Note(text=text, reply_id=ctx.id).send()
