import json


def obj2dict(obj):
    return obj.__dict__
def addDef2File(FILE,user,arg,defn):
    with open(FILE, encoding='utf-8') as feedsjson:
        feeds=json.load(feedsjson)

    with open(FILE, mode='w', encoding='utf-8') as feedsjson:
        entry={'Nume':user,'Arg':str(arg),'Def':defn}
        feeds.append(entry)
        json.dump(feeds, feedsjson)
def checkDef(FILE,arg):
    with open(FILE,mode='r',encoding='utf-8') as f:
        dd=json.load(f)
    if not any(c.get('Arg',None)==arg for c in dd):
        return True
    else: return False
def printDef(FILE,arg):
    with open(FILE,encoding='utf-8') as f:
        dd=json.load(f)
    for elem in dd:
        if elem['Arg']==arg:
            return elem['Arg']+": "+elem['Def']
def printAlreadyDef(FILE,arg):
    with open(FILE,encoding='utf-8') as f:
        dd=json.load(f)
    for elem in dd:
        if elem['Arg']==arg:
            return "Acest cuvant: "+elem['Arg']+" , este deja definit."#sau.
