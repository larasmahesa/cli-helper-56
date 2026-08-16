import random
import json

def roll_dice(num_dice=1, num_sides=6):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls


def save_game_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_game_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def generate_character(name, level):
    character = {
        'name': name,
        'level': level,
        'health': level * 10,
        'mana': level * 5,
        'attributes': {
            'strength': random.randint(1, 20),
            'dexterity': random.randint(1, 20),
            'intelligence': random.randint(1, 20)
        }
    }
    return character


def display_character_info(character):
    info = f"Name: {character['name']}\nLevel: {character['level']}\nHealth: {character['health']}\nMana: {character['mana']}\nAttributes: {character['attributes']}"
    print(info)