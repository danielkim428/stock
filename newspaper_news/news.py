from newspaper import Article

url = 'http://v.media.daum.net/v/20170604205121164'

a = Article(url, languague='ko')
a.download()
a.parse()
a.nlp()

print(a.title)
print(a.text[:150])
