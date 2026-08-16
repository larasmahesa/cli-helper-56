def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty")
    if len(user_input) > 100:
        raise ValueError("Input must be 100 characters or less")
    return True

def process_game_input():
    while True:
        try:
            user_input = input("Enter your command: ")
            validate_input(user_input)
            # Code to process valid input
            print(f"Processing command: {user_input}")
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
        except KeyboardInterrupt:
            print("Exiting...")
            break