import re

def validate_username(username):
    if not isinstance(username, str) or not 3 <= len(username) <= 20:
        raise ValueError('Username must be a string between 3 and 20 characters')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise ValueError('Username can only contain alphanumeric characters and underscores')
    return True

def validate_game_choice(choice, valid_choices):
    if choice not in valid_choices:
        raise ValueError(f'Invalid choice. Choose from {valid_choices}')
    return True

def validate_positive_integer(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError('Value must be a positive integer')
    return True

# Example usage in a main processing loop
if __name__ == '__main__':
    valid_choices = ['easy', 'medium', 'hard']
    try:
        username = input('Enter your username: ')
        validate_username(username)
        game_choice = input(f'Choose your game difficulty {valid_choices}: ')
        validate_game_choice(game_choice, valid_choices)
        level = int(input('Select a level (positive integer): '))
        validate_positive_integer(level)
        print('All inputs are valid!')
    except ValueError as e:
        print(f'Error: {e}')