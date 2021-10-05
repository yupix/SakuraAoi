from mi import Note


async def good_morning(word, ctx):
    text = word['replay'].format(ctx.author.name or ctx.author.username, 'さん')
    await Note(text=text, reply_id=ctx.id).send()


async def follow_me(word, ctx: Note):
    user = ctx.author.get_profile()
    username = user.name or user.username
    if user.is_following:
        ctx.author.unfollow()
        text = word['unfollow_replay'].format(username, 'さん')
    else:
        ctx.author.follow()
        text = word['follow_replay'].format(username, 'さん')
    await Note(text=text, reply_id=ctx.id).send()
