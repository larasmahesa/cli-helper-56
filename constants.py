class GameConstants:
    MAX_PLAYERS = 100
    MIN_PLAYERS = 1
    DEFAULT_COLOR = 'blue'
    DEFAULT_DIFFICULTY = 'normal'
    SUPPORTED_MODES = ['single', 'multiplayer']

    @staticmethod
    def validate_player_count(count):
        if not isinstance(count, int):
            raise ValueError('Player count must be an integer.')
        if count < GameConstants.MIN_PLAYERS or count > GameConstants.MAX_PLAYERS:
            raise ValueError('Player count must be between {} and {}.'.format(GameConstants.MIN_PLAYERS, GameConstants.MAX_PLAYERS))

    @staticmethod
    def validate_game_mode(mode):
        if mode not in GameConstants.SUPPORTED_MODES:
            raise ValueError(f'Game mode must be one of {GameConstants.SUPPORTED_MODES}.')

    @staticmethod
    def get_default_settings():
        return {
            'color': GameConstants.DEFAULT_COLOR,
            'difficulty': GameConstants.DEFAULT_DIFFICULTY,
        }