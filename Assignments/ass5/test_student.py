from a05 import LinkedList 


def test_s_push_1(): 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)

    m = '[1,2,3]'
    assert "".join(str(l).split()) == m


def test_s_rev_1(): 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)
    l.reverse_list()

    m = '[3,2,1]'
    assert "".join(str(l).split()) == m


def test_s_rev_2(): 
    l = LinkedList() 
    l.push(10) 
    l.push(20)
    l.reverse_list()

    m = '[20,10]'
    assert "".join(str(l).split()) == m

def test_s_rev_3(): 
    l = LinkedList() 
    l.reverse_list()

    m = '[]'
    assert "".join(str(l).split()) == m

def test_s_rev_4(): 
    l = LinkedList() 
    l.push(4)
    l.reverse_list()

    m = '[4]'
    assert "".join(str(l).split()) == m