import json
import csv
from operator import itemgetter
import re


def p(a):
  print(a)
  
def open_json(file):
  # Opening JSON file
  f = open(file)
  d = json.load(f)
  return d


def buscar_detalle_nodo(dialog_node,list):
  for i in list:
    if i['dialog_node'] in dialog_node:
      pretty = json.dumps(i, indent=4,sort_keys=True)
      print(pretty)
  print('\n')


def buscar_detalle_title(title,list):
  for i in list:
    try:
      if i['title'] == title:
        pretty = json.dumps(i, indent=4,sort_keys=True)
        print(pretty)
    except: None
  print('\n')



def get_param_dic(key,value,list):
  params=[]
  for i in list:
    try: 
      if i['dialog_node']==value: ## encuentra el parent objetivo  
        params.append(i[key])
    except: None
      
  return params


def save_json(dic):
  
  with open("sample.json", "w") as outfile:
    json.dump(dic, outfile)




dict_simple={}## inicia lista de simplificación del json
list_simple=[]
data = open_json('dialognodes.json')
list_json=data['dialog_nodes']

