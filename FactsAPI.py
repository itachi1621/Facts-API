from fastapi import FastAPI
import json
import random
from starlette.responses import RedirectResponse
app = FastAPI()

version = "1.0.3"
base_url = '/api/v1'

#import json file
with open('facts/intresting_facts.json') as f: #Relatively small file with 2000 ish entries loading it into memory is faster and less work than transposing into a DB
    ifacts = json.load(f)

ifacts = ifacts['facts']
ifacts_size = len(ifacts)


with open('facts/useless_facts.json') as f: #Relatively small file with 2000 ish entries loading it into memory is faster and less work than transposing into a DB0
    ufacts = json.load(f)

ufacts = ufacts['facts']
ufacts_size = len(ufacts)


@app.get('/')
def read_root():
    # redirect to /docs url
    return RedirectResponse(url='/docs')

@app.get('/version')
def getVersion():
    return {
        'version': version
        }

@app.get(base_url+'/useless/fact')
def getUFact(fid:str | None = None ):
    try:

        if fid == None:
            fid = ""

        if fid.isdigit():
            fid = int(fid)
            if fid <= 0 or fid > ufacts_size - 1 :
                return {
                    'error': 'Fact ID out of range',
                }
            else:
                return {
                    'id':fid,
                    'fact': ufacts[fid]['text'],
                    'source':ufacts[fid]['source']
                }
        elif fid.isdigit() == False and fid != "":
            return {
                'error': 'Fact ID must be a number',
            }
        elif fid == "":
                        #check for query string fid
            random_index = random.randrange(0,ufacts_size - 1)
            return {
                    'id':random_index,
                    'fact': ufacts[random_index]['text'],
                    'source':ufacts[random_index]['source']
                    }
        else:
            return {
                'error': 'Unable to process request',
            }

    except Exception as e:
        print(e)
        return {
            'error': 'Unable to process request',
            }


@app.get(base_url+'/intresting/fact')
def getIFact(fid:str | None = None):
    try:
        if fid == None:
            fid = ""
        if fid.isdigit():
            fid = int(fid)
            if fid <= 0 or fid > ifacts_size - 1 :
                return {
                    'error': 'Fact ID out of range',
                }
            else:
                return {
                    'id':fid,
                    'fact': ifacts[fid],
                    'source':"N/A"
                }
        elif fid.isdigit() == False and fid != "":
            return {
                'error': 'Fact ID must be a number',
            }
        elif fid == "":
            random_index = random.randrange(0,ifacts_size - 1)
            return {
                    'id':random_index,
                    'fact': ifacts[random_index],
                    'source':"N/A"
                    }
        else:
            return {
                'error': 'Unable to process request',
            }

    except Exception as e:
        print(e)
        return {
            'error': 'Unable to process request',
            }
