import discord
from discord.ext import commands
import datetime
import pytz  # Import pytz for timezone support

TOKEN = '' # Replace with your actual bot token
intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Channel ID where notifications should be sent
notification_channel_id = 936159703858307123  # Replace with the channel ID where notifications should be sent

# Set the timezone to Bangkok (Indochina Time)
bangkok_timezone = pytz.timezone('Asia/Bangkok')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Twitch!"), status=discord.Status.online)

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if after.channel and before.channel:  # Check for both channels to detect a move
            await send_move_notification(member, before.channel, after.channel)
        elif after.channel and not before.channel:
            # Member joined a voice channel
            await send_join_notification(member, after.channel)
        elif before.channel and not after.channel:
            # Member left a voice channel
            await send_leave_notification(member, before.channel)

async def send_join_notification(member, channel):
    notification_channel = bot.get_channel(notification_channel_id)

    if notification_channel:
        logo_url = '' # Replace with your actual logo URL
        embed = discord.Embed(
            description=f'{member.mention} **joined voice channel** <#{channel.id}>',
            color=discord.Color.green()
        )
        embed.set_author(name='𝗠𝗲𝗺𝗯𝗲𝗿 𝗲𝗻𝘁𝗲𝗿𝘀 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝗻𝗻𝗲𝗹',icon_url=logo_url)
        embed.set_footer(text=f'Time now • {datetime.datetime.now(bangkok_timezone).strftime("%a %d %b %Y, %I:%M%p")}')
        await notification_channel.send(embed=embed)
    else:
        print(f'Error: Could not find notification channel with ID {notification_channel_id}')

async def send_leave_notification(member, channel):
    notification_channel = bot.get_channel(notification_channel_id)

    if notification_channel:
        logo_url = '' # Replace with your actual logo URL
        embed = discord.Embed(
            description=f'{member.mention} **left voice channel** <#{channel.id}>',
            color=discord.Color.red()
        )
        embed.set_author(name='𝗠𝗲𝗺𝗯𝗲𝗿 𝗹𝗲𝗮𝘃𝗲𝘀 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝗻𝗻𝗲𝗹',icon_url=logo_url)
        embed.set_footer(text=f'Time now • {datetime.datetime.now(bangkok_timezone).strftime("%a %d %b %Y, %I:%M%p")}')
        await notification_channel.send(embed=embed)
    else:
        print(f'Error: Could not find notification channel with ID {notification_channel_id}')

async def send_move_notification(member, before_channel, after_channel):
    notification_channel = bot.get_channel(notification_channel_id)

    if notification_channel:
        logo_url = '' # Replace with your actual logo URL
        embed = discord.Embed(
            description=f'{member.mention} **switched voice channels** <#{before_channel.id}> **to** <#{after_channel.id}>',
            color=discord.Color.blue()
        )
        embed.set_author(name='𝗠𝗲𝗺𝗯𝗲𝗿 𝗺𝗼𝘃𝗲𝘀 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝗻𝗻𝗲𝗹',icon_url=logo_url)
        embed.set_footer(text=f'Time now • {datetime.datetime.now(bangkok_timezone).strftime("%a %d %b %Y, %I:%M%p")}')
        await notification_channel.send(embed=embed)
    else:
        print(f'Error: Could not find notification channel with ID {notification_channel_id}')

bot.run(TOKEN)