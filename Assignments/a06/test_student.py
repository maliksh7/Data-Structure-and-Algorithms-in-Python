try: 
    from a06 import TreeNode
except ImportError: 
    pass 


try: 
    from a06 import Person
except ImportError: 
    pass


try: 
    from a06 import Collector
except ImportError: 
    pass 

def get_hier(): 
    director = Person("Director")
    hod_1 = Person("HoD 1")
    hod_2 = Person("HoD 2")
    faculty_cs_1 = Person("CS 1")
    faculty_cs_2 = Person("CS 2")
    faculty_ee_1 = Person("EE 1")
    faculty_ee_2 = Person("EE 2")

    t_d = TreeNode(director)
    t_d.left = TreeNode(hod_1)
    t_d.right = TreeNode(hod_2)

    t_d.left.left = TreeNode(faculty_cs_1)
    t_d.left.right = TreeNode(faculty_cs_2)

    t_d.right.left = TreeNode(faculty_ee_1)
    t_d.right.right = TreeNode(faculty_ee_2)
    return t_d

def get_hier_2(): 
    director = Person("Rector")
    hod_1 = Person("Registrar")
    hod_2 = Person("Controller")
    faculty_cs_1 = Person("Exam 1")
    faculty_cs_2 = Person("Exam 2")
    faculty_ee_1 = Person("Account 1")
    faculty_ee_2 = Person("Account 2")

    t_d = TreeNode(director)
    t_d.left = TreeNode(hod_1)
    t_d.right = TreeNode(hod_2)

    t_d.left.left = TreeNode(faculty_cs_1)
    t_d.left.right = TreeNode(faculty_cs_2)

    t_d.right.left = TreeNode(faculty_ee_1)
    t_d.right.right = TreeNode(faculty_ee_2)
    return t_d


def test_s_person_1(): 
    director = Person("Director")
    hod_1 = Person("HoD 1")

    assert str(director) == 'Director'


def test_s_find_val_1(): 
    t_d = get_hier()
    node = t_d.find_val('Director')
    assert str(node.val) == 'Director'

def test_s_find_val_2(): 
    t_d = get_hier()
    node = t_d.find_val('HoD 3')
    assert node is None


def test_s_find_val_3(): 
    t_d = get_hier_2()
    node = t_d.find_val('Director')
    assert node is None


def test_s_find_val_4(): 
    t_d = get_hier_2()
    node = t_d.find_val('Account 1')
    assert str(node.val) == 'Account 1'


def test_s_find_val_5(): 
    t_d = get_hier_2()
    node = t_d.find_val('Account 2')
    assert str(node.val) == 'Account 2'



def test_s_collector_1():
    t_d = get_hier()
    c = Collector() 
    t_d.dfs_apply(c.process)
    assert c.get_list()  == ['Director', 'HoD 1', 'CS 1', 'CS 2', 'HoD 2', 'EE 1', 'EE 2']


def test_s_collector_1():
    t_d = get_hier()
    c = Collector() 
    t_d.left.dfs_apply(c.process)
    assert c.get_list()  == ['HoD 1', 'CS 1', 'CS 2']

def test_s_collector_2():
    t_d = get_hier()
    c = Collector() 
    t_d.left.left.dfs_apply(c.process)
    assert c.get_list()  == ['CS 1']


def test_s_hierarchy_1(): 
    t_d = get_hier()
    l = t_d.find_people_in_hierarchy('Director')
    assert l == ['Director', 'HoD 1', 'CS 1', 'CS 2', 'HoD 2', 'EE 1', 'EE 2']


def test_s_hierarchy_2(): 
    t_d = get_hier()
    l = t_d.find_people_in_hierarchy('HoD 2')
    assert l == ['HoD 2', 'EE 1', 'EE 2']


def test_s_hierarchy_3(): 
    t_d = get_hier()
    try: 
        t_d.find_people_in_hierarchy('Accountant')
        raise AssertionError("Expecting a ValueError when node is not found.")
    except ValueError: 
        pass 

    