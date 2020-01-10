from a03 import LinkedList 


def test_s_len_1(): 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 

    assert l.len() == 2

def test_s_len_2(): 
    l = LinkedList() 
    assert l.len() == 0

def test_s_len_3(): 
    l = LinkedList() 
    l.push(5) 
    l.push(2)
    l.pop()

    assert l.len() == 1

def test_s_remove_1(): 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 
    
    l.remove(5)
    m = '[6]'
    assert str(l).strip() == m
    # assert len(l) == len(m) and all([x==y for x, y in zip(l, m)])


def test_s_remove_2(): 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 
    
    l.remove(6)
    m = '[5]'
    assert str(l).strip() == m


def test_s_remove_2(): 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 
    
    l.remove(19)
    m = '[5, 6]'
    assert str(l).strip() == m
    

def test_s_get_1(): 
    l = LinkedList() 
    l.push(10) 
    l.push(11)
    l.push(12)
    assert l.get(0) == 10
    

def test_s_get_2(): 
    l = LinkedList() 
    l.push(10) 
    l.push(11)
    l.push(12)
    assert l.get(1) == 11


def test_s_get_3(): 
    l = LinkedList() 
    l.push(10) 
    l.push(11)
    l.push(12)
    l.pop()
    try: 
        l.get(2)
        raise AssertionError("IndexError not raised as expected!")
    except IndexError:
        pass  
    