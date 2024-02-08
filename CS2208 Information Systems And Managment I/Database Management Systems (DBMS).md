- Database Management Systems are used to organize large quantities of information by providing systems for storing, managing and retrieval of information.
- They should store data safety and securely. They should be designed to be robust to errors, and should avoid designs which result in [[anomalous states]]
## How to connect to a DBMS
- We can connect to a DBMS through several techniques:
	- **Programmatically**: using a programming language such as Python
	- **CLI** (command line interface): Such as CMD or bash
	- **GUI**: Such as MySQL workbench or other software
## How to host a DBMS
1) **Native installation**: Simply installing it on your OS.
2) **Container Based Installation:** Using OS virtualization software such as Docker or Kubernetes to run a container.
3) **Virtual Machine**: Using something such as VirtualBox and then install an OS image that includes as DBMS.
4) **Cloud Based Installation**: Use virtualized remote resources to host a DBMS.

# Databases
- A collection of data which is hosted on a DBMS
- The design of a database is known as a [[schema]] and is made up of columns and relationship
- A database should be viewed as a collection of relations which are made up of a list of attributes.
- This list of attributes is known as a [[Array Based Lists#Tuples|Tuple]]
# Relations and keys
- Each tuple must be uniquely identified, normally with a primary key/superkey.
- A **superkey** is an attribute which identify a tuple

# Queries
- Queries are commands used to query information in one or more relations in a database
