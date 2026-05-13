def set_value(self, index, value):
    if index < 0 or index >= self.length:
        return None
    temp = self.head
    for _ in range(index):
        temp = temp.next
    temp.value = value
    return True

def set_value(self, index, value):
    temp = self.get(index)
    if temp:
        temp.value = value
        return True
    else:
        return False
