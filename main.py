import list as lst
import message_object as msg
import discord
from discord.ext import commands
import Key
import json
import requests
import binary_tree_setup as bts

intents = discord.Intents.all()

client = commands.Bot(command_prefix='$', intents=intents)

# VARS ------------------------------------------------------------
history_json = json.load(open("list.json", "r"))
history = lst.List_chained(msg.Message(history_json["history"][0]["text"], history_json["history"][0]["user"]))
history.load()

tree = bts.setup()

actual_history_node = history.first_node
actual_history_name = None
actual_tree_node = None

def get_random_dog_image_url():
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url)
    data = res.json()
    if "message" in data:
        return data["message"]
    return None
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
    global  actual_tree_node
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
                else:
                    break
            if actual_history_node.data.user == actual_history_name:
                await reaction.message.edit(content=str(actual_history_node.data))
        return
    elif emoji == "◀️" and reaction.message.author.id == 830811392378535968:
        if type(actual_tree_node) != str and actual_tree_node.left is not None:
            actual_tree_node = actual_tree_node.left
            if type(actual_tree_node) == str:
                await reaction.message.edit(content=actual_tree_node)
            else:
                await reaction.message.edit(content=str(actual_tree_node.text))
    elif emoji == "▶️" and reaction.message.author.id == 830811392378535968:
        if type(actual_tree_node) != str and actual_tree_node.right is not None:
            actual_tree_node = actual_tree_node.right
            if type(actual_tree_node) == str:
                await reaction.message.edit(content=actual_tree_node)
            else:
                await reaction.message.edit(content=str(actual_tree_node.text))


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
    admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
    if admin_role in ctx.author.roles:
        history.clear(msg.Message("First message", "Bot"))
        await ctx.message.add_reaction("✅")
    else:
        await ctx.message.add_reaction("🛑")


@client.command()
async def L(ctx):
    await ctx.channel.send(str(history.length))
    await ctx.message.add_reaction("✅")


@client.command()
async def SAVE(ctx):
    admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
    if admin_role in ctx.author.roles:
        history.save()
        await ctx.message.add_reaction("✅")
    else:
        await ctx.message.add_reaction("🛑")

@client.command()
async def DL(ctx):
    admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
    if admin_role in ctx.author.roles:
        await ctx.send(file=discord.File(r'list.json'))
        await ctx.message.add_reaction("✅")
    else:
        await ctx.message.add_reaction("🛑")

@client.command()
async def SA(ctx, arg):
    await ctx.send(tree.print_subject(str(arg)))
    await ctx.message.add_reaction("✅")


@client.command()
async def HELP(ctx):
    global actual_tree_node
    actual_tree_node = tree.root
    message = await ctx.send(actual_tree_node)
    await ctx.message.add_reaction("✅")
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    await message.add_reaction("❌")

@client.command()
async def DOG(ctx):
    random_dog_image = get_random_dog_image_url()
    if not random_dog_image:
        await ctx.message.add_reaction("🛑")
    else:
        await ctx.message.add_reaction("✅")
        await ctx.send(random_dog_image)


client.run(Key.key)

quit(history.save())
