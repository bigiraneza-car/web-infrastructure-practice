import requests

API_KEY = ""
with open('.env') as f:
    for line in f:
        if line.startswith('KEY'):
           API_KEY = line.split(':')[1].strip().strip('"')
           break
    
url = f'https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key={API_KEY}'

# nasa = requests.get(url)
# nasa_obj= nasa.json()
# print(f"{url}")
response_obj = requests.get(url)
#check the status of our requests before printing the output
status = response_obj.status_code
if status != 200:
    print(f"something went wrong with status: {status}")
else:
    data = response_obj.json()
    print(data)
# with open() as f is used to download the images to do later

