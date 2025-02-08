def setup_module(module):
    print("\nthis setup_module functions will run only at the time of before FIRST test case start ...")
    
def teardown_module(module):
    print("\nthis teardown_module functions will run only at the time of after LAST test case END ...")
    
def setup_function(function):
    print("\nthis setup_function functions start at the time of before EACH test case start ...")
    
def teardown_function(function):
    print("\nthis teardown_function functions start at the time of AFTER EACH test case END ...")
    
def test_case_001():
    print("test case 001")
    
def test_case_002():
    print("test case 002")

    