try: 
    from a02 import Address
except ImportError: 
    pass 

try: 
    from a02 import Employee 
except ImportError: 
    pass 

try: 
    from a02 import Lecturer
except ImportError: 
    pass 

def test_s_address_1(): 
    a = Address() 
    a.house_no = 2 
    a.street = 3 
    a.city = "Peshawar"
    a.country = "Pakistan"

    assert a.get_full_address() == "H. No. 2, Street 3, Peshawar Pakistan"

def test_s_address_2(): 
    a = Address(2, 3, "Peshawar", "Pakistan") 
    assert a.get_full_address() == "H. No. 2, Street 3, Peshawar Pakistan"

def test_s_address_3(): 
    a = Address(21, 3, "Peshawar", "Pakistan") 
    assert str(a) == "H. No. 21, Street 3, Peshawar Pakistan"


def test_s_employee_1(): 
    e = Employee() 
    e.set_current_address(1, 2, "Cape Town", "South Africa")
    assert e.get_current_address()  == "H. No. 1, Street 2, Cape Town South Africa"


def test_s_employee_2(): 
    e = Employee() 
    e.set_current_address(1, 2, "Cape Town", "South Africa")
    assert e.get_permanent_address()  == 'None' or e.get_permanent_address() is None

def test_s_employee_3(): 
    e = Employee() 
    e.set_permanent_address(1, 2, "Cape Town", "South Africa")
    assert e.get_permanent_address()  == "H. No. 1, Street 2, Cape Town South Africa"


def test_s_employee_3(): 
    e = Employee(11, "Ali") 
    e.set_permanent_address(1, 2, "Cape Town", "South Africa")
    assert str(e) == "11 Ali H. No. 1, Street 2, Cape Town South Africa"


def test_s_lecturer_1(): 
    l = Lecturer() 
    l.set_permanent_address(44, 24, "KL", "Malaysia")
    assert str(l) == "Lecturer: 1 Mr. Bigshot H. No. 44, Street 24, KL Malaysia"


