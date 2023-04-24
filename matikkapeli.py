import random
import time

oikeita = 0
vaaria = 0
kayttajan_vastaukset = []
oikeat_vastaukset = []
kysymykset = []
list = []

print('Moi Elsi! Tervetuloa opettelemaan kertolaskuja.')

kerrottava = input('Valitse mitä kertotauluja haluat harjoitella. (Valitse haluamasi kertotaulu tai paina enteriä jos haluat että kaikkia kysytään)\n')
if (kerrottava == ''):
  print('Okei, haluat siis että kaikkia kysytään!')
  list = [2,3,4,5,10]
else:
  print('Ok, kysytään siis '+ kerrottava + ':n kertotauluja.')
  list = [int(kerrottava)]

kysymysten_lkm = input('Kuinka monta kysymystä haluat? (valitse 10, 20 tai 30)\n')
if (kysymysten_lkm == ''):
  print("Koska jätit kentän tyhjäksi, saat 40 kysymystä!")
  kysymysten_lkm = "40"
else:
  print('Selvä, kysytään '+kysymysten_lkm+ ' kysymystä. Aloitetaan!\n')



start = time.time()
for i in range(1,int(kysymysten_lkm)+1):
  kerrottava = random.choice(list)
  kertoja = random.randint(1, 10)
  print(str(i) + '. kysymys:')
  vastaus = input("Paljonko on % s·% s?\n" % (kertoja, kerrottava))
  while (vastaus == ''):
    print("Painoit enteriä kerran liikaa. Anna vastaus numeroina.")
    vastaus = input("Paljonko on % s·% s?\n" % (kertoja, kerrottava))
  if (vastaus == 'q'):
    print("Heippa Elsi!")
    quit()
  else:
    kayttajan_vastaukset.append(vastaus)
    oikeat_vastaukset.append(kertoja * int(kerrottava))
    kysymykset.append("% s·% s\n" % (kertoja, kerrottava))
    huraa = random.choice(['Jee!', 'Upeeta, mahtavaa!', 'Jihuu!', 'Jiihaa!', 'tuhat pistettä!'])
    voivotus = random.choice(['Voih!', 'Aijjaijai!', 'Himpura!', 'Tuhannen tulimmaista!', 'Eih!'])
    if (int(vastaus) == kertoja*int(kerrottava)):
      print('Oikea vastaus. '+huraa)
      oikeita= oikeita+1
    else:
      print('Väärä vastaus. '+voivotus)
      vaaria = vaaria+1
  end = time.time()
print()
print('Tässä vastauksesi:')
for i in range(0, len(kysymykset)):
  oikein_vai_vaarin = ''
  if (int(kayttajan_vastaukset[i]) == oikeat_vastaukset[i]):
    oikein_vai_vaarin = 'oikein'
  else:
    oikein_vai_vaarin = 'väärin'
  print(str(i+1)+'. kysymys: '+ str(kysymykset[i]) + 'Vastauksesi oli '+ str(kayttajan_vastaukset[i])+' ja se on '+oikein_vai_vaarin+'\n')
print('Oikeita vastauksia '+str(oikeita)+'kpl')
print('Vääriä vastauksia '+str(vaaria)+'kpl')
print('vastaamisessa kesti yhteensä noin ' + str(end-start) + ' sekuntia.')
if (oikeita>vaaria):
  print('Hyvä Elsi!')
else:
  print('Voi voi voi. Taisi tulla muutama huolimattomuusvirhe.')
