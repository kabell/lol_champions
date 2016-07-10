# -*- coding: utf-8 -*-
from django.shortcuts import render
import os,re,random,jsonpickle
from django.http import HttpResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = BASE_DIR+'/lol_champions/data'

class Champion:

    def __init__(self,name):
        self.name = name
        self.mp3 = name+'.mp3'
        self.jpg = name+'.jpg'


def index(request,tah=None):
    sprava = ""
    spravne = request.session.get('spravne',0)
    nespravne = request.session.get('nespravne',0)

    if tah:
        champion = request.session['champion']
        if tah == champion:
            sprava = "Spravne"
            spravne+=1
        else:
            sprava = "Nespravne - mal to byť "+champion
            nespravne+=1
    request.session['spravne'] = spravne
    request.session['nespravne'] = nespravne

    champions = []
    with open('lol_champions/champions.txt') as f:
        lines = f.readlines()
        for c in lines:
            champions.append(Champion(c.rstrip('\n')))

    championpos = random.randint(0,len(champions)-1)
    champion = champions[championpos]

    request.session['champion'] = champion.name

    return render(request, 'lol.html', locals())

def reset(request):
    del request.session['spravne']
    del request.session['nespravne']
    return index(request)




