import os
from flask import Flask, request
import werkzeug
from suggestion.associationRules import association_rules_log, convertToDict, dfToDataset, filtering_associations, frequent_itemsets, logToDf, transform_datasetTodf

fichier = ''
UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/suggestion', methods = ['POST'])
def suggestion():
  f = request.files['file']
  if f.filename != '':
    global fichier
    fichier = f.filename
    fichierLog = werkzeug.utils.secure_filename(f.filename)
    fichier = os.path.join(app.config['UPLOAD_FOLDER'], fichierLog)
    f.save(fichier)
    return fichier

@app.route('/association', methods=['GET'])
def association():
  df = logToDf("./"+fichier)
  association = filtering_associations(association_rules_log(frequent_itemsets(transform_datasetTodf(dfToDataset(df))))) 
  dictAssociation = convertToDict(association)
  return dictAssociation



if __name__ == "__main__":
  from waitress import serve
  serve(app, host="0.0.0.0", port=8085)