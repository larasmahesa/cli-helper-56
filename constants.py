GAMING_DATA_CONSTANTS = {
    'MAX_PLAYERS': 100,
    'GAME_TYPES': ['battle royale', 'team deathmatch', 'capture the flag'],
    'PLAYER_STATISTICS': [
        'kills',
        'deaths',
        'assists',
        'score'
    ],
    'DEFAULT_SETTINGS': {
        'difficulty': 'normal',
        'graphics': 'high',
        'audio': 70
    },
    'ITEM_RARITIES': {
        'common': 0,
        'uncommon': 1,
        'rare': 2,
        'epic': 3,
        'legendary': 4
    }
}

def get_game_type(index):
    try:
        return GAMING_DATA_CONSTANTS['GAME_TYPES'][index]
    except IndexError:
        return 'invalid game type'

def get_item_rarity(level):
    return next((k for k, v in GAMING_DATA_CONSTANTS['ITEM_RARITIES'].items() if v == level), 'unknown')

