import discord
from discord.ext import commands



bot = commands.Bot(command_prefix='//')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))



@bot.command()
async def test(ctx):
    await ctx.send('working :)')

#gives robin regards YT channal
@bot.command()
async def YT(ctx):
    await ctx.send('https://www.youtube.com/channel/UCgDUK8ONMwwI63G8arPKj5g/')

#gives dragonblade316's YT channal and linkedin
@bot.command()
async def bot_creator(ctx):
    await ctx.send('https://www.youtube.com/channel/UCTOnC0xbuPkIV0YVwgx_emw')

@bot.command()
async def kill(ctx, arg):

    #for fun it cant kill me lol
    if 'dragonblade316' == arg:
        await ctx.send('cant kill him he built this thing')
        return 0
    
    await ctx.send(f'abcdefg {arg} my enemy \n stick a sword up his nose slash and burn there he goes \n abcdefg {arg} my enemy')






bot.run('ODY0OTE3MDk1MDc3NTExMTc4.YO8a0A.Lf0nT8FSm6lgj1ByMMW7wHEhJAY')



