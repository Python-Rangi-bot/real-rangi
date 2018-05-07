import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord import opus 
import asyncio
import time
import random
import os
import functools, youtube_dl

bot = commands.Bot("")
@bot.event
async def on_ready():
    print("준비 되었느니라")

class Main_Commands():
    def _init_(self, bot):
        self.bot = bot

@bot.command()
async def 랑이야():
    possible_responses = [
        '왜 불렀느냐?',
        '내가 보고 싶었느냐?',
        '으에에에? 날 불렀느냐?',
        '놀아줄것이냐?!',
        '너는 누구냐?',
        '내가 요괴들의 왕이니라!',
        '으냐아아앗?'
        '내가 이쁘다는 것이냐? 처음듣는구나 흐헷',
        '나는 사랑 받고 싶느니라~!',
        '나도 커질 것이니라! 커질 것이니라',
        '아우우우우! 랑이님은 지금 없는 거에요',
        ]
    await bot.say(random.choice(possible_responses))

@bot.event
async def on_message(message):
    if message.content ==("누구"):
        await bot.send_message(message.channel, "으에에에!나...날 아직 모른다는 것이냐?!")
    await bot.process_commands(message)
    
@bot.command()    
async def 안녕():
    possible_responses = [
        '안녕!',
        '인사 해주길 바라는 것이느냐?'
        ]
    await bot.say(random.choice(possible_responses))

@bot.command()    
async def 하():
    possible_responses = [
        '무언가 ㅈ 망한 것이냐?',
        '뭐 떔에 탄식을 하느냐?',
        '뭔진 몰라도 슬프구나...',
        ]
    await bot.say(random.choice(possible_responses))
    
@bot.command()
async def 랑이():
    possible_responses = [
        '왜 불렀느냐?',
        '내가 보고 싶었느냐?',
        '으에에에? 날 불렀느냐?',
        '무엇이느냐?',
        ]
    await bot.say(random.choice(possible_responses))
    
from discord import opus
  
from discord import opus
  
@bot.event
async def on_ready(): 
    try:
        if not discord.opus.is_loaded():
             discord.opus.load_opus('libopus-0.dll')
    except OSError:
            pass
def setup(bot):
    bot.add_cog(Music(bot))
    print('풍악을 울려라!')
    
async def play(ctx):
    channel = discord.utils.get(ctx.guild.channels, type=discord.VoiceChannel)
    voice_client = await channel.connect()
    player = discord.FFmpegPCMAudio('file.mp3')
    player = discord.PCMVolumeTransformer(player, volume=1)
    voice_client.play(player)
    
import functools, youtube_dl
url = 'youtube url'
opts = {"format": 'webm[abr>0]/bestaudio/best',"ignoreerrors": True,"default_search": "auto","source_address": "0.0.0.0",'quiet': True}
ydl = youtube_dl.YoutubeDL(opts)
func = functools.partial(ydl.extract_info, url, download=False)
info = func()
player = discord.FFmpegPCMAudio(info['url'])

bot.run(os.environ['BOT_TOKEN']) 
