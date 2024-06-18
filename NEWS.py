import feedparser as fe
import time
url = "http://www.trthaber.com/sondakika.rss"
news = fe.parse(url)
for n in news.entries:
    print(n.title)
    for i in range(10):
        print()
time.sleep(30)
#News

    



