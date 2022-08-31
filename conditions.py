from datetime import datetime
import json
import re



  
def open_json(file):
  # Opening JSON file
  f = open(file)
  d = json.load(f)
  return d

class bcolors:
  
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def get_param_dic(key,value,list):
  params=[]
  for i in list:
    try: 
      if i['dialog_node']==value: ## encuentra el parent objetivo  
        params.append(i[key])
    except: None
      
  return params

### Llamar JSON
data = open_json('dialognodes.json')
list_json=data['dialog_nodes']
message = open_json('backtoconv.json')


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

def save_json(dic):
  
  with open("sample.json", "w") as outfile:
    json.dump(dic, outfile)




def find_transf_date(str):##### buscar fechas en context
  strtodate = datetime.now().date()
  prog = re.compile(r'([\d]{4})(-)([\d]{2})(-)([\d]{2})')
  found=prog.search(str)
  if True:
    try:
      strtodate= datetime.strptime(found.group(0), '%Y-%m-%d').date()
      
      return strtodate
    except: None
  else: 
    return str
    
context_values2=""

def transf_var_ctx(var,json_name): #### Transformación de variavles $ a py
  
  prog = re.compile(r'([$])([\w_]+)')
  found=prog.match(var)
  
  if found:
    py_var=json_name+"""['context'].get('"""+found[2]+"""')"""
    # str = "global context_values2; context_values2 = "+py_var
    # exec(str)
    
    
    
    # print(isinstance(find_transf_date(context_values2),datetime.date))
    
    # if isinstance(find_transf_date(context_values2),datetime.date) :
    #   p("^")
    #   json_name['context'][found[2]]=(find_transf_date(context_values2))
    #   print("*************",json_name['context'][found[2]])
    return py_var
  else: var



def get_all_var_ctx(condition): ##### Obtener listado de variables de contexto
  
  list_var_ctx=[]
  condition = condition.replace("&&","")
  condition = condition.replace("||","")
  list_var=re.split('=|!|<|>| ',condition)
  
  for r in list_var: ##s
    
    if r and r != "" and r != " ": 
      prog = re.compile(r'([$])([\w_]+)')
      found=prog.findall(r)
      
      try:
        for f in found: 
          var ="".join(f)
          list_var_ctx.append(var)
      except: None
      
  return unique(list_var_ctx)    



def change_all_vars_ctx(condition):
  
  try:
    
    for c in get_all_var_ctx(condition):
      
      transf_var_ctx(c,"message")
      condition=condition.replace(c,transf_var_ctx(c,"message"))
      
  except: None
  
  return condition



def get_plus_days (condition,json_name):##### Reemplazar función plusDays

  
  prog = re.compile(r'(\b.plusDays\b)([(])([\w$]+)([)])')
  found=prog.findall(condition)
  try:
    for f in found: 
      plus_day_old= "".join(f)
      plus_day_new= """ + timedelta(days= """ + f[2] +""" )"""
      condition=condition.replace(plus_day_old,plus_day_new)
  except: None
  return condition



def get_matches (condition,json_name):##### Reemplazar función .matches

  prog = re.compile(r"([\w_@$-.]+)(\b.matches\b)([(])([\w., ']+)([)])")
  found=prog.findall(condition)
  try:
    for f in found: 
      matches_old = "".join(f)
      matches_new = """re.search("""+f[3]+","+f[0]+")"
      condition=condition.replace(matches_old,matches_new)
  except: None
  return condition



def get_size (condition,json_name):##### Reemplazar función size()

  
  prog = re.compile(r'([\w_@$-]+)(\b.size\b)([()]+)')
  found=prog.findall(condition)
  try:
    for f in found: 
      size_old= "".join(f)
      size_new= """ len(""" + f[0] +""")"""
      condition=condition.replace(size_old,size_new)
  except: None
  return condition



def get_toint (condition,json_name):##### Reemplazar función toint()
  
  prog = re.compile(r'([\w_@$-.]+)(\b.toInt\b)([()]+)')
  found=prog.findall(condition)
  
  try:
    for f in found: 
      size_old= "".join(f)
      size_new= """ int(""" + f[0] +""")"""
      condition=condition.replace(size_old,size_new)
  except: None
  return condition



def get_func_transf(condition,json_name):   ##### transformar funciones de condicióm a formato python
  
  condition = condition.replace('today()',"datetime.today()")
  condition = condition.replace('toInt()'," and ")
  condition = condition.replace("input.text",(json_name+"['input']['text']"))
  return condition



def get_basic_transf(condition):  ##### transformar operadores básicos de condición a formato python
  
  condition = condition.replace('\"',"'")
  condition = condition.replace("&&"," and ")
  condition = condition.replace("||"," or ")
  condition = condition.replace("true"," True ")
  condition = condition.replace("false"," False ")
  condition = condition.replace("null"," None ")
  
  return condition



def get_conditions(dialog_node,json_name):

  try: 
    condition = get_param_dic('conditions',dialog_node,list_json)
    
    for c in condition:
      
      try: c = get_plus_days(c,json_name)
      except: None
      try: c = get_matches(c,json_name)
      except: None
      try: c = get_size(c,json_name)
      except: None
      try: c = get_toint(c,json_name)
      except: None
      try: c = get_func_transf(c,json_name)
      except: None
      try: c = get_basic_transf(c)
      except: None
      try: c = change_all_vars_ctx(c)
      except: None     
      return c
  except: None

