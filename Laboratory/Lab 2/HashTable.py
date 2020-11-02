from collections import deque

class HashTable:
    def __init__(self, length):
        self.__values = [deque() for _ in range(length)]
        self.__size = 0

    '''
    The method hashed the given key
    Input: @key - a string
    Output: integer
    '''
    def hash(self, key):
        asciiSum = 0
        for character in key:
            asciiSum += ord(character) - ord('0') # ord() returns the unicode of the given character
        return asciiSum % len(self.__values)

    def size(self):
        return self.__size

    '''
    The method adds the given key to the hashtable if it does not exists. If it exists it returns the existing one
    Input: @key - a string
    Output: None, if it did not exist already
            True, if it already existed
    '''
    def add(self, key):
        value = self.search(key)
        if value is False:
            hashedKey = self.hash(key)
            self.__values[hashedKey].append(key)
            self.__size += 1
            return self.position(key)
        else:
            return value

    '''
    The method determines if the given key exists
    Input: @key - a string
    Output: True if it exists
            False otherwise
    '''
    def search(self, key):
        return key in self.__values[self.hash(key)]

    """
    The method returns a pair if the key exists or (-1,-1) if it does not
    Input: @key - a string
    Output: (int,int) - a pair of integers
    """
    def position(self, key):
        value = self.search(key)
        if value is False:
            return (-1,-1)
        position = self.hash(key)
        index = 0
        for k in self.__values[position]:
            if k == key:
                return (position, index)
            else:
                index +=1

    def __str__(self):
        result = ""
        for i in range(len(self.__values)):
            result += str(i) + ": " + str(self.__values[i]) + "; \n"
        return result
