class Person: 
    pass


def heap_sort(lst):
    pass





if __name__ == '__main__': 
    p = Person('A', 24, 1) 
    print(p) # should output: A 99

    p = Person('A', 40, 1) 
    print(p) # should output: A 199
    
    people = [ 
        Person('A', 24, 1), 
        Person('B', 32, 2), 
        Person('C', 45, 3), 
        Person('D', 22, 4), 
        Person('E', 21, 5), 
        Person('F', 32, 6), 
        Person('G', 39, 7), 
        Person('H', 44, 8), 
        Person('I', 22, 9), 
        Person('J', 29, 10), 
        Person('K', 32, 11), 
        Person('L', 31, 12) 
    ]
    
    print([str(p)  for p in people])
    heap_sort(people) 
    print([str(p)  for p in people])
    # sould output: 
    # ['C 197', 'H 192', 'A 99', 'B 98', 'D 96', 'E 95', 'F 94', 'G 93', 'I 91', 'J 90', 'K 89', 'L 88']