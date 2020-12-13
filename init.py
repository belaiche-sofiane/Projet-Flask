#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/references")#donne tous les livres présents dans la base de données, choix  de quelques informations sur les livres uniquement
def references():
    # print("/references")
    references = []
    file = open('livres.csv', 'r')
    reader = csv.reader(file)
    for row in reader:
        references.append(row)
    livres = json.dumps(references)
    liste = json.loads(livres)
    resultats=""
    i=0
    for elem in liste:
        resultats=resultats+"<ul class='references'><p><strong><u>livre "+str(i)+"</u></strong>"
        resultats=resultats+"</br><li><strong>reference du livre: </strong>"+elem[0]+"</li>"
        resultats=resultats+"</br><li><strong>Titre du livre: </strong>"+elem[1]+"</li>"
        resultats=resultats+"</br><li><strong>Sous-titre du livre: </strong>"+elem[2]+"</li>"
        resultats=resultats+"</br><li><strong>Auteurs du livre: </strong>"+elem[3]+"</li>"
        resultats=resultats+"</br><li><strong>Edition du livre: </strong>"+elem[4]+"</li>"
        resultats=resultats+"</br><li><strong>Date d'edition du livre: </strong>"+elem[5]+"</li>"
        resultats=resultats+"</br><li><strong>Preface du livre: </strong>"+elem[24]+"</li>"
        resultats=resultats+"</br><li><strong>Resume du livre: </strong></br><p stytle='text-justify: auto;'>"+elem[25]+"</p></li>"
        resultats=resultats+"</br><li><strong>ISBN du livre: </strong>"+elem[31]+"</li></ul>"
        i=i+1
    txt = open("templates/data.html", "w")
    txt.write(resultats)
    path= request.path
    return render_template('references.html', titre=path)
    


@app.route("/Informatique")#renvoie une page html traitant des généralites sur l'informatique
def informatique():
    path = request.path
    return render_template('informatique.html', titre=path)


@app.route("/recherche/<critere>")#methode de recherche avec critere
def recherche_critere(critere):

    print("/recherche/"+critere)
    lignes = []
    file = open('livres.csv', 'r')
    reader = csv.reader(file)
    for row in reader:
        if critere in row:
            lignes.append(row)
    return json.dumps(lignes)


@app.errorhandler(404)
@app.errorhandler(401)
@app.errorhandler(500)
def error(error):
    return "erreur {}".format(error.code), error.code
# mieux specifier les erreurs.


if __name__ == "__main__":
    app.run(debug=True) #permet de demarer en mode debugage
