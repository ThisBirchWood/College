from priority_queues import AdaptablePriorityQueue, UnsortedListPriorityQueue
from graph_gen import graph_generator
from random import seed


def prim(g):
    pq = AdaptablePriorityQueue()

    locs = {}

    for v in g.vertices():
        locs[v] = pq.add(float("inf"), (v, None))

    tree = []

    while pq.length() > 0:
        c = pq.remove_min()
        v = c._value[0]
        e = c._value[1]
        
        if v in locs:
            del locs[v]

        if e != None:
            tree.append(e)

        for d in g.get_edges(v):
            w = d.opposite(v) 

            if w in locs:
                cost = d.element
                if cost < pq.get_key(locs[w]):
                    element = pq.update_key(locs[w], cost)

                    pq.queue[element._index]._value = (w, d)
    return tree

def prim_unsorted(g):
    pq = UnsortedListPriorityQueue()

    locs = {}

    for v in g.vertices():
        locs[v] = pq.add(float("inf"), (v, None))

    tree = []

    while pq.length() > 0:
        c = pq.remove_min()
        v = c._value[0]
        e = c._value[1]
        
        if v in locs:
            del locs[v]

        if e != None:
            tree.append(e)

        for d in g.get_edges(v):
            w = d.opposite(v) 

            if w in locs:
                cost = d.element
                if cost < pq.get_key(locs[w]):
                    element = pq.update_key(locs[w], cost)

                    pq.queue[element._index]._value = (w, d)
    return tree
