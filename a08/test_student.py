try:
    from a08 import HashMap
except ImportError:
    pass




def test_s_hashmap_add_1(): 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(25, "twenty five")
    h.add(26, "twenty six updated")
    h.add(887, "large number")

    assert h.get(26) == "twenty six updated"


def test_s_hashmap_add_2(): 
    h = HashMap() 

    h.add("blah", "blah text")
    h.add(26, "twenty six")
    h.add(887, "large number")

    assert h.get("blah") == "blah text"

def test_s_hashmap_add_3(): 
    h = HashMap() 

    h.add((24, 2), "tuple text")
    h.add(26, "twenty six")
    h.add(887, "large number")

    assert h.get((24, 2)) == "tuple text"




def test_s_hashmap_del_1(): 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(887, "large number")
    h.delete(17)

    try: 
        h.get(17)
        raise AssertionException("Expected a KeyError after delete")
    except: 
        pass 

def test_s_hashmap_del_2(): 
    h = HashMap() 

    h.add("blah", "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(887, "large number")
    h.delete("blah")

    try: 
        h.get("blah")
        raise AssertionException("Expected a KeyError after delete")
    except: 
        pass

def test_s_hashmap_del_3(): 
    h = HashMap() 

    h.add("blah", "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(887, "large number")
    h.delete("blah")

    h.get(26) == "twenty six"
