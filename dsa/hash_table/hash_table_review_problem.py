class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    # Problem 1:
    # contains_key 메서드를 작성하세요.
    # key가 hash table 안에 있으면 True, 없으면 False를 반환합니다.
    def contains_key(self, key):
        index = self.__hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return True
        return False


    # Problem 2:
    # values 메서드를 작성하세요.
    # hash table 안에 저장된 모든 value를 리스트로 반환합니다.
    def values(self):
        all_values = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_values.append(self.data_map[i][j][1])

        return all_values


my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)
my_hash_table.set_item("nails", 400)

print("Has bolts:", my_hash_table.contains_key("bolts"))
print("Has screws:", my_hash_table.contains_key("screws"))
print("Keys:", my_hash_table.keys())
print("Values:", my_hash_table.values())


"""
    EXPECTED OUTPUT:
    ----------------
    Has bolts: True
    Has screws: False
    Keys: ['bolts', 'washers', 'lumber', 'nails']
    Values: [1400, 50, 70, 400]

"""
