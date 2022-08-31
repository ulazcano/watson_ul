import json



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

def open_json(file):
  # Opening JSON file
  f = open(file)
  d = json.load(f)
  return d

def save_json(dic,name_json):
  
  with open(name_json, "w") as outfile:
    json.dump(dic, outfile)
    

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

