from rdflib import Graph, BNode, Literal
from rdflib.namespace import Namespace, RDF, FOAF


# register namespaces
people = Namespace('http://owl.man.ac.uk/2006/07/sssw/people#')
brett = Namespace('http://www.semanticweb.org/pablo/ontologies/2019/brett#')

big_brain = Graph()

# meet the people
# add BNodes to the Graph and tag them with different concepts such as FOAF.person and other vocabulary concepts
marcellus_wallace = BNode()
vincent_vega = BNode()
pitt = BNode()

big_brain.add((marcellus_wallace, RDF.type, FOAF.person))
big_brain.add((vincent_vega, RDF.type, FOAF.person))
big_brain.add((pitt, RDF.type, FOAF.person))


# you can add extra information about a person by adding properties to a node
big_brain.add((pitt, RDF.type, brett['black']))
big_brain.add((marcellus_wallace, RDF.type, brett['black']))
big_brain.add((marcellus_wallace, RDF.type, brett['bald']))
big_brain.add((marcellus_wallace, FOAF.name, Literal("Marcellus Wallace")))


# you can add relations between nodes
big_brain.add((pitt, brett['works_for'], marcellus_wallace))
big_brain.add((vincent_vega, brett['works_for'], marcellus_wallace))


def describe(subject):
    for predicate, object in big_brain.predicate_objects(subject):
        print(subject, predicate, object)


def checkout():
    # print our big brain
    for s, p, o in big_brain:
        print(s, p, o)


if __name__ == '__main__':
    describe(marcellus_wallace)
