import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/" #verilerin çekileceği internet sitesi url.

response = requests.get(url) #verileri çekme.

html_content = response.content #html içeriği.

soup = BeautifulSoup(html_content,"html.parser") #Verileri parçalıyoruz.

users_rating_input = float(input("Please, enter rating: ")) 

movie_titles = soup.find_all("td",{"class":"titleColumn"}) #html içerisinden tanımladığımız class'a göre buluyor.
movie_rating = soup.find_all("td",{"class":"ratingColumn imdbRating"}) #html içerisinden tanımladığımız class'a göre buluyor.

for title,rating in zip(movie_titles, movie_rating): 
    title = title.text #text olan verileri çekiyoruz.
    rating = rating.text #text olan verileri çekiyoruz.
    
    title = title.strip() 
    title = title.replace("\n","") #verilerdeki satır boşluklarını kaldırıyoruz.

    rating = rating.strip()
    rating = rating.replace("\n","") #verilerdeki satır boşluklarını kaldırıyoruz.

    
    if (float(rating) > users_rating_input): #Kullanıcının girdiği rating değerinden yüksek olan filmler gelir.
        print("Title of Movie: {} Rating of Movie: {}".format(title,rating))
