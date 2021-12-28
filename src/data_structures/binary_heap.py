class BinaryHeap(object):
    def __init__(self, key = None) -> None:
        self.values = []
        
        if key is not None:
            self.key = key
        else:
            self.key = self.__default_key
        
    def peek_min(self):
        if self.values:
            return self.values[0]
        else:
            return None
        
    def insert(self, val) -> None:
        self.values.append(val)
        current_index = len(self.values) - 1
        
        self.__heap_up(current_index)
            
    def __heap_up(self, i) -> None:        
        while i != 0:
            parent_index = self.__get_parent_index(i)
            
            if self.key(self.values[i], self.values[parent_index]):
                self.values[i], self.values[parent_index] = self.values[parent_index], self.values[i]
                
                i = parent_index
            else:
                break

    def __get_children_indices(self, i):
        base = 2 * i

        return base + 1, base + 2
    
    def __get_parent_index(self, i):
        return (i - 1) // 2

    def __default_key(self, l, r):
        return l <= r