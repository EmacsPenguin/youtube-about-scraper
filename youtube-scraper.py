import requests

youtube_about_section_url = "put the url here"

#Downloading Website Data Through Requests
response = requests.get(youtube_about_section_url)

#Isolating Discription (it is in the 807 quotation mark, on the 20th line)
discription = response.text.splitlines()[20].split("\"")[807]
print(discription)
    
