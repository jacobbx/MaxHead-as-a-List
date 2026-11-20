

def extract(h):
    
    if h is None:
        raise ValueError("no heap")
    
    if not h:
        raise ValueError("empty heap")

    if len(h) == 1:
        return h.pop(0)
        
    current_index = 0
    root_value = h[current_index]
    h[current_index] = h.pop(-1)

    left_child = (2 * current_index) + 1
    right_child = (2 * current_index) + 2
                    
    while (
        (left_child < len(h) and h[current_index] < h[left_child]) 
        or (right_child < len(h) and h[current_index] < h[right_child])
    ):
        if len(h) <= 3:
            if h[left_child] > h[current_index]:
                h[left_child], h[current_index] = h[current_index], h[left_child]
                
            return root_value
        
        if right_child < len(h):
            if h[left_child] > h[right_child] and h[left_child] > h[current_index]:   
                h[left_child], h[current_index] = h[current_index], h[left_child]
                current_index = left_child
            elif h[right_child] > h[left_child] and h[right_child] > h[current_index]:
                h[right_child], h[current_index] = h[current_index], h[right_child]
                current_index = right_child
        else:
            if h[left_child] > h[current_index]:
                h[left_child], h[current_index] = h[current_index], h[left_child]
                current_index = left_child
            else:
                break

        left_child = (2 * current_index) + 1
        right_child = (2 * current_index) + 2

    return root_value
        

def insert(h, value):
    
    if h is None:
        raise ValueError("no heap")
    

    if value is None:
        raise ValueError("null key")
    
    if len(h) > 0:
        try:
            value < h[0]
        except Exception:
            raise Exception("heap error")
    
    h.append(value)
    
    current_index = len(h) - 1
    parent_index = (current_index - 1) // 2
        
    while current_index > 0:
        if h[current_index] > h[parent_index]:
            h[current_index], h[parent_index] = h[parent_index], h[current_index]
            current_index = parent_index
            parent_index = (current_index - 1) // 2
        else:
            break
                
            
# helper routine for recursive traversal
# returns a list which is the in-order traversal
# of the subtree rooted at node


def _iOR(t, node):
    if (node >= len(t)) or (t[node] is None):
        return []
    left = _iOR(t, (2 * node) + 1)
    right = _iOR(t, (2 * node) + 2)
    return left + [t[node]] + right


# Classic inorder recursive traversal


def inOrderRecurse(t):
    return _iOR(t, 0)
