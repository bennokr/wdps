import requests
import sys
import json, re
import collections, math

ELASTICSEARCH_URL = 'http://10.149.0.127:9200/freebase/label/_search'
TRIDENT_URL = 'http://10.141.0.11:8082/sparql'

query = sys.argv[1]

print('Searching for "%s"...' % query)
response = requests.get(ELASTICSEARCH_URL, params={'q': query, 'size':100})
ids = set()
labels = {}
scores = {}

if response:
    response = response.json()
    for hit in response.get('hits', {}).get('hits', []):
        freebase_id = hit.get('_source', {}).get('resource')
        label = hit.get('_source', {}).get('label')
        score = hit.get('_score', 0)

        ids.add( freebase_id )
        scores[freebase_id] = max(scores.get(freebase_id, 0), score)
        labels.setdefault(freebase_id, set()).add( label )

print('Found %s results.' % len(labels))


prefixes = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX fbase: <http://rdf.freebase.com/ns/>
"""
same_as_template = prefixes + """
SELECT DISTINCT ?same WHERE {
    ?s owl:sameAs %s .
    { ?s owl:sameAs ?same .} UNION { ?same owl:sameAs ?s .}
}
"""
po_template = prefixes + """
SELECT DISTINCT * WHERE {
    %s ?p ?o.
}
"""

print('Counting KB facts...')
facts  = {}
for i in ids:
    response = requests.post(TRIDENT_URL, data={'print': False, 'query': po_template % i})
    if response:
        response = response.json()
        n = int(response.get('stats',{}).get('nresults',0))
        print(i, ':', n)
        sys.stdout.flush()
        facts[i] = n

def get_best(i):
    return math.log(facts[i]) * scores[i]

print('Best matches:')
for i in sorted(ids, key=get_best, reverse=True)[:3]:
    print(i, ':', labels[i], '(facts: %s, score: %.2f)' % (facts[i], scores[i]) )
    sys.stdout.flush()
    response = requests.post(TRIDENT_URL, data={'print': True, 'query': same_as_template % i})
    if response:
        response = response.json()
        for binding in response.get('results', {}).get('bindings', []):
            print(' =', binding.get('same', {}).get('value', None))
