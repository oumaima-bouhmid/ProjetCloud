import os
from flask import Flask, request
import werkzeug
from analyse.analyseLogFunctions import all_canaux, all_code_status, all_search_engines, logToDf, nb_apparence_pages, nb_consultation_ip, nbTotalIp, reduction_ip, sort_all_canaux, sort_all_code_status, sort_all_search_engines, sort_nb_apparence_pages, sort_reduction_ip, top10_canaux, top5_codestatus, convertToDict, top5_pages, top5_se
from analyse.toDict import top10CanauxDict, top5PagesDict, top5SeDict
import requests

fichier = ''
UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/analyse', methods = ['POST'])
def analyse():
  f = request.files['file']
  if f.filename != '':
    global fichier
    fichier = f.filename
    fichierLog = werkzeug.utils.secure_filename(f.filename)
    fichier = os.path.join(app.config['UPLOAD_FOLDER'], fichierLog)
    f.save(fichier)
    df = open(fichier, "r")
    fichierLogPostSug = requests.post("http://suggestions:8085/suggestion", files={'file' : df})
    return fichier


@app.route("/nombreTotalIp", methods = ['GET'])
def nombreTotalIp():
  df = logToDf("./"+fichier)
  return str(nbTotalIp(df))


@app.route('/consultationIp', methods=['GET'])
def nombreConsultation():
  df = logToDf("./"+fichier)
  nbConsultationIp = sort_reduction_ip(reduction_ip(nb_consultation_ip(df)))
  return nbConsultationIp


@app.route('/codeStatus', methods=['GET'])
def codeStatus():
  df = logToDf("./"+fichier)
  codeStatus = top5_codestatus(sort_all_code_status(all_code_status(df)))
  return codeStatus

@app.route('/top5PageGraph', methods=['GET'])
def topPagesGraph():
  df = logToDf("./"+fichier)
  top5Page = top5_pages(sort_nb_apparence_pages(nb_apparence_pages(df)))
  return top5Page

@app.route('/top5PageDict', methods=['GET'])
def topPagesDict():
  df = logToDf("./"+fichier)
  top5Page = top5_pages(sort_nb_apparence_pages(nb_apparence_pages(df)))
  pagesDict = top5PagesDict(top5Page)
  return pagesDict

@app.route('/top5SeGraph', methods=['GET'])
def searchEngineGraph():
  df = logToDf("./"+fichier)
  top5_SE = top5_se(sort_all_search_engines(all_search_engines(df)))    
  return top5_SE

@app.route('/top5SeDict', methods=['GET'])
def searchEngineDict():
  df = logToDf("./"+fichier)
  top5_SE = top5_se(sort_all_search_engines(all_search_engines(df)))    
  dict5Se = top5SeDict(top5_SE)
  return dict5Se

@app.route('/top10CanneaxGraph', methods=['GET'])
def top10CanneaxGraph():
  df = logToDf("./"+fichier)
  top10_FU = top10_canaux(sort_all_canaux(all_canaux(df)))   
  return top10_FU

@app.route('/top10CanneaxDict', methods=['GET'])
def top10CanneaxDict():
  df = logToDf("./"+fichier)
  top10_FU = top10_canaux(sort_all_canaux(all_canaux(df)))   
  dictTop10Canaux = top10CanauxDict(top10_FU)
  return dictTop10Canaux


@app.route('/hello', methods=['GET'])
def association():
  return "hello"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
