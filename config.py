import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='defaults.json', user_config_path='user_config.json'):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)
        self.final_config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, path):
        if os.path.exists(path):
            with open(path, 'r') as file:
                return json.load(file)
        return {}

    def merge_configs(self, default, user):
        return {**default, **user}

    def get(self, key, default=None):
        return self.final_config.get(key, default)

# Example usage (not to be executed in the module itself)
# if __name__ == '__main__':
#     loader = ConfigLoader()
#     print(loader.get('some_key', 'default_value'))