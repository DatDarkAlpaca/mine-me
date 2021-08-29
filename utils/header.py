from utils.config import config


def display():
    bot_name = config['bot_name']
    version = open('./VERSION').read()
    print(f"-=-= {bot_name} | v{version} =-=-")
