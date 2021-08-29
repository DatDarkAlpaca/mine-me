from json import load, dump
from pathlib import Path


config_path = './config.json'


# Loads a JSON file:
def get_json(filename: str):
    try:
        with open(filename) as json_file:
            return load(json_file)
    except AttributeError:
        raise AttributeError('Json: Unknown argument')
    except FileNotFoundError:
        raise FileNotFoundError(f"Json: {filename} wasn\'t found.")


# Create default Config:
def create_default_config():
    config_file = Path(config_path)

    if config_file.is_file():
        return

    data = {
        "bot_name": "Bot Name",
        "token": "Put your token here",
        "prefix": "!"
    }

    try:
        with open(config_path, 'w') as file:
            dump(data, file, indent=4)
    except Exception as e:
        print('[Error]: Could not create a default configuration file.', e)
        exit(1)
    else:
        print('[Config]: Configuration file created. Please modify it accordingly.')
        exit(1)


create_default_config()

config = get_json(config_path)
