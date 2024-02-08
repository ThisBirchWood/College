- ER (Entity Relationship) Models is a means of combining multiple views of the data model into a single unambiguous representation that is free of implementation detail.
- Various notations for ER diagrams exists, such as entity-relationship modelling (Chen, 1976) and the Unified Mark-up Language (UML), which we will be using.
## Entity Type
- An **entity type** is a group of objects in the real world that have the same properties, (usually a name and a list of properties)
	- Example: "FutureLeases has many branches around the world.  Every branch has staff. Some staff manage a branch;  this includes supervising staff"
	- 2 entities here: *Branch* and *Staff*
	- Represented as a square box

## Relationship Type
- A **relationship type** is a set of associations between entities
	- Example: "FutureLeases has many branches around the world.  Every branch has staff. Some staff manage a branch;  this includes supervising staff"
	 ![[Pasted image 20231021202347.png]]
	- The degree of these relationships is binary.
	- The "supervises" relationship is recursive.
	- Represented as arrows with text above them

## Attributes
- Entities have properties, known as **attributes**
	- Example: “Every FutureLeases branch has name, location, contact information and operating hours.”
		![[Pasted image 20231021202541.png]]
	- Represented as ovals

## Multiplicity
- Multiplicity is the amount of occurrences of an entity type that relates to another entity type.
- Difficult to decide where to apply multiplicity
	- Example 1: "Each member of staff is associated with a branch"
		![[Pasted image 20231022224357.png]]
	- Example 2: “Each branch is managed by a staff member”
		![[Pasted image 20231022224703.png]]

### Participation and Cardinality
- Multiplicity is made up of two parts, participation and cardinality
- **Participation** determines whether all or only some entity occurrences participate in the relationship.
- **Cardinality** describes the maximum number of occurrences of participating in a relationship.
- Basically min/max
 ![[Pasted image 20231022230837.png]]
## Strong/Weak Entities
- A **weak entity** is an entity whose existence is dependent on another entity.
- A **strong entity** does not depend on another entity.
- For example - a database with a bank and branches of a bank, the entity "Bank Branches" is a weak entity as it depends on the "bank" entity to exist


# Entity Relationship Notations
## Chen's
![[Pasted image 20231022234407.png]]
- Attribute with a line under the text = Identifying attribute (such as id's)
- Entity with a double line = weak entity
## Barker's
![[Pasted image 20231023000015.png]]

## Crow's Foot
![[Pasted image 20231023112659.png]]

### Relationship Notation
![[Pasted image 20231023112924.png]]



