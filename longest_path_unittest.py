import unittest
from unittest.mock import patch
from io import StringIO

from placeholderfilename import main as exact_longest_path_main
from placeholderfilename2 import main as approximation_longest_path_main

class TestLongestPath(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):

        cls.t0_in = """5
6
1 A B
6 A D
5 B C
1 C D
2 D E
3 E A"""
        cls.t0_exp =
        
        cls.t1_in = """4
5
2 A B
5 B C
4 B D
7 C D
8 C A"""
        cls.t1_exp =

        cls.t2_in ="""15
20
1 A B
5 B C
6 H P
7 P A
10 G H
2 Z G
4 A Z
6 Z C
8 P B
1 B R
2 R C
4 Z R
3 R A
9 C G
1 G A
2 Z X
3 X B
7 X G
6 Z Y
2 Y C""" 
        cls.t2_exp = 

        cls.t3_in =
        cls.t3_exp = 

    @patch('sys.stdout', new_callable=StringIO)
    def testshort(self, mock_out):

        with patch('sys.stdin', new = StringIO(self.t0_in)):
            exact_longest_path_main()
        self.assertEqual(mock_out.getvalue(), self.t0_exp)

        with patch('sys.stdin', new = StringIO(self.t0_in)):
            approximation_longest_path_main()
        self.assertEqual(mock_out.getvalue(), self.t0_exp)

    @patch('sys.stdout', new_callable=StringIO)
    def testlong(self, mock_out):

        with patch('sys.stdin', new = StringIO(self.t1_in)):
            exact_longest_path_main()
        self.assertEqual(mock_out.getvalue(), self.t1_exp)

        with patch('sys.stdin', new = StringIO(self.t1_in)):
            approximation_longest_path_main()
        self.assertEqual(mock_out.getvalue(), self.t1_exp)

    @patch('sys.stdout', new_callable=StringIO)
    def testmedium(self, mock_out):

        with patch('sys.stdin', new = StringIO(self.t2_in)):
            exact_longest_path_main()
        self.assertEqual(mock_out.getvalue(), self.t2_exp)

        with patch('sys.stdin', new = StringIO(self.t2_in)):
            approximation_longest_path_main()
        self.assertEqual(mock_out.getvalue(), self.t2_exp)

    @patch('sys.stdout', new_callable=StringIO)
    def testlong(self, mock_out):

        with patch('sys.stdin', new = StringIO(self.t3_in)):
            exact_longest_path_main()
        self.assertEqual(mock_out.getvalue(), self.t3_exp)

        with patch('sys.stdin', new = StringIO(self.t3_in)):
            approximation_longest_path_main()
        self.assertEqual(mock_out.getvalue(), self.t3_exp)
