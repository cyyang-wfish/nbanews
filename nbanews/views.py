import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from nbanews.models import Post
from nbanews.serializers import PostSerializer
from rest_framework import viewsets

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    url = 'https://nba.udn.com/nba/index?gr=www'
    html = requests.get(url)
    html.encoding = "utf-8"

    sp = BeautifulSoup(html.text, 'html.parser')
    dbArray = [['s', 's', 's', 's'], ['s', 's', 's', 's'],
               ['s', 's', 's', 's'], ['s', 's', 's', 's']]

    # 新聞標題
    newsTitle = sp.select("#news_body")[0].find_all("h3")
    for i in range(0, len(newsTitle)):
        dbArray[i][0] = newsTitle[i].text

    # 新聞內容
    newsContent = sp.select("#news_body")[0].find_all("p")
    for i in range(0, len(newsContent)):
        dbArray[i][1] = newsContent[i].text

    # 新聞連結
    newsLink = sp.select("#news_body")[0].find_all("a")
    # newsLink = sp.select("#news_body a")
    for count, item in enumerate(newsLink, start=0):
        dbArray[count][2] = "https://nba.udn.com" + item.get("href")

    # 圖片連結
    img = sp.select("#news_body")[0].find_all(["img"])
    for count, item in enumerate(img, start=0):
        dbArray[count][3] = item.get("src")

    # 寫入資料庫
    for count, item in enumerate(dbArray, start=0):
        Post.objects.get_or_create(newsNum=count + 1, newsTitle=dbArray[count][0],
                            newsContent=dbArray[count][1], newsLink=dbArray[count][2], imgLink=dbArray[count][3])

    post_list = Post.objects.all()

    return render(request, 'index.html', {
        'post_list': post_list,
    })