from brett import big_brain, namespaces as ns



def works_for():
    works_for_query = """
        SELECT ?person_name ?another_person_name WHERE{
            ?person <prefix>works_for ?another_person
            ?person foaf:name ?person_name .
            ?person foaf:name ?another_person_name .
        }
    """
    for row in big_brain.query(works_for_query):
        print("%s works for %s" % row)
