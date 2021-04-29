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

I reccomend u to use replit just because its the same IDE im using and other IDE's might have problems.
But if ur using another one. For the enviroment variables, make a file named .env, and then put this:
"TOKEN=<YOUR TOKEN HERE>"
It should kind of look like this:
"TOKEN=ODM3MDA4MjkxMzUxMjMyNTIz.YImStw.-aPLEnE1rUHRk4QL-WJDaeUEhfs"
But replace the token with ur bots token.
