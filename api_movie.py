import requests

show = "girls"
url = f"https://api.tvmaze.com/search/shows?q={show}"
 #why did he use the response-obj?? To read about
response_obj = requests.get(url)

json_data= response_obj.json()
# print(json_data)
for i in range(0, 5):
    print(f'----- show {i} -----')
    show_name = json_data[i]['show']["name"]
    print(f"Name of the show is: {show_name}")

    show_genres = []

    print(f"The genres of the show are:")
    for genre in json_data[i]['show']['genres']:
        
        show_genres.append(genre)
    
    for genre in show_genres:
        print(genre)

    synopsis = json_data[i]['show']['summary']
    print(f"The summary of the movie: {synopsis}")
    print(f"End of movie {i} summary")
    print()