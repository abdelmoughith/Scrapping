import bs4
import requests
import urllib.parse


url = 'https://www.google.com/'
#os.makedirs('folder', exist_ok=True)

res8 = requests.get('https://www.google.com/', verify=False)


def uncode(encoded_str):
    return urllib.parse.unquote(encoded_str)

value = input("enter product name (JUMIA SEARCH) : ")
value = value.replace(' ', '+')

res = requests.get('https://www.jumia.ma/catalog/?q', params={'q': value})
soup = bs4.BeautifulSoup(res.text, features='html.parser')

products = soup.select('article')

def is_product(p):
    if p.select('div .prc'):
        return True
    return False
products = list(filter(is_product, products))

def scrape_product(index:int):
    dic = dict()

    if products[index].select('div .old'):
        dic['old'] = products[index].select('div .old')[0].getText()
        dic['reduction'] = products[index].select('div.bdg._dsct._sm')[0].getText()
    # info
    if products[index].select('div.bdg._mall._xs'):
        dic['boutique'] = products[index].select('div.bdg._mall._xs')[0].getText()

    dic['new'] = products[index].select('div .prc')[0].getText()
    # image of products
    dic['image'] = products[index].select('.img')[0].get('data-src')
    dic['name'] = products[index].select('h3.name')[0].getText()

    return dic

def print_dict(dic:dict):
    print(f'PRODUCT : {dic["name"]}\n')
    for index, value in dic.items():
        print(f'{index}: {value}')
    print('\n')

for i in range(len(products)):
    print_dict(scrape_product(i))

print(len(products))