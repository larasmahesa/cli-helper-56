import random
import string

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None
    except IOError:
        return None


def save_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError:
        return False
    return True


def get_random_choice(choices):
    if not choices:
        return None
    return random.choice(choices)


def display_message(message):
    print(f'[INFO] {message}')