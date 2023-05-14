import list as lst
import list_queue as queue
import message_object as msg
import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix='$', intents=intents)

# VARS ------------------------------------------------------------
history = lst.List_chained(msg.Message("First message", "Bot"))
first_node = queue.Node(None, None)
waiting_queue = queue.Queue()
actual_history_node = history.first_node
actual_history_name = None


# COMMANDS --------------------------------------------------------


@client.event
async def on_message(message):
    if str(message.content)[0] == "$":
        await client.process_commands(message)



@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    global actual_history_node
    global actual_history_name
    if user.bot:
        return
    elif emoji == "❌" and reaction.message.author.id == 830811392378535968:
        await reaction.message.delete()
        return
    elif emoji == "⏮️" and reaction.message.author.id == 830811392378535968:
        if actual_history_node.previous_node is not None:
            actual_history_node = actual_history_node.previous_node
            while actual_history_node.data.user != actual_history_name:
                if actual_history_node.previous_node is not None:
                    actual_history_node = actual_history_node.previous_node
                    print(actual_history_node.data.user)
                    print(actual_history_name)
                else:
                     break
            if actual_history_node.data.user == actual_history_name:
                await reaction.message.edit(content=str(actual_history_node.data))
        return
    elif emoji == "⬅️" and reaction.message.author.id == 830811392378535968:
        if actual_history_node.previous_node is not None:
            actual_history_node = actual_history_node.previous_node
            await reaction.message.edit(content=str(actual_history_node.data))
        return
    elif emoji == "➡️" and reaction.message.author.id == 830811392378535968:
        if actual_history_node.following_node is not None:
            actual_history_node = actual_history_node.following_node
            await reaction.message.edit(content=str(actual_history_node.data))
        return
    elif emoji == "⏭️" and reaction.message.author.id == 830811392378535968:
        if actual_history_node.following_node is not None:
            actual_history_node = actual_history_node.following_node
            while actual_history_node.data.user != actual_history_name:
                if actual_history_node.following_node is not None:
                    actual_history_node = actual_history_node.following_node
                    print(actual_history_node.data.user)
                    print(actual_history_name)
                else:
                    break
            if actual_history_node.data.user == actual_history_name:
                await reaction.message.edit(content=str(actual_history_node.data))
        return


@client.command(pass_context=True)
async def S(ctx, *, arg):
    message = msg.Message(arg, ctx.message.author.name)
    history.append(message)
    await ctx.message.add_reaction("✅")

@client.command()
async def V(ctx, arg):
    index = int(arg)
    global actual_history_node
    actual_history_node = history.get(index)
    message = await ctx.send(str(history.view(index)))
    await message.add_reaction("⬅️")
    await message.add_reaction("➡️")
    await message.add_reaction("❌")

@client.command()
async def VF(ctx, arg):
    name = str(arg)
    global actual_history_name
    global actual_history_node
    actual_history_node = history.get_from(name)
    actual_history_name = name
    message = await ctx.send(str(history.view_from(name)))
    await message.add_reaction("⏮️")
    await message.add_reaction("⬅️")
    await message.add_reaction("➡️")
    await message.add_reaction("⏭️")
    await message.add_reaction("❌")

@client.command()
async def C(ctx):
    history.clear(msg.Message("First message", "Bot"))
    await ctx.message.add_reaction("✅")

@client.command()
async def L(ctx):
    await ctx.channel.send(str(history.length))
    await ctx.message.add_reaction("✅")

client.run("ODMwODExMzkyMzc4NTM1OTY4.GwbZe-.Yuvlfa7xdphQLMcungr0un2qaGuSSQ-G16y_tc")
