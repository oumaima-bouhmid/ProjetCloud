import json
import os
from flask import Flask, render_template, request
import werkzeug
from graph.graph import top10_canaux_graph, top5_se_graphes, top5PagesGraph
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

fichier = ''
UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#page d'accueil
@app.route("/")
def index():
  return render_template("index.html")

#page des conditions générales
@app.route("/conditions")
def conditionGenerales():
  return render_template("conditions.html")

#page d'analyse
@app.route("/analyse", methods=['GET', 'POST'])
def analyse():
  if request.method == 'POST':
    f = request.files['file']
    if f.filename != '':
      global fichier
      fichier = f.filename
      fichierLog = werkzeug.utils.secure_filename(f.filename)
      fichier = os.path.join(app.config['UPLOAD_FOLDER'], fichierLog)
      f.save(fichier)
      df = open(fichier, "r")
      fichierLogPostStat = session.post("http://statistiques:5000/analyse", files={'file' : df})
      return render_template("analyse.html")


#page des suggestions
@app.route("/suggestion")
def suggestion():
  association = requests.get("http://suggestions:8085/association")
  association = association.json()
  repAssociation = json.dumps(association, ensure_ascii=False, indent=4)
  repAssociationDict = json.loads(repAssociation)

  return render_template("suggestion.html", association = repAssociationDict)


#page des statistiques
@app.route("/statistique")
def statistique():
  #nombre total
  nbTotal = requests.get("http://statistiques:5000/nombreTotalIp").json()

  #nombre par consultation
  nbConsultationIp = requests.get("http://statistiques:5000/consultationIp")
  nbConsultationIp = nbConsultationIp.json()
  repnbConsultation = json.dumps(nbConsultationIp, ensure_ascii=False, indent=4)
  nbConsultationIpDict = json.loads(repnbConsultation)

  #code status
  codeStatus = requests.get("http://statistiques:5000/codeStatus")
  codeStatus = codeStatus.json()
  repCodeStatus = json.dumps(codeStatus, ensure_ascii=False, indent=4)
  repCodeStatusDict = json.loads(repCodeStatus)
  
  #top 5 pages
  top5PageDict = requests.get("http://statistiques:5000/top5PageDict")
  top5PageDict = top5PageDict.json()
  reptop5Page = json.dumps(top5PageDict, ensure_ascii=False, indent=4)
  reptop5PageDict = json.loads(reptop5Page)
  top5PageGraph = requests.get("http://statistiques:5000/top5PageGraph")
  top5PageGraph = top5PageGraph.json()
  reptop5PageGraph = json.dumps(top5PageGraph, ensure_ascii=False, indent=4)
  top5PageGraph = json.loads(reptop5PageGraph)
  top5Page = top5PagesGraph(top5PageGraph)

  #search engines
  top5SeDict = requests.get("http://statistiques:5000/top5SeDict")
  top5SeDict = top5SeDict.json()
  repTop5Se = json.dumps(top5SeDict, ensure_ascii=False, indent=4)
  repTop5SeDict = json.loads(repTop5Se)
  Top5SeGraph = requests.get("http://statistiques:5000/top5SeGraph")
  Top5SeGraph = Top5SeGraph.json()
  repTop5SeGraph = json.dumps(Top5SeGraph, ensure_ascii=False, indent=4)
  Top5SeGraph = json.loads(repTop5SeGraph)
  top5Se = top5_se_graphes(Top5SeGraph)

  #canaux de distributions
  top10CanneaxDict = requests.get("http://statistiques:5000/top10CanneaxDict")
  top10CanneaxDict = top10CanneaxDict.json()
  reptop10Canneax = json.dumps(top10CanneaxDict, ensure_ascii=False, indent=4)
  reptop10CanneaxDict = json.loads(reptop10Canneax)
  top10CanneaxGraph = requests.get("http://statistiques:5000/top10CanneaxGraph")
  top10CanneaxGraph = top10CanneaxGraph.json()
  reptop10CanneaxGraph = json.dumps(top10CanneaxGraph, ensure_ascii=False, indent=4)
  top10CanneaxGraph = json.loads(reptop10CanneaxGraph)
  top10_canaux = top10_canaux_graph(top10CanneaxGraph)

  return render_template("statistique.html", nbTotal = nbTotal, nbConsultationIp = nbConsultationIpDict, codeStatus = repCodeStatusDict, top5Page = top5Page, top5PageDict = reptop5PageDict, top5Se = top5Se, top5SeDict = repTop5SeDict, top10_canaux = top10_canaux, top10CanneaxDict = reptop10CanneaxDict)


#page du map
@app.route("/map")
def map():
  return render_template("map.html")


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
