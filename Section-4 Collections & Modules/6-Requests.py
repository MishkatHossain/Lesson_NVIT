import requests

# The requests library is a simple and powerful tool used to send HTTP 
# requests in Python. It allows you to communicate with web servers, 
# retrieve data from the web, and send data to remote servers.

# install pip install requests


# A simple Get request
# A GET request is used to retrieve data from a server. Here's a basic 
# example:

response = requests.get('https://en.wikipedia.org/wiki/Batman')
print(response.status_code)  # Shows the HTTP status code (e.g., 200 
print(response.text)         # Shows the content of the response
print(response) #response 200
# print(help(response))



# Sending Parameters in URLs (Query Parameters)
# When you need to send additional data in the URL, like search terms, 
# you can pass parameters using the params argument:

params = {'q': 'python png'}
response = requests.get('https://www.google.com/search', params=params)
print(response.url)  # Shows the URL with the parameters included




# A POST request sends data to the server, typically when submitting 
# forms.

data = {'username': 'test', 'password': '1234'}
response = requests.post('https://example.com/login', data=data)
print(response.status_code)


# When the server responds with JSON (commonly used in APIs), you can 
# easily parse it:

response = requests.get('https://api.github.com')
data = response.json()  # Convert the JSON response into a Python dictionary
print(data['current_user_url'])


# The requests library simplifies the process of working with HTTP requests in Python. 
# It's widely used for interacting with web APIs and retrieving web data.












