# Write a function pop_four_elements()
# that removes the last four elements of a list parameter.

def pop_four_elements(items):
    for i in range(4):
        items.pop()


items_to_update = input().split()

pop_four_elements(items_to_update)
print(items_to_update)