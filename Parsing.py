import requests
import re

def geturl(adress):
    urls = {
             'http://statsoft.ru/' + t[7:len(t) - 1]
             for t in re.findall('href="/.+[/]+["]+', requests.get(adress[0]).text)
                 
            }
    return(urls)
adress=['http://statsoft.ru/']
urls = geturl(adress)
urls=list(urls)
emails = {
             t
             for j in range(len(urls))
             for t in re.findall('[\w.]*[\-]*[\w.]+@\w+\.\w+[\.]*[\w+]*', requests.get(urls[j]).text)
            }
print('\n'.join(emails))
