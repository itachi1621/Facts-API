from fastapi import FastAPI
import json
import random
app = FastAPI()

version = "1.0.2"
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
    return {'Hello': 'World'}

@app.get(base_url+'/useless/fact')
def getUFact():
    try:

        random_index = random.randrange(0,ufacts_size - 1)
        return {
                'id':random_index,
                'fact': ufacts[random_index]['text'],
                'source':ufacts[random_index]['source']
                }

    except Exception as e:
        print(e)
        return {
            'error': 'Unable to process request',
            }


@app.get(base_url+'/useless/fact/{useless_fact_id}')
def getUFactWithId(useless_fact_id: int):
    try:

        if useless_fact_id < 0 or useless_fact_id > ufacts_size - 1:
            return {
                'error': 'Fact ID out of range',
                }
        else:
            return {
                'id':useless_fact_id,
                'fact': ufacts[useless_fact_id]['text'],
                'source':ufacts[useless_fact_id]['source']
                }

    except Exception as e:
        print(e)
        return {
            'error': 'Unable to process this request',
            }


@app.get(base_url+'/intresting/fact')
def getIFact():
    try:

        random_index = random.randrange(0,ifacts_size - 1)
        return {
                'id':random_index,
                'fact': ifacts[random_index],
                'source':"N/A"
                }

    except Exception as e:
        print(e)
        return {
            'error': 'Unable to process request',
            }


@app.get(base_url+'/intresting/fact/{intresting_fact_id}')
def getIFactWithId(intresting_fact_id: int):
    try:

        if intresting_fact_id < 0 or intresting_fact_id > ifacts_size - 1:
            return {
                'error': 'Fact ID out of range',
                }
        else:
            return {
                'id':intresting_fact_id,
                'fact': ifacts[intresting_fact_id],
                'source':"N/A"
                }

    except Exception as e:
        print(e)
        return {
            'error': 'Unable to process this request',
            }
@app.get('/version')
def getVersion():
    return {
        'version': version
        }
