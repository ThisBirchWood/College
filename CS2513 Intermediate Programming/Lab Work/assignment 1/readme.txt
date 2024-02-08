STUDENT NUMBER: 122415616

This project is meant to simulate a computer with the main file being "computer.py".
It has multiple different components such as CPU, GPU, RAM, SSD, most of which inherit off the "computer_part" class.
Just like building a real computer, they can be pieced together almost like lego.
Similarly the storage_part class (which inherits off of computer_part) is a parent to SSD and HDD.

Encapuslation is also kept in all the classes, though I left out some of the setter methods because say for example, you're not meant to
be able to change the amount of memory already on a GPU, though where I thought they were suitable, I added them.

Aggregation is also used in the computer.py class, where I initialise many parts outside of the class, and they can them be assosiated/put
into a motherboard class which can then be put in a computer class.

Composition is also used when initialising the PSU in the computer class.

The project ended up being more messy than I wanted it due to the long init arguements but I think it all still works well.
