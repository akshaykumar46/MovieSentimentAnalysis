import requests
url = "http://0.0.0.0:80/predict"

data="Our Indian Nationalist Hero Shri Atal Bihari ji is truly Bharat Ratna. Well made and beautifully portrayed. I love to watch Pankaj Tripathi, he's acting skill is very natural, classic and fabulous. In between sometime I felt seeing him as original Atalji. I would like to thanks director for making this true biopic movie. I wasn't knowing many facts about our political history, After watching the movie I did started to read about our all Prime Ministers. Specifically I read about Shri Atal ji's political journy. Everyone must watch this movie and especially youth must have to watch and know about our national and political history."

resp = requests.post(url, json={'review': data})

# Print result
print(resp.json())