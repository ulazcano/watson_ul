
import json
import csv
from operator import itemgetter
import re
from tools import tool

data = tool.open_json('dialognodes.json')
list_json=data['dialog_nodes']



def p(a):
  print(a)
  
def buscar_detalle_nodo(dialog_node,list):
  for i in list:
    if i['dialog_node'] in dialog_node:
      pretty = json.dumps(i, indent=4,sort_keys=True)
      print(pretty)
      
def get_param_dic(key,value,list): 
  params=[]
  for i in list:
    try: 
      if i['dialog_node']==value: ## encuentra el parent objetivo  
        params.append(i[key])
    except: None
      
  return params



def get_dependence(dialog_node,list):
  list_previous=[]
  list_previous_mcr=[]
  list_previous_jump_to=[]
  list_child=[]
  list_next_sibling=[]
  list_last_option=[]
  list_1=[]
  end_flow=False
  uncle_next=""
  
  type_dialog_node = get_param_dic('type',dialog_node,list)[0]
  
  i=0
  for l in list:
    try: #Calcula mcr
      if l['type']=='response_condition' and l['parent']==dialog_node : list_previous_mcr.append(l['dialog_node'])
    except: None
    
    try: #Calcula jump to
      if l['next_step']['behavior']=='jump_to' and l['dialog_node']==dialog_node: list_previous_jump_to.append(l['next_step']['dialog_node'])
    except: None
    
    try: #Calcula child
      
      if l['type']=='standard' and l['parent']==dialog_node and l.get('previous_sibling') is None : list_child.append(l['dialog_node'])
    
    except: None
      
    try: #Calcula next sibling
      if type_dialog_node == "standard" and l['type']=='standard' and l['previous_sibling']==dialog_node: list_next_sibling.append(l['dialog_node'])
    except: None
    
    try: #Calcula next sibling
      if type_dialog_node == "response_condition" and l['type']=='standard' and l['previous_sibling']==dialog_node: list_next_sibling.append(l['dialog_node'])
    except: None
  
  
  n = len(list_previous_mcr)+len(list_previous_jump_to)+len(list_child)+len(list_next_sibling)+len(list_last_option)
    
  if n==0:
    
    try: #Calcula last option
      parent=get_param_dic('parent',dialog_node,list)[0]
      for x in range (20):
        
        for l in list:
          try:
            if parent==l['previous_sibling']:
              uncle_next= l['dialog_node']
              n=1
              break
            
          except: None
        if uncle_next != "": break
        else: 
          try: parent=get_param_dic('parent',parent,list)[0]
          except:end_flow=True
    except:end_flow=True


  dic_next_step = dict(
  n= n,
  dialog_node = dialog_node,
  mcr = list_previous_mcr,
  jump_to = list_previous_jump_to,
  child = list_child,
  next_sibling = list_next_sibling,
  last_option =uncle_next,
  end_flow=end_flow
  )
  return dic_next_step




for l in list_json:
  p(get_dependence(l,list_json))

