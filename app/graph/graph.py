import base64
from io import BytesIO
import matplotlib.pyplot as plt


#Top5Pages
def top5PagesGraph(top5Page):
    img = BytesIO() 
    left = ["Page 1","Page 2","Page 3","Page 4","Page 5"]
    height = top5Page.values()
    
    plt.xlabel('Pages')
    plt.ylabel('Nombre occurence')
    plt.title('Top 5 pages les plus visitées!')
    
    plt.bar(left, height, width = 0.8)
    plt.savefig(img, format='png') 
    plt.close() 
    img.seek(0) 
    return base64.b64encode(img.getvalue()).decode('utf8')

#5 search engines
def top5_se_graphes(top5_SE):
    img = BytesIO()
    left = ["Moteur 1","Moteur 2","Moteur 3","Moteur 4","Moteur 5"]
    height = top5_SE.values()

    plt.xlabel('Moteur de recherche')
    plt.ylabel('Nombre occurence')
    plt.title('Top 5 moteurs de recherche!')

    plt.bar(left, height, width = 0.8)

    plt.savefig(img, format='png') 
    plt.close() 
    img.seek(0) 
    return base64.b64encode(img.getvalue()).decode('utf8')


# Canaux de distributions les plus frequentés
def top10_canaux_graph(top10_FU):
    img = BytesIO()
    left = ["C 1","C 2","C 3","C 4","C 5", "C 6","C 7","C 8","C 9","C 10"]
    height = top10_FU.values()

    plt.xlabel('Canaux')
    plt.ylabel('Fréquence')
    plt.title('Top 10 canaux de distribution!')

    plt.bar(left, height, width = 0.8)

    plt.savefig(img, format='png') 
    plt.close() 
    img.seek(0) 
    return base64.b64encode(img.getvalue()).decode('utf8')