import discord
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("MTM0NDA0MDkwNTM1MDU3ODE5Ng.GgWLVF.GrHqonUpE2Se4Bx-EQmcADsn70Zz0dNVtT_EDo")
OPENAI_API_KEY = os.getenv("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")

# Set up OpenAI
openai.api_key = OPENAI_API_KEY

# Set up Discord client
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore bot messages

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.content}]
    )

    reply = response["choices"][0]["message"]["content"]
    await message.channel.send(reply)

client.run(TOKEN)
