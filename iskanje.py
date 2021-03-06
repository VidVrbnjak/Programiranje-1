import requests
import csv
import json
import os
import re
import sys
import pandas


vzorec = re.compile(
    r'<a class="Adlink" href="[^<]*<span>(?P<znamka>.+?)</span>.*?'
    r'<li>Letnik 1.registracije:(?P<letnik>\d+)</li>.*?'
    r'<li>(?P<prevozenih>\d+) km</li>.*?'
    r'<li>(?P<tip_motorja>.+?),.*?'
    r', (?P<moc_motorja>\d+) kW.*?'
    r'<li>(?P<menjalnik>.+?)</li>.*?'
#   r'<!-* REDNA OBJAVA CENE -*>\n\n\t*(?P<cena>.+?) ',
    r'<div class="ResultsAdPriceRegular">*(?P<cena>.+?) ',
    re.DOTALL
)




def get_data(data):
    oglas = data.groupdict()
    a = data['znamka'].split(' ', 2)
    if a[0] in ('Land', 'Alfa', 'Range'):
        oglas['znamka'] = a[0] + ' ' + a[1]
    else:
        oglas['znamka'] = a[0]
    oglas['letnik'] = int(data['letnik'])
    oglas['prevozenih'] = int(data['prevozenih'])
    oglas['tip_motorja'] = data['tip_motorja']
    oglas['moc_motorja'] = int(data['moc_motorja'])
    oglas['menjalnik'] = data['menjalnik']
    try:
        oglas['cena'] = float(data['cena'])
    except:
        oglas['cena'] = None
    return oglas


def shrani_stran(url, filename):
    try:
        print('shranjujem... {}'.format(url))
        sys.stdout.flush()

        if( os.path.isfile(filename)):
            print('datoteka ze obstaja!')
            return

        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Napaka pri nalaganju strani (stran ne obstaja)!')
    else:
        dat = os.path.dirname(filename)
        if dat:
            os.makedirs(dat, exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as datoteka:
            datoteka.write(response.text)
            print('shranjeno!')




def to_csv(data, fieldnames, filename):
    datoteka = os.path.dirname(filename)
    if datoteka:
        os.makedirs(datoteka, exist_ok=True)

    with open(filename, 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for podatek in data:
            writer.writerow(podatek)




podatki_oglasov = []

for i in range(1, 15):
    url = (
    'https://www.avto.net/Ads/results.asp?znamka=&model=&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=&cenaMin=100&cenaMax=999999&letnikMin=0&letnikMax=2090&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=&mocMax=&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&EToznaka=0&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1000100020&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&zaloga=10&arhiv=0&presort=2&tipsort=DESC&stran={}'
    ).format(i)
    shrani_stran(url, 'avtonet{}.html'.format(i))
print('koncano prejemanje!')



for i in range(1, 15):
    with open('avtonet{}.html'.format(i), encoding='utf-8') as datoteka:
        vsebina = datoteka.read()

    for ujemanje in vzorec.finditer(vsebina):
        podatki_oglasov.append(get_data(ujemanje))

to_csv(podatki_oglasov, ['znamka', 'letnik', 'prevozenih', 'tip_motorja', 'moc_motorja', 'menjalnik', 'cena'], 'koncani_podatki.csv')
print('Podatki uspesno zapisani v datoteko!')