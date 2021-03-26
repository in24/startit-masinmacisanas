import requests

URL = 'https://www.ss.lv/lv/transport/cars/today-5/sell'
LAPAS = 'lapas/'

rezultats = requests.get(URL)
print(rezultats.status_code)
print(rezultats.text)

def saglaba(url,datne):
    rezultats = requests.get(url)
    if rezultats.status_code==200:
        with open(datne,'w',encoding='UTF-8')as f:
            f.write(rezultats.text)

# saglaba(URL,LAPAS+"pirma_lapa.html")