from a04 import Ring 


def test_s_len_1(): 
    l = Ring() 
    l.insert(0, 5) 
    l.insert(0, 6) 

    assert l.len() == 2

def test_s_len_2(): 
    l = Ring() 
    assert l.len() == 0

def test_s_len_3(): 
    l = Ring() 
    l.push(5) 
    l.push(2)
    l.pop()

    assert l.len() == 1

def test_s_remove_1(): 
    l = Ring() 
    l.push(5) 
    l.push(6) 
    
    l.remove(5)
    m = '[6]'
    assert "".join(str(l).split()) == m
    # assert len(l) == len(m) and all([x==y for x, y in zip(l, m)])


def test_s_remove_2(): 
    l = Ring() 
    l.push(5) 
    l.push(6) 
    
    l.remove(6)
    m = '[5]'
    assert "".join(str(l).split()) == m


def test_s_remove_3(): 
    l = Ring() 
    l.push(5) 
    l.push(6) 
    
    l.remove(19)
    m = '[5,6]'
    assert "".join(str(l).split()) == m
    
def test_s_remove_at_1(): 
    l = Ring() 
    l.push(5) 
    l.remove_at(0) 
    
    m = '[]'
    assert "".join(str(l).split()) == m


def test_s_remove_at_2(): 
    l = Ring() 
    l.push(5) 
    l.push(8) 
    l.remove_at(1) 
    
    m = '[5]'
    assert "".join(str(l).split()) == m



def test_s_remove_at_3(): 
    l = Ring()
    l.remove_at(0) 
    
    m = '[]'
    assert "".join(str(l).split()) == m



def test_s_get_1(): 
    l = Ring() 
    l.push(10) 
    l.push(11)
    l.push(12)
    assert l.get(0) == 10
    

def test_s_get_2(): 
    l = Ring() 
    l.push(10) 
    l.push(11)
    l.push(12)
    assert l.get(1) == 11


def test_s_get_3(): 
    l = Ring() 
    try: 
        l.get(2)
        raise AssertionError("IndexError not raised as expected!")
    except IndexError:
        pass  
    

def test_s_get_4(): 
    l = Ring() 
    l.push(1)
    l.push(2)
    l.push(4)
    assert l.get(5) == 4