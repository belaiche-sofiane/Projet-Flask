#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys, os, json, requests

reponse = requests.get("http://localhost:5000/recherche/"+sys.argv[1])
lignes = reponse.json()
os.system("curl localhost:5000/recherche/"+sys.argv[1]+" > resultat")
fd = open("resultat")
reponses = json.loads(fd.readline())

for reponse in reponses :
    print("reference du livre:",reponse[0])
    print("titre du livre: ",reponse[1])
    print("sous-tire du livre: ",reponse[2])
    print("Auteurs du livre: ", reponse[3])
    print("Edition du livre: ", reponse[4])
    print("Date d'edition du livre: ", reponse[5])
    print("preface du livre: ", reponse[24])
    print("Resume du livre: ", reponse[25])
    print("ISBN du livre: ", reponse[31])

    print("---------------------------------")