import feedparser

d = feedparser.parse('https://psyrozvytok.com.ua/rss-feed-450446572451.xml')

def last_article():
    print(d.entries[-1].links[0])

last_article()

