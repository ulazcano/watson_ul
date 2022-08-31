import conditions as condition
import context as context
import mapping as mapping
import json

data = mapping.open_json('dialognodes.json')
list_json=data['dialog_nodes']


def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    
    request_json = request.get_json(force=True, silent=True, cache=True)
    dialog_node=request_json['context']["system"]["dialog_stack"][0]['dialog_node']
    print(dialog_node)
    join(dialog_node,list_json)
    
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'


def join(dialog_node,list):
    conditions = condition.get_conditions(dialog_node)
    dependence = mapping.get_dependence(dialog_node,list)
    print(conditions,"\n",dependence)




