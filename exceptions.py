class GameError(Exception):
    """Base class for all game-related exceptions."""
    pass

class InvalidMoveError(GameError):
    """Raised when an invalid move is attempted."""
    def __init__(self, message="Invalid move."):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(GameError):
    """Raised when a required resource is not found."""
    def __init__(self, resource_type, resource_id):
        self.message = f'{resource_type} with ID {resource_id} not found.'
        super().__init__(self.message)

class InsufficientResourcesError(GameError):
    """Raised when there are not enough resources for an action."""
    def __init__(self, required, available):
        self.message = f'Required: {required}, Available: {available}'
        super().__init__(self.message)

# Example usage within the game logic
def perform_move(move):
    if not is_valid_move(move):
        raise InvalidMoveError()

# Function to simulate resource checking
def check_resources(required, available):
    if required > available:
        raise InsufficientResourcesError(required, available)


# This is where game logic would typically handle exceptions
try:
    perform_move("left")
except GameError as e:
    print(f'Game Error: {e}')