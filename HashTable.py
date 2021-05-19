# HashTable class using chaining which includes an insert, search and remove method.
class HashTable:
    # Constructor with assignable capacity. Buckets are empty lists
    # Time Complexity O(1)
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for x in range(initial_capacity):
            self.table.append([])

    # Requirement E: Objects inserted using package id as the key
    # Inserts a new item into the hash table.
    # Time Complexity O(n)
    def insert(self, key, package):
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = package
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, package]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # Time Complexity O(n)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]
        return None

    # Removes an item with matching key from the hash table.
    # Time Complexity O(n)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

