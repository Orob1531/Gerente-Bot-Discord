## ¡Hola! bienvenido a mi código en python.

##

```python

"""
Este es un bot de Discord que tiene un solo comando slash, 
/ping. El comando responde con un mensaje que muestra la latencia del bot.
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

@bot.event
async def on_ready():
    """
    Esta función se ejecuta cuando el bot se conecta al servidor de Discord.

    Parametros:
    - Ninguno.

    Returns:
    - Ninguno.

    Raises:
    - Ninguno.
    """
    print(f"Conectado como {bot.user} ({bot.user.id})")

@bot.slash_command(
    name="ping",
    description="Muestra el ping del bot."
)
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

@bot.slash_command(
    name="kick",
    description="Expulsa a un miembro del servidor."
)
@commands.has_permissions(kick_members=True)
async def kick(ctx: disnake.ApplicationCommandInteraction,
        member: disnake.Member, *, reason: str = "No se especificó una razón."):
    """
    Expulsa a un miembro del servidor.

    Parameters:
    - ctx: El contexto del comando.
    - member: El miembro del servidor que se va a expulsar.
    - Razon (opcional): La razón detrás de la expulsión.

    Returns:
    - Ninguno

    Raises:
    - discord.ext.commands.errors.BadArgument: Si se proporciona un miembro inválido.
    - discord.ext.commands.errors.MissingPermissions:
    Si el autor del comando no tiene permiso para expulsar miembros.
    """
    await member.kick(reason=reason)
    await ctx.response.send_message(f"El \
            miembro {member.mention} ha sido expulsado del servidor. Razón: {reason}")
@bot.slash_command(
    name="ban",
    description="Banea a un miembro del servidor."
)
@commands.has_permissions(ban_members=True)
async def ban(ctx: disnake.ApplicationCommandInteraction,
            member: disnake.Member, *, reason: str = "No se especificó una razón."):
    """
    Banea a un miembro del servidor.

    Parameters:
    - ctx: El contexto del comando.
    - member: El miembro del servidor que se va a banear.
    - reason (opcional): La razón detrás del baneo.

    Returns:
    - Ninguno

    Raises:
    - discord.ext.commands.errors.BadArgument: Si se proporciona un miembro inválido.
    - discord.ext.commands.errors.MissingPermissions:
    Si el autor del comando no tiene permiso para banear miembros.
    """
    await member.ban(reason=reason)
    await ctx.response.send_message(f"El\
            miembro {member.mention} ha sido baneado del servidor. Razón: {reason}")
@bot.slash_command(
    name="unban",
    description="Desbanea a un miembro del servidor."
)
@commands.has_permissions(ban_members=True)
async def unban(ctx: disnake.ApplicationCommandInteraction,
            member: str, *, reason: str = "No se especificó una razón."):
    """
    Desbanea a un miembro del servidor.

    Parameters:
    - ctx: El contexto del comando.
    - member: El nombre y discriminador (ejemplo: "usuario#0000") del usuario a desbanear.
    - reason (opcional): La razón detrás del desbaneo.

    Returns:
    - Ninguno

    Raises:
    - discord.ext.commands.errors.BadArgument: Si se proporciona un miembro inválido.
    - discord.ext.commands.errors.NotFound: Si la persona que se intenta desbanear no está baneada.
    - discord.ext.commands.errors.MissingPermissions: 
    Si el autor del comando no tiene permiso para desbanear miembros.
    """
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user, reason=reason)
            await ctx.response.send_message(f"El\
                    miembro {user.mention} ha sido desbaneado del servidor. Razón: {reason}")
            return

    await ctx.send(f"No se encontró un usuario baneado con el nombre {member}.")
@bot.slash_command(
    name="clear",
    description="Elimina un número específico de mensajes de un canal."
)
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

bot.run('DISCORD_BOT_TOKEN')

```

