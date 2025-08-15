import discord
import os
from discord.ext import commands
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv("DISCORD_TOKEN")
channel_id = 1404434756388524160  # 채널 ID

already_ran = False

@bot.event
async def on_ready():
    global already_ran
    if already_ran:
        return
    already_ran = True 

    now = datetime.now(KST)  # 한국 시간
    channel = bot.get_channel(channel_id)

    if channel:
        embed = discord.Embed(
            title=now.strftime('%m월 %d일'),
            description="내용은 스레드를 통해 작성해 주세요.",
            color=discord.Color.orange()
        )

        main_message = await channel.send(embed=embed)

        # 스레드 생성
        await main_message.create_thread(
            name=now.strftime('%m월 %d일'),
            auto_archive_duration=1440
        )

    await bot.close()

bot.run(token)
