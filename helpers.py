import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming you want JSON data
        except requests.RequestException:
            attempt += 1
            if attempt < retries:
                time.sleep(delay)
            else:
                raise NetworkError(f'Failed to fetch {url} after {retries} attempts')

# Example usage (commented out to avoid execution on import)
# if __name__ == '__main__':
#     try:
#         data = retry_request('https://api.example.com/data')
#         print(data)
#     except NetworkError as e:
#         print(e)