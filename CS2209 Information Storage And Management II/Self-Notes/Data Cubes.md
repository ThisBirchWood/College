- Data cubes are multi-dimensional structures that stores many different related values
- Commonly used in [[Data Warehousing + OLAP|Data Warehouses]]
![[Pasted image 20240226100935.png]]

# Building Cubes
- Imagine we have a table for a days worth of sales
![[Pasted image 20240226101053.png]]
- We can start building up a cube by stacking each table of days on top of each other
- Then, another dimension is added, *time* ![[Pasted image 20240226101129.png]]
- Dimensions have a number of *members* 
	- Branches has: Dublin, Cork, Limerick, Galway

# Multi-dimensional Operations

## Roll Up
- Aggregate dimension to decrease *granularity* (wtf)
![[Pasted image 20240226101328.png]]
- All the Irish cities are grouped into just *Ireland*
- All the food categories are grouped

## Dicing & Drill Down
- Basically the opposite of rollup, this involves splitting the existing categories down into more specific categories
	- Should these more specific categories exist in the database of course
![[Pasted image 20240226101751.png]]
- Cities could be split into their respective sub-areas
- Food could be split into their different flavours

## Slicing
- Involves selecting a member of a dimension and ignoring the rest of that dimension
![[Pasted image 20240226101856.png]]
- Select just Corks data


# SQL Data Cubes
## Cube Command
- GROUP BY \<attributes\> WITH CUBE
- This command creates all possible combinations of the columns specified
- It also includes a NULL attribute, which will just include everything else
![[Pasted image 20240226103137.png]]
- This table becomes this:
![[Pasted image 20240226103206.png]]

## Rollup Command
- Very similar to the CUBE command, but instead it follows a certain order
![[Pasted image 20240226104628.png]]
- This would show the subtotals for region, then for product, then for the combinations of the region and product, then a grand total
