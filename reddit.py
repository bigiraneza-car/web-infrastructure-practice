import requests
#import subreddit name
#10 newest posts
#the subreddit description
#number of subs
sub_reddit = ''
URL =''
response = requests.get(URL)
data = response.json()
reddit_name = data['name']
#depending of the order of the post, get them from the start 0-9 or the end -1 to -9


