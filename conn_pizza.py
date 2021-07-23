from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    'http://localhost:3030/ds')


def consultar_owl_TradicionalPizza():
    sparql.setQuery('''

        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf x:TradicionalPizza .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

def consultar_owl_EventoPizza():
    sparql.setQuery('''

        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf x:EventoPizza .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

def consultar_owl_tiposPizzas():
    sparql.setQuery('''

        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name
        WHERE { 
            ?s  rdfs:subClassOf x:Pizza .
            ?s rdfs:label ?name 
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

def consultar_owl_pizzaNavidad():
    sparql.setQuery('''
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name
        WHERE { 
            x:NavidadCoronaPizza rdfs:subClassOf ?o .
            ?o owl:someValuesFrom ?h .
            ?h rdfs:label ?name 
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

def consultar_owl_pizzaHalloween():
    sparql.setQuery('''
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name
        WHERE { 
            x:HalloweenPizza rdfs:subClassOf ?o .
            ?o owl:someValuesFrom ?h .
            ?h rdfs:label ?name 
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

def consultar_owl_pizzaSanValentin():
    sparql.setQuery('''
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name
        WHERE { 
            x:CorazonSanValentinPizza rdfs:subClassOf ?o .
            ?o owl:someValuesFrom ?h .
            ?h rdfs:label ?name 
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

def consultar_owl_pizzaHawaiana():
    sparql.setQuery('''
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name
        WHERE { 
            x:HawainaPizza  rdfs:subClassOf ?o .
            ?o owl:someValuesFrom ?h .
            ?h rdfs:label ?name 
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

def consultar_owl_pizzaNaturista():
    sparql.setQuery('''
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name
        WHERE { 
            x:NaturistaPizza  rdfs:subClassOf ?o .
            ?o owl:someValuesFrom ?h .
            ?h rdfs:label ?name 
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

def consultar_owl_pizzaPepperoni():
    sparql.setQuery('''
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX x:<http://www.semanticweb.org/tfgra/ontologies/2021/5/special-pizza#>
        
        SELECT DISTINCT ?name
        WHERE { 
            x:PepperoniSpecialPizza  rdfs:subClassOf ?o .
            ?o owl:someValuesFrom ?h .
            ?h rdfs:label ?name 
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    print(qres)
    return qres

if __name__ == '__main__':
    consultar_owl_TradicionalPizza()
    consultar_owl_tiposPizzas()
