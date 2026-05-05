class ToDo:
    # WRONG - will be the same list for each instance
    list = []

todo_1 = ToDo()
todo_1.list.append("Go get grocieries")  # will modify the list for all instances

print(todo_1.list)

todo_2 = ToDo()
print(todo_2.list)  # todo_2 has the list of todo_1


class ToDo:
    def __init__(self):
        self.list = []  # use instance attribute

todo_1 = ToDo()
todo_1.list.append("Go get grocieries")

print(todo_1.list)

todo_2 = ToDo()
print(todo_2.list)
