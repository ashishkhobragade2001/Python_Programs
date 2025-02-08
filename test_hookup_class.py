class Testclass:
    @classmethod
    def setup_class(cls):
        print("\nsetup_class method : start webdriver...")
    
    @classmethod
    def teardown_class(cls):
        print("\nteardown_class method : quit webdriver...")
        
    
    def setup_method(self, method):
        print("\nsetup_method : open browser.")
        
    def teardown_method(self, method):
        print("\nteardown_method : close browser.")
        
    def test_case_003(self):
        print("test case 003")
        
    def test_case_004(self):
        print("test case 004")
        
    
 