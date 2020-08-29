import requests

response = requests.get('https://api.github.com') #To make a GET request, invoke requests.get().

# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not found :(')
# IS THE SAME AS:......

if response:
    print('Success!')
    print(response.json())
    print(response.headers)
else:
    print('Error')
