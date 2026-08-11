import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self):
        env_config = self.load_from_env()
        file_config = self.load_from_file()
        combined_config = self.merge_configs(env_config, file_config)
        return {**self.default_config, **combined_config}

    def load_from_env(self):
        return {key: os.getenv(key) for key in self.default_config.keys() if os.getenv(key) is not None}

    def load_from_file(self):
        try:
            with open('config.json') as config_file:
                return json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def merge_configs(self, env_config, file_config):
        return {**file_config, **env_config}

# Example usage:
# default_config = {'HOST': 'localhost', 'PORT': 8080}
# config_loader = ConfigLoader(default_config)
# print(config_loader.config)