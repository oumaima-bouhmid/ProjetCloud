
#fct qui retourne dictionnaire qui contient les valuer des pages a:.. b:..
def top5PagesDict(top5Page):
    liste5page = []
    for key,value in top5Page.items():
        liste5page.append(key)
    pageDict = dict()
    liste = ["Page 1","Page 2","Page 3","Page 4","Page 5"]    
    for i in range(0,5):
        pageDict[liste[i]] = liste5page[i]
    return pageDict

#fct qui retourne dictionnaire qui contient les valuer des SE
def top5SeDict(top5_SE):
    liste5Se = []
    for key,value in top5_SE.items():
        liste5Se.append(key)
    seDict = dict()
    liste = ["Moteur 1","Moteur 2","Moteur 3","Moteur 4","Moteur 5"]    
    for i in range(0,5):
        seDict[liste[i]] = liste5Se[i]
    return seDict

#fct qui retourne dictionnaire qui contient les valuer des canaux
def top10CanauxDict(top10_FU):
    liste10Canaux = []
    for key,value in top10_FU.items():
        liste10Canaux.append(key)
    canauxDict = dict()
    liste = ["C 1","C 2","C 3","C 4","C 5", "C 6","C 7","C 8","C 9","C 10"]    
    for i in range(0,10):
        canauxDict[liste[i]] = liste10Canaux[i]
    return canauxDict
