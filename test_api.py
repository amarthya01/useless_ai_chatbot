import requests

url = "http://127.0.0.1:5000/chat"  # URL of your Flask endpoint
payload = {"message": "Why is the sky blue?"}

response = requests.post(url, json=payload)  # Sending a POST request
print(response.json())  # Print the response from the Flask server
