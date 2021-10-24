import os, asyncio, discord, random, string, db
from discord.ext import commands
from dotenv import load_dotenv


# Get .env variable
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Check db
os.system("./script/check_db.sh")


# Setup cmd Prefix

bot = commands.Bot(command_prefix='!')

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

# Set custom status
@bot.event
async def on_ready(): 
    print(f'{bot.user} has connected to Discord!')
    activity = discord.Game(name="be in BETA", type=4)
    await bot.change_presence(activity=activity)

# MANAGE CMD
@bot.command(name='manage', help="  Your settings")
async def aboutDyver(ctx):
    if(True):
        OutStr = "TEST"
    else:
        OutStr = "Plz retry"
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(
        f'Hey {ctx.author.name}, to register your self you will need to awnser to my quetion :smile:. \n<IG_Nickname> <Rank> <Short_description>'
    )
    await ctx.send(f'Hey {ctx.author.name}, plz check your DM')


@bot.command(name='profile', help="  !profile <IG_nickname> <highest_rank> <bio> Create your profile")
async def profile(ctx, nickname, rank, bio):
    print("before for")
    if(db.not_register()):
        token = random_string_generator(32, string.ascii_letters)
        db.new_player(ctx, token, nickname, rank, bio)
        await ctx.send(f"Welcome aboard :smile:, here is a recap of your identity. if there is an error you can use `!update`\n **Nickname :** {nickname}\n**Highest rank :**{rank}\n**Bio :**{bio}")
        await ctx.author.create_dm()
        await ctx.author.dm_channel.send(
            f'Hey {ctx.author.name}, here is your recovery token account keep it private :smile:\n**TOKEN: **`{token}`')
    else:
        await ctx.send("Plz use !update")
        
    print("exit")


# Run bot
bot.run(TOKEN)