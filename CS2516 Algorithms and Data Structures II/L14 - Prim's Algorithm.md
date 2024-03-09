- Dynamic Priority Queue is slightly different to a normal priority queue
	- It allows access to all items, not just the one with the highest priority 
	- Uses a dictionary, with the key as the priority and the value as the reference to the element

## Minimum Spanning Tree
- A spanning tree is a subgraph of any Graph that connects every vertex and is a tree
- Each edge has a cost, what is the cheapest path to connect everything
- Trees have no cycles

## Prims Algorithm
```Python
T = [v], where v is any vertex in V
S = []

for each i from 2 to n
	e = {w, y}, an edge with minimum weight in E such that w is in T and y is not in T
	add e to S
	add y to T
return S
```

- T - a list of vertices
- S - a list of edges
- (collection of potential additions): APQ

```pseudo-code
create APQ pq
create empty dict locs for locations of vertices in pq
for each v in G
	add (infinity, (v, None)) into pq and store location in locs[v]
create an empty list tree, which will be the output (the edges in the tree)
while pq is not empty:
	remove c:(v,e), the minimum element, from pq
	remove v from locs
	if e is not None, append e to Tree
	for each edge d incident on v:
		w = d's opposite vertex from v
		if w is in locs
			cost = d's cost
			if cost is cheaper than w's
				replace ?:(w, ?) in pq with cost: (w, d)
return tree
```
