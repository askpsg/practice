class DataNode:
    def __init__(self, key: int, value: int, before: "DataNode" = None, after: "DataNode" = None):
        self.key = key
        self.value = value
        self.before = before
        self.after = after

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCache:
    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.__capacity: int = capacity
        self.__data: dict[int, DataNode] = {}
        self.__recent: DataNode = None
        self.__oldest: DataNode = None
    

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        if key not in self.__data:
            return -1
        
        self.__make_latest(key)
        return self.__data[key].value

    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.__data:
            self.__data[key].value = value
            self.__make_latest(key)
        else:
            if len(self.__data) == self.__capacity:
                self.__remove_last()
            
            self.__data[key] = DataNode(key, value, None, self.__recent)
            if self.__recent:
                self.__recent.before = self.__data[key]
            if not self.__oldest:
                self.__oldest = self.__data[key]

            self.__recent = self.__data[key]

    def __remove_last(self):
        data_node = self.__oldest
        self.__oldest = data_node.before

        if self.__oldest:
            self.__oldest.after = None

        del self.__data[data_node.key]
        del data_node
    
    def __make_latest(self, key):
        data_node = self.__data[key]
        if data_node == self.__recent:
            return
        
        if data_node == self.__oldest:
            self.__oldest = self.__oldest.before
            self.__oldest.after = None

        before_node = data_node.before
        after_node = data_node.after
        if after_node:
            after_node.before = before_node

        before_node.after = after_node

        self.__recent.before = data_node
        data_node.after = self.__recent
        data_node.before = None

        self.__recent = data_node
