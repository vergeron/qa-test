import requests
import time

# def get_backend_message(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text.strip()
#         else:
#             return f"Error: Status code {response.status_code}"
#     except requests.exceptions.RequestException as e:
#         return f"Error: {e}"
#
# if __name__ == "__main__":
#     backend_url = "http://127.0.0.1:55090"  # Replace with your actual backend service URL
#     message = get_backend_message(backend_url)
#     print(message)



# Define the URLs for your frontend and backend services
FRONTEND_URL = "http://127.0.0.1:55090"  # Replace with your frontend service URL
BACKEND_EXPECTED_MESSAGE = "Hello from the Backend!"

import requests
import re

# Define the URLs for your frontend and backend services
FRONTEND_URL = "http://127.0.0.1:55090"  # Replace with your frontend service URL
BACKEND_EXPECTED_MESSAGE = "Hello from the Backend!"

def strip_html_tags(html):
    # Use regex to remove HTML tags from the string
    return re.sub(r'<[^>]*>', '', html)

def get_backend_message():
    try:
        response = requests.get(FRONTEND_URL)
        if response.status_code == 200:
            frontend_message = strip_html_tags(response.text.strip())
            if frontend_message == BACKEND_EXPECTED_MESSAGE:
                return True, f"Integration test passed: Frontend displays '{frontend_message}' correctly."
            else:
                return False, f"Integration test failed: Frontend displays '{frontend_message}', expected '{BACKEND_EXPECTED_MESSAGE}'."
        else:
            return False, f"Error: Frontend returned status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Error: {e}"

if __name__ == "__main__":
    passed, message = get_backend_message()
    print(message)


