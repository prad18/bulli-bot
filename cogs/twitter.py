import discord
from discord.ext import commands
import sys

sys.path.append('D:\Bulli-Bot')
from tweet import *

def rod(x:float):
    return x/1000000


class Twitter(commands.Cog):
    #tweepy intergation
    @commands.command()
    async def followers(self, ctx , username):
        user=api.get_user(screen_name=username)
        count=user.followers_count
        if count>1000000 or count==1000000:
            follow=int(rod(user.followers_count))
            await ctx.send(f"{user.screen_name} has {round(follow)}M followers")
        else:
            await ctx.send(f"{user.screen_name} has {count} followers")

    @commands.command()
    async def user_tweet(self, ctx, username):
        urls=get_tweet_urls(username)
        for url in urls:
            await ctx.send(url)


async def setup(client):
    await client.add_cog(Twitter(client))

