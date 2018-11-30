import requests, json

def sparql(domain, query):
    url = 'http://%s/sparql' % domain
    response = requests.post(url, data={'print': True, 'query': query})
    if response:
        try:
            response = response.json()
            print(json.dumps(response, indent=2))
        except Exception as e:
            print(reponse)
            raise e

if __name__ == '__main__':
    import sys
    try:
        _, DOMAIN, QUERY = sys.argv
    except Exception as e:
        print('Usage: python sparql.py DOMAIN QUERY')
        sys.exit(0)

    sparql(DOMAIN, QUERY)
