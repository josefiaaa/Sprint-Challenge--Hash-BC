#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for ticket in tickets:
        if ticket.source == "NONE":
            hash_table_insert(hashtable, 'start', ticket.destination)
        else:
            hash_table_insert(hashtable, ticket.source, ticket.destination)
            # We can hash each ticket such that the starting 
            # location is the key and the destination is the value.
            # Then, when constructing the entire route, 
            # the `i`th location in the route can be found by checking
            #  the hash table for the `i-1`th location.
    route[0] =hash_table_retrieve(hashtable, 'start')
    for i in range (1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
    return route
