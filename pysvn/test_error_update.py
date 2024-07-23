import copy

class MyClass:
    def delete_member(self):
        return self.members

# 浅拷贝
def copy_loop():
    d1 = {"a": 1, "b": [2, 3]}
    d2 = copy.copy(d1)

    while d1 == d2:
        d2["b"].append(4)

def endless_rec(a):
    if not a:
        return endless_rec(a-1)