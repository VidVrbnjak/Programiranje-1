# Programiranje-1
Najdražji rabljeni avtomobili
=======================

Analiziral bom prvih 600 rabljenih avtomobilov filtrirani padajoče po ceni na spletni strani
[Avto.net](https://www.avto.net/Ads/results.asp?znamka=&model=&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=&cenaMin=100&cenaMax=999999&letnikMin=0&letnikMax=2090&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=&mocMax=&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1000100020&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&zaloga=10&arhiv=0&presort=3&tipsort=DESC&stran=1&subSORT=2&subTIPSORT=DESC).

Za vsak avto bom zajel:
* znamko
* letnik
* prevožene kilometre
* tip motorja
* moč motorja
* vrsta menjalnika 
* cena

Delovne hipoteze:
* Ali obstaja povezava med ceno in močjo avtomobila?
* Katera znamka ima najdražje avtomobile?
* Ali lahko iz letnika avtomobila napovemo število prevoženih kilometrov?
* Kolikšen je delež električnih avtomobilov 

Analiza podatkov:
* Po analizi podatkov opazimo, da ni nobene direktne povezave med močjo motorja in ceno avtomobila, edino
odstopanje so avtomibli ki imajo več kot 413HP, ti imajo občutno višjo ceno.
* Znamke razporejene padajoče glede na njihovo povprečno ceno so: <br> Rolls-Royce, Lamborghini, McLaren, Ferrari, Porsche,
 Land Rover, Audi, Mercedes-Benz, BMW, Maserati, Tesla in Ford. <br> 
 Pri tem imajo Rolls-Roycei in Lamborghiniji povprečno ceno
 vsaj enkrat vecjo od preostalih znamk, preostale znamke pa so v istem cenovnem razredu.
* Starejši avtomobili imajo povprečno več prevoženih kilometrov, kot bi pričakovali, z izjemo letnikov 2010, za katere
