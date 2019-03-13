from brett import big_brain
from rdflib.namespace import FOAF, RDF
from rdflib.plugins.sparql import prepareQuery


namespaces = {
    'foaf': FOAF,
    'rdf': RDF,
    'brett': 'http://www.semanticweb.org/pablo/ontologies/2019/brett#'
}

ask_query = prepareQuery(
    """
    ASK WHERE{
        ?person brett:works_for ?another_person .
        ?another_person rdf:type brett:bitch .
    }
    """, initNs=namespaces)

for result in big_brain.query(ask_query):
    print(result)


works_for_query = prepareQuery("""

    SELECT ?person ?another_person_name 
    WHERE{
        ?person brett:works_for ?another_person .
        ?another_person foaf:name ?another_person_name .
    }
    """, initNs=namespaces)

for row in big_brain.query(works_for_query):
    print("%s works for %s" % row)


construct_query = prepareQuery("""
    CONSTRUCT 
        { ?person foaf:name "Jules Winnfield" . } 
    WHERE{
        ?person brett:works_for ?another_person;
                rdf:type brett:black .
    }
    """, initNs=namespaces)

for row in big_brain.query(construct_query):
    print(row)
