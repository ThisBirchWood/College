public class linked_list {
    // init size and dummy nodes
    public int size = 0;    // keep track of how many elements in list
    private DLLNode start = new DLLNode();  // dummy start node
    private DLLNode end = new DLLNode();    // dummy end node

    public static void main(String[] args){
        linked_list test_list = new linked_list();
        test_list.append(11);
        test_list.append(22);
        test_list.append(6);
        test_list.append(89);
        test_list.append(99);
        test_list.display();
        test_list.insert(50, 2);
        test_list.display();
        test_list.remove(1);
        test_list.display();
        test_list.remove(0);
        test_list.display();
        test_list.pop();
        test_list.display();
        
    }

    public linked_list(){
        // connect dummy nodes to each other
        start.next = end;
        end.prev = start;
    }

    public void display(){
        // set current node as the start
        DLLNode current = start.next;
        // loop through each node
        for (int i = 0; i < size; i++){
            // check that this isn't the first element
            if (i > 0){
                // print node
                System.out.print("->" + current.element);
            } else {
                // print now without -> prefix
                System.out.print(current.element);
            }
            // set current to next node
            current = current.next;
        }
        // go to next line
        System.out.println();
    }

    public DLLNode append(int e){
        // create new node for the element
        DLLNode new_node = new DLLNode();
        new_node.set_element(e);    // set element in node to element specified

        // adjust pointers to add node to the list
        DLLNode previous_node = end.prev;   // get last node in list
        previous_node.next = new_node;  // set the next pointer in the last node to the new node
        end.prev = new_node;    // set the prev pointer in the end dummy node to the new node
        new_node.prev = previous_node;  // set new node prev pointer to last node
        new_node.next = end;    // set new node next pointer to end dummy pointer

        // add one to size
        size++;

        // return pointer to node
        return new_node;
    }

    public int pop(){
        // get last node in list
        DLLNode node_to_remove = end.prev;

        // adjust pointers
        end.prev = node_to_remove.prev;
        node_to_remove.prev.next = end;

        // remove one from size
        size--;

        // return element
        return node_to_remove.element;
    }

    public DLLNode insert(int element, int index){
        // create node from element
        DLLNode new_node = new DLLNode();
        new_node.set_element(element);  // set element attribute to element specified

        // loop through list and find correct node to add in front of
        DLLNode current_node = start;   // set start dummy node as "current_node"
        for (int i = 0; i < index; i++){    // loop until reach the index
            current_node = current_node.next;   // go to next node in list
        }

        // adjust pointers
        DLLNode next_node = current_node.next;  // get node after current node
        current_node.next = new_node;   // set current node's next pointer to the new node
        new_node.prev = current_node;   // set new node prev pointer to current node
        new_node.next = next_node;      // set new node next pointer to next_note
        next_node.prev = new_node;      // set next_node prev pointer to new node

        // add size
        size++;
        // return node object
        return new_node;
    }

    public int remove(int index){
        // find correct node by iterating through each node
        DLLNode current_node = start;   // set current node as start dummy node
        for (int i = 0; i <= index; i++){   // loop until we reach the index specified
            current_node = current_node.next;       // set current node to next node in the list
        }

        // get previous and next nodes
        DLLNode node_to_remove = current_node;  // this is the node at the index that we want removed
        DLLNode previous_node = current_node.prev;  // node before it
        DLLNode next_node = current_node.next;  // node after it

        // adjust pointers
        previous_node.next = next_node; // set the previous node's next pointer to the node after the index
        next_node.prev = previous_node; // set the next node's prev pointer to the node before the index

        // remove and return node
        size--;
        // return the element of the node
        return node_to_remove.element;
    }

    public int length(){
        // return the instance attribute size
        return this.size;
    }
}

class DLLNode {
    // setup element, previous and next nodes
    public int element;
    public DLLNode prev = null;
    public DLLNode next = null;

    public void set_element(int e){
        // set the element variable to the input
        this.element = e;
    }
}

