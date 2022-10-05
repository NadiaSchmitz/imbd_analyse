from bs4 import BeautifulSoup
from requests import get

url_list = []
response_list = []
response_end_list = []
numbers = []
titles = []
ratings = []
votes = []

url_1 = "https://www.imdb.com/search/title/?title_type=feature&release_date=2020-01-01,2020-12-31&sort=user_rating,desc&count=250"
url_list.append(url_1)

response_1 = get(url_1)
response_list.append(response_1)

response_1_end = BeautifulSoup(response_1.text, "lxml")
response_end_list.append(response_1_end)

film_amount_string = response_1_end.find("div", class_="desc").find("span").text

film_amount = film_amount_string.split("f ")[-1]
film_amount = film_amount.split(" ")[0]
film_amount = int(film_amount.replace(",",""))

#page_number = 251
#while page_number < film_amount:
#    url_list.append(url_1 + "start=" + str(page_number) + "&ref_=adv_nxt")
#    page_number = page_number + 250

#i = 1
#while i < len(url_list):
#    response_list.append(get(url_list[i]))
#    i = i + 1

#i = 1
#while i < len(response_list):
#    response_end_list.append(BeautifulSoup(response_list[i].text, "lxml"))

films = response_1_end.find("div", class_="lister-list")

for film_block in films:
    film_block = films.find_all("h3", class_="lister-item-header")

for film_block in films:
    numbers.append(film_block.find("span"))
    titles.append(film_block.find("a"))
    ratings.append(film_block.find("strong"))
    #votes.append(film_block.find("span"))

for film_block in films:
    print("Number", "Title", "Rating", "Votes")
    print(numbers, titles, ratings)
