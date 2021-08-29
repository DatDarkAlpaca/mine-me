from bot.extensions import load_extensions
from bot import Bot, HelpFormat, config

import utils.header as header

bot = Bot(command_prefix=config['prefix'], command_attrs=dict(hidden=True), help_command=HelpFormat())

# Header:
header.display()

# Loading:
load_extensions(bot)


try:
    bot.run(config['token'])
except Exception as e:
    print('[Error]: Failed to log-in', e)
