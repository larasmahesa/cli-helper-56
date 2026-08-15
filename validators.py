import time
import requests
from functools import wraps


def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    attempts += 1
                    print(f'Attempt {attempts} failed: {e}')
                    if attempts < max_attempts:
                        time.sleep(delay)
            raise Exception('Max retry attempts reached')
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Example usage of fetch_data
if __name__ == '__main__':
    try:
        data = fetch_data('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f'Error fetching data: {e}')