from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')


def get_response_dbpedia_pizzasEs():
    sparql.setQuery(f'''
        SELECT ?name ?pais1 ?imagen ?comment ?mainingredients 
        WHERE {{
            ?s dbo:type dbr:Pizza .
            ?s rdfs:label ?name .
            ?s rdfs:comment ?comment .
            ?s dbo:thumbnail ?imagen .
            ?s dbo:country ?pais .
            ?pais dbo:demonym ?pais1 .
            ?s dbp:mainIngredient ?mainingredients .
            FILTER (lang(?name ) = 'es')
            FILTER (lang(?comment) = 'es')
        }}
    ''')

    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    return qres



if __name__ == '__main__':

    result = get_response_dbpedia_pizzasEs()
    for item in result:
        name, comment, image_url = result['name']['value'], result['comment']['value'], result['image']['value']
