from jinja2 import Template
import json

def handle(req):
    input = json.loads(req) 


    t = Template("User {{id}} registered")
    res = t.render(id=input["userId"])
    return res 
