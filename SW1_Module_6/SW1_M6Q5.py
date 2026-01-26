def filter_even_numbers(l):
    return [x for x in l if x % 2 == 0]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Original list: {list}")
print(f"List with even numbers only: {filter_even_numbers(list)}")