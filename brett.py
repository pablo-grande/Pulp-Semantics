from rdflib import Graph, BNode, Namespace, Literal
from rdflib.namespace import Namespace, RDF, FOAF
from pprint import pprint

# register namespaces
people = Namespace('http://owl.man.ac.uk/2006/07/sssw/people#')
brett = Namespace('http://www.semanticweb.org/pablo/ontologies/2019/brett#')

big_brain = Graph()
big_brain.parse('ontologies/brain.owl')

# for a more readable output, bind the namespace to a prefix
big_brain.bind('me', brett)
big_brain.bind('people', people)
big_brain.bind('rdf', RDF)
big_brain.bind('foaf', FOAF)

# meet the people
# add BNodes to the Graph and tag them with different concepts such as FOAF.person and other vocabulary concepts
marcellus_wallace = BNode()
vincent_vega = BNode()
pitt = BNode()

big_brain.add((marcellus_wallace, RDF.type, FOAF.person))
big_brain.add((vincent_vega, RDF.type, FOAF.person))
big_brain.add((pitt, RDF.type, FOAF.person))


# you can add extra information about a person by adding properties to a node
big_brain.add((marcellus_wallace, RDF.type, people['bald']))
big_brain.add((marcellus_wallace, RDF.type, brett['black']))
big_brain.add((marcellus_wallace, FOAF.name, Literal("Marcellus Wallace")))


# you can add relations between nodes
big_brain.add((pitt, brett['works_for'], marcellus_wallace))
big_brain.add((vincent_vega, brett['works_for'], marcellus_wallace))


def describe(subject):
    for p, o in big_brain.predicate_objects(subject):
        print(subject, '--[', p, ']-->', o)


def t_print(*args):
    # print URIs without URL
    print(tuple([arg.split('#')[-1] for arg in args]))


def checkout(format_as='n3'):
    pprint(big_brain.serialize(format=format_as).decode('utf-8'))


if __name__ == '__main__':
    describe(marcellus_wallace)
