#Simple example of a hashmap

class HashMap:
    def __init__(self):
        self.size=6
        #Create a list according to the size and populate with None
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        #iterate over every character in the key
        for char in str(key):
            #count the unicode code point of the character 
            hash += ord(char)
            #get modulo of the hash number
        return hash % self.size

    def add(self, key, value):
        #get the hash value from the _get_hash function
        key_hash = self._get_hash(key)
        #create a list of key value
        key_value = [key, value]

        # if the position in the list is free
        if self.map[key_hash] is None:
            #insert new list inside the list
            self.map[key_hash] = list([key_value])
            return True
        else:
            # append new value into collision
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        # Get the key
        key_hash = self._get_hash(key)
        # If the key_hash exists
        if self.map[key_hash] is not None:
            # Get each entry in the list (incase of a collision)
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
    
    def printing(self):
        print('------PHONEBOOK------')
        for item in self.map:
            if item is not None:
                print(str(item))

h = HashMap()
h.add('Bob', '123123')
h.add('Claire', '4444')
h.printing()
h.delete('Bob')
h.printing()
