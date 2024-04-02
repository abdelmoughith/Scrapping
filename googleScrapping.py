import urllib.parse
import bs4
import requests
import webbrowser


def uncode(encodedStr):
    return urllib.parse.unquote(encodedStr)


value = input('Google search (Top 5 results will appear) : ')
value = value.replace(' ', '+')

res = requests.get('https://www.google.com/search?q=', params={'q': value})
soup = bs4.BeautifulSoup(res.text, features='html.parser')
#scrapping


links = soup.select('a')
#filtering
links = list(map(lambda x:x.get('href'), links))
links = list(filter(lambda x:x[:6] == '/url?q', links))
links = list(map(lambda x:x[7:], links))
links = list(map(uncode, links))
for i in range(5):

    webbrowser.open(links[i])


