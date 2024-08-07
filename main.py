import nextcord
import os

from commands.hello import hello
from commands.pong import pong
from dotenv import load_dotenv

intents = nextcord.Intents.default()
intents.message_content = True

client = nextcord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
       await hello(message)
       
    if message.content.startswith('$ping'):
       await pong(message)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

if token==None:
    print("Token not found")
    exit()

client.run(token)