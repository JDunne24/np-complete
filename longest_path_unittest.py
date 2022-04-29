import unittest
from unittest.mock import patch

from placeholderfilename import main as longest_path_main

class TestLongestPath(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.file_a_ok = False
        cls.t0_in =
        cls.t0_exp =
        
        cls.t1_in =
        cls.t1_exp =
        cls.t2_in = 
        cls.t2_exp = 

    @weight(0)
    @number("1.2")
    def test_01(self):
        """Check file cs412_hw0_a does not contain a dictionary"""

        dict_char = False
        with open('cs412_hw0_a.py') as f:
            if '{' in f.read():
                dict_char = True

        with open('cs412_hw0_a.py') as f:
            if 'dict()' in f.read():
                dict_char = True

        self.assertEqual(False, dict_char, 
                          'Appears that a dictionary is used in cs412_hw0_a.py')
        
        # test OK, set status to good/true
        TestHW1.file_a_ok = True