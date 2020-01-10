try:
    from a07 import Person
except ImportError:
    pass

try:
    from a07 import heap_sort
except ImportError:
    pass


def test_s_person_1():
    p = Person('A', 24, 1)
    assert str(p) == 'A 99'

def test_s_person_2():
    p = Person('A', 49, 10)
    assert str(p) == 'A 190'


def test_heap_sort_1(): 
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

    heap_sort(people) 
    l = ['C 197', 'H 192', 'A 99', 'B 98', 'D 96', 'E 95', 'F 94', 
            'G 93', 'I 91', 'J 90', 'K 89', 'L 88']
    
    assert len(l) == len(people)
    for i, j in zip(l, people): 
        assert i == str(j)


def test_heap_sort_2(): 
    people = []

    heap_sort(people) 
    l = []
    
    assert len(l) == len(people)
    for i, j in zip(l, people): 
        assert i == str(j)

def test_heap_sort_3(): 
    people = [ 
        Person('A', 24, 10), 
        Person('B', 32, 2), 
        Person('C', 5, 3), 
        Person('D', 22, 4), 
        Person('E', 41, 9)
    ]

    heap_sort(people) 
    l = ['E 191', 'B 98', 'C 97', 'D 96', 'A 90']
    
    assert len(l) == len(people)
    for i, j in zip(l, people): 
        assert i == str(j)


def test_heap_sort_4(): 
    people = [ 
        Person('A', 41, 10), 
        Person('B', 42, 2), 
        Person('C', 46, 3)
    ]

    heap_sort(people) 
    l = ['B 198', 'C 197', 'A 190']
    
    assert len(l) == len(people)
    for i, j in zip(l, people): 
        assert i == str(j)