import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f"Default config not found: {self.default_config_path}")
        with open(self.default_config_path, 'r') as config_file:
            return json.load(config_file)

    def update_config(self, user_config_path):
        if os.path.exists(user_config_path):
            with open(user_config_path, 'r') as user_file:
                user_config = json.load(user_file)
            self.config.update(user_config)
        else:
            print(f"User config not found, using defaults.")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __str__(self):
        return json.dumps(self.config, indent=4)

# Example usage:
# loader = ConfigLoader('defaults.json')
# loader.update_config('user_config.json')
# print(loader.get('key_name', 'default_value'))
