##¡Hola! bienvenido a mi código en python.

##

```python

"""

Este es un bot de Discord que realiza funciones básicas de moderación.

Incluye comandos para expulsar, banear y desbanear a usuarios del servidor.

También hay un comando para borrar mensajes de un canal en particular.

"""

import os

import discord

from discord.ext import commands

from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo `.env`

load_dotenv()

# Configurar el bot

intents = discord.Intents.default()

intents.members = True

intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Variables de autenticación

CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")

CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Autenticar el bot

@bot.event

async def on_ready():

    """

    Imprime un mensaje cuando el bot esté listo y conectado al servidor.

    """

    print(f'Conectado como: {bot.user.name} - {bot.user.id}')

# Imprime un mensaje cuando el bot esté listo y conectado al servidor

# Comando de kick

@bot.command()

@commands.has_permissions(kick_members=True)

async def kick(ctx, member: discord.Member, *, reason=None):

    """

    Expulsa a un usuario del servidor.

    Parameters:

    - member: El miembro del servidor que se va a expulsar.

    - reason (opcional): La razón detrás de la expulsión.

    Returns:

    - Un mensaje que indica que el usuario ha sido expulsado.

    Raises:

    - discord.ext.commands.errors.BadArgument: Si se proporciona un miembro inválido.

    - discord.ext.commands.errors.MissingPermissions:

    Si el autor del comando no tiene permiso para expulsar miembros.

    """

    await member.kick(reason=reason)

    await ctx.send(f'Usuario {member} expulsado. Razón: {reason}')

# Comando de ban

@bot.command()

@commands.has_permissions(ban_members=True)

async def ban(ctx, member: discord.Member, *, reason=None):

    """

    Banea a un usuario del servidor.

    Parameters:

    - member: El miembro del servidor que se va a banear.

    - reason (opcional): La razón detrás del baneo.

    Returns:

    - Un mensaje que indica que el usuario ha sido baneado.

    Raises:

    - discord.ext.commands.errors.BadArgument: Si se proporciona un miembro inválido.

    - discord.ext.commands.errors.MissingPermissions:

    Si el autor del comando no tiene permiso para banear miembros.

    """

    await member.ban(reason=reason)

    await ctx.send(f'Usuario {member} baneado. Razón: {reason}')

# Comando de unban

@bot.command()

@commands.has_permissions(ban_members=True)

async def unban(ctx, *, member):

    """

    Desbanea a un usuario del servidor.

    Parameters:

    - member: El nombre y discriminador (ejemplo: "usuario#0000") del usuario a desbanear.

    Returns:

    - Un mensaje que indica que el usuario ha sido desbaneado.

    Raises:

    - discord.ext.commands.errors.BadArgument: Si se proporciona un miembro inválido.

    - discord.ext.commands.errors.NotFound: Si la persona que se intenta desbanear no está baneada.

    - discord.ext.commands.errors.MissingPermissions: 

    Si el autor del comando no tiene permiso para desbanear miembros.

    """

    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:

        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):

            await ctx.guild.unban(user)

            await ctx.send(f'Usuario {user.name} desbaneado')

            return

    raise commands.BadArgument(f'Usuario {member} no encontrado en la lista de baneos')

# Comando de limpiar mensajes

@bot.command()

@commands.has_permissions(manage_messages=True)

async def clear(ctx, amount=5):

    """

    Elimina una cantidad específica de mensajes del canal actual.

    Parameters:

    - amount (opcional): El número de mensajes que se eliminarán. Por defecto son 5.

    Returns:

    - Un mensaje que indica que los mensajes se han eliminado.

    Raises:

    - discord.ext.commands.errors.MissingPermissions: 

    Si el autor del comando no tiene permiso para eliminar mensajes.

    """

    await ctx.channel.purge(limit=amount + 1)

    await ctx.send(f'{amount} mensajes han sido borrados')

# Manejador de errores

@bot.event

async def on_command_error(ctx, error):

    """

    Maneja los errores que ocurren al ejecutar un comando.

    Parameters:

    - ctx: El contexto del comando que se intentó ejecutar.

    - error: El error que se levantó al ejecutar el comando.

    Returns:

    - Un mensaje de error que indica que se produjo un error al ejecutar el comando.

    Raises:

    - No lanza ninguna excepción.

    """

    if isinstance(error, commands.CommandNotFound):

        await ctx.send('Comando no encontrado')

# Inicio del bot

bot.run('DISCORD_BOT_TOKEN')

```

