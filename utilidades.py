"""
Este es el apartado de comando de utilidades del bot "Gerente".\n
Comandos:\n
 - /clear\n
 - /ping\n
"""

import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = disnake.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

#Comando /ping.
@bot.slash_command(
    name="ping",
    description="Muestra el ping del bot.")
async def ping(ctx: disnake.ApplicationCommandInteraction):
    """
    Muestra el ping del bot.

    Parameters:
    - ctx: El contexto del comando.

    Returns:
    - Ninguno.

    Raises:
    - Ninguno.
    """
    await ctx.response.send_message(f"Pong! Latencia: {bot.latency*1000:.2f} ms")
#Comando /clear.
@bot.slash_command(
    name="clear",
    description="Elimina un número específico de mensajes de un canal.")

@commands.has_permissions(manage_messages=True)
async def clear(ctx: disnake.ApplicationCommandInteraction, amount: int):
    """
    Elimina un número específico de mensajes de un canal.

    Parameters:
    - ctx: El contexto del comando.
    - amount: El número de mensajes que se eliminarán.

    Returns:
    - Ninguno.

    Raises:
    - discord.ext.commands.errors.MissingPermissions: 
    Si el autor del comando no tiene permiso para eliminar mensajes.
    """
    await ctx.channel.purge(limit=amount + 1)
    await ctx.response.send_message(f"{amount} mensajes han sido eliminados.")

# Inicio del bot
bot.run("DISCORD_BOT_TOKEN")
