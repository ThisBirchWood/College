public class linked_list {
    public int size = 0;
    private DLLNode start = new DLLNode();
    private DLLNode end = new DLLNode();

    public linked_list(){
        start.next = end;
        end.prev = start;
    }

    public DLLNode append(int e){
        DLLNode new_node = new DLLNode();
        new_node.set_element(e);

        DLLNode previous_node = end.prev;
        previous_node.next = new_node;
        end.prev = new_node;

        new_node.prev = previous_node;
        new_node.next = end;

        size += 1;

        return new_node;
    }

    public int pop(){
        DLLNode node_to_remove = end.prev;

        end.prev = node_to_remove.prev;
        node_to_remove.prev.next = end;

        size -= 1;

        return node_to_remove.element;
    }
}

class DLLNode {
    public int element;
    public DLLNode prev = null;
    public DLLNode next = null;

    public void set_element(int e){
        element = e;
    }
}

