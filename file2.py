# file megnyitása írásra egy file típusú változóban
# ha még nincs demo.txt nevű fájl, akkor létrehozza
from encodings import utf_8


file1 = open("demo.txt", "w")
file1.write("Now the file has more content!"+"\n")
file1.write("...next line"+"\n")

# ellenőrző kiiratás, megnyitom olvasásra
file1 = open("demo.txt", "r")
print(file1.read())

# használat után a fájlt illik bezárni
file1.close()

# FELADAT: golok.txt számait írjuk át a golok2.txt-be
# létrehozom az egyik fájlt olvasásra, a másikat írásra
file2 = open("golok.txt", "r")
file3 = open("golok2.txt", "w")
#beolvasom az első sort, és megy a kukába
file2.readline()
#for ciklussal bejárom az olvasásra megnyitott fájlt
for sor in file2: 
    # az olvasásra megnyitott fájlnak minden sorát hozzáfűzöm az írásra megnyitott fájlhoz
    file3.write(sor)
# lezárom a fájlokat    
file2.close() 
file3.close()  
 
# FELADAT: golok.txt-ből a páros számokat írjuk át a golok3.txt-be 
# létrehozom az egyik fájlt olvasásra, a másikat írásra   
file4 = open("golok.txt", "r")
file5 = open("golok3.txt", "w")
#beolvasom az első sort, és megy a kukába
file4.readline()
#for ciklussal bejárom az olvasásra megnyitott fájlt
for sor in file4: 
    # a beolvasott sort (ami 1 db szám) integerré konvertálom
    # és megnézem, hogy páros-e és nem nulla
    if(int(sor) % 2 == 0 and int(sor) != 0):
        # ha a szám páros és nem nulla, akkor hozzáadom az írandó fájlhoz
        file5.write(sor)
# lezárom a fájlokat
file4.close() 
file5.close()   

# FELADAT: 
# Kérj be a felhasználótól egy mondatot, 
# majd hozz létre a programban egy fájlt mondat.txt néven, 
# ami ezt a mondatot tartalmazza (egy sorban). 
# A fájlból kiolvasva a mondatot, 
# írd ki minden második szavát a képernyőre. Szónak tekintjük a szóközök között levő karaktersorozatot.
# Szorgalmi: ne csak a képernyőre írd ki, hanem az eredmeny.txt fájlba is.

# bekérem a mondatot
megadottMondat = input("Adj meg egy tetszőleges mondatot: ")
# megnyitom a fájl írásra, és beleteszem a megadott mondatot, majd lezárom a fájlt
file6 = open("mondat.txt", "w")
file6.write(megadottMondat)
file6.close()
# megnyitom ugyanazt a fájl olvasásra
file6 = open("mondat.txt", "r")
# kiolvasom belőle az első sort (nincs is több)
kiolvasottMondat = file6.readline().strip()
# feldarabolom szóközök mentén a kiolvasott mondatot
szavakListaja= kiolvasottMondat.split(" ")
# megnyitok egy új fájlt írásra
file7 = open("eredmeny.txt","w", encoding="utf_8")

# for ciklussal bejárom a LISTÁT
for i in range(len(szavakListaja)):
    # ha minden második elemt kell kiiratnom, akkor a páratlan indexű elemek kellenek
    if i % 2 != 0:
        print(szavakListaja[i])
        file7.write(szavakListaja[i] +  " ")

# lezárok minden fájlt
file6.close()
file7.close()

    