
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

def unique(list1):
  
    # initialize a null list
    unique_list = []
  
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
        else:
          continue
    # print list
    
    return(unique_list)

def buscar_detalle_nodo(dialog_node,list):
  for i in list:
    if i['dialog_node'] in dialog_node:
      pretty = json.dumps(i, indent=4,sort_keys=True)
      print(pretty)
      
  # print('\n')



def order(list1): ##[i['id_dialog_node'],i['id_sibling'],i['order']]
  output_list=list1
  counter=len(list1)
  id_operation_node=0
  num_order=0
  switch ="onm"
  for tuple in list1: ## sete id  operation node e inicia numero de order
  
    if tuple[2] == 1:    
      id_operation_node = tuple[0]
      num_order = 1
          
  
    for x in range(len(list1)):
      for v in list1:
        
        if v[1]==id_operation_node:
          v[2]=num_order+1
          num_order=v[2]
          id_operation_node=v[0]
  
  return output_list


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



data = open_json('dialognodes.json')
list_json=data['dialog_nodes']






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
    
    try: 
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




def get_uncle_next(get,list):
  for g in get:
    if g['n'] == 0:  
      padre =get_param_dic('parent',g['dialog_node'],list)[0]
      for x in range (20):
        for l in list:
          try:
            if padre==l['previous_sibling']:
              uncle_next= l['dialog_node']
              
          except: None
        padre=get_param_dic('parent',padre,list)
      print(g['dialog_node'],uncle_next)  
      # print(g['dialog_node'],padre,abuelo)


# ### Calcular lista completa de dependencias para todos los nodos
lista_final=[]









































# print (get_param_dic('parent','node_1_1590425903524',list_json)  )
# print(get_dependence('node_39_1614086021405',list_json))

'Preguntas Spot''node_10_1660445682847'
'RECURSIVAS   node_10_1660445728816 "_customization": {"mcr": true}'

'   Registra Respuesta pregunta recursiva        node_9_1660749730793'
'   pregunta spot siguiente true rspuesta 1      response_6_1660445769622'
'   sin pregunta spot siguiente, toAnswer null   response_8_1660445772146'









###############################Cementerio
###############################Cementerio
###############################Cementerio
###############################Cementerio
###############################Cementerio
#Convertir condición a formato python y hacer que las variables llamen al json context[""]








# i=0
# list_context=[]
# list_conditions=[]


# for l in list_json:


#   # try: 
#   #   for k,i in l['context'].items():
#   #     list_context.append(k)
#   #     print("'",i,"'")
#   # except: None

# # my_list = my_string.split(",")
  
#   try:   
    
#     # if "&&" in l['conditions'] and "||" in l['conditions']:
#     if True:
#       list_re=re.split('=|&| |>|<|!',l['conditions'])
#       list_re=unique(list_re)
      
  


      
#       for r in list_re:
#         list_context.append(r)
#         # if "$" in r and r != "" and r != " ": 
#         #   if "." not in r: 
#         #     continue
#         #     # print(re.sub(r'[()]', '', r))
#         #   else: 
#         #     continue
#         #     # print (r)
          
#         # else: print(r)

#     # l_new=l['conditions'].replace('||','or').replace('&&','and')
#     # list_conditions.append([l['dialog_node'],l_new])
#   except: None
# list_context =sorted(unique(list_context))
# for lc in list_context:
#   if lc != "" and lc != " ":
#     print(lc)  
  

# # for l in list_conditions:
# #   # if 'input.text' in l[1]:
# #     print(l[1])
# # correo_paciente=1

# # mycode = "if correo_paciente!=None: p(1)"
# # exec(mycode)



# list_context=unique(list_context)
# list_var_unique=[]
# for l in list_context:
#   for ll in list_conditions:
#     if l in ll and l not in list_var_unique:
#       list_var_unique.append(l)
#     else:
#       continue


# # print(list_var_unique,len(list_var_unique))

# list_conditions_clean =[]
# for l in list_var_unique:
  
#   for ll in list_conditions:
#     if l in ll:
      
#       lll=ll.replace(l,"")
#       # print(l,"\n",ll,"\n",lll,"\n","\n","\n")
#       list_conditions_clean.append(lll)
#     else:
#       continue

# # print(list_conditions_clean)
