class GameError(Exception):
    """Base class for all game-related exceptions."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class PlayerNotFoundError(GameError):
    """Raised when a player is not found."""
    def __init__(self, player_name):
        super().__init__(f"Player '{player_name}' not found.")
        self.player_name = player_name

class InvalidMoveError(GameError):
    """Raised for invalid moves in the game."""
    def __init__(self, move):
        super().__init__(f"Invalid move: '{move}'.")
        self.move = move

class GameOverError(GameError):
    """Raised when trying to perform an action after the game is over."""
    def __init__(self):
        super().__init__("The game is over. No further actions can be performed.")

class ServerConnectionError(GameError):
    """Raised when there's a server connection issue."""
    def __init__(self, url):
        super().__init__(f"Unable to connect to server at {url}.")
        self.url = url
