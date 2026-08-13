class GameSettings:
    DEFAULT_MAX_PLAYERS = 4
    DEFAULT_MAP_SIZE = (100, 100)
    DEFAULT_GAME_MODE = 'Survival'
    DEFAULT_GAME_DIFFICULTY = 'Normal'

class Color:
    RED = '#FF0000'
    GREEN = '#00FF00'
    BLUE = '#0000FF'
    WHITE = '#FFFFFF'
    BLACK = '#000000'

class KeyBindings:
    UP = 'W'
    DOWN = 'S'
    LEFT = 'A'
    RIGHT = 'D'
    ATTACK = 'SPACE'

class ScreenResolution:
    HD = (1280, 720)
    FULL_HD = (1920, 1080)
    UHD = (3840, 2160)

class GameModes:
    SINGLE_PLAYER = 'Single Player'
    MULTI_PLAYER = 'Multiplayer'

class ErrorCodes:
    GAME_NOT_FOUND = 404
    SERVER_ERROR = 500
    SUCCESS = 200