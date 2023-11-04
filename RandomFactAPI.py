from typing import Union
from fastapi import FastAPI
import json
import random
app = FastAPI()

#import json file
with open('facts/facts.json') as f: #Relatively small file with 2000 ish entries loading it into memory is faster and less work than transposing into a DB
    facts = json.load(f)

facts = facts['facts']



@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/fact')
def getFact():
    random_index = random.randrange(0,len(facts))
    #print(random_index)
    return {'fact': facts[random_index]['text'],'source':facts[random_index]['source']}
