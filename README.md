# Discord-Bot-Tutorial
be sure to watch the episodes: https://www.youtube.com/watch?v=r4EEs5N3VeM&list=PLLZSNIRwjIgKr1bZvMbQB2HswQ7Zu5XhQ

To make a basic command use this:
```python
import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="!")
token = os.environ.["TOKEN"]

bot.run(token)
```
