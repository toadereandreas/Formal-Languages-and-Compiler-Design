from HashTable import HashTable

class SymbolTable:

    def __init__(self, size):
        self.__hashTable = HashTable(size)

    # def add(self, key):
    #     self.__hashTable.add(key)
    #
    # def size(self):
    #     return self.__hashTable.size()
    #
    # def search(self, key):
    #     return self.__hashTable.search(key)

    '''
    The method adds in the hashtable the given key if it does no exist.
    If it does, it returns what is already there
    Input: @key - a string
    Output: a pair
    '''
    def position(self, key):
        if self.__hashTable.search(key):
            return self.__hashTable.position(key)
        else:
            return self.__hashTable.add(key)

    def __str__(self):
        return str(self.__hashTable)
