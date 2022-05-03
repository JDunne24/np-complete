import unittest
from unittest.mock import patch
from io import StringIO

from LongestPathExact import main as exact_longest_path_main
from LongestPathApprox import main as approximation_longest_path_main

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
        cls.t0_exp = """['D', 'E', 'A', 'B', 'C']"""
        
        cls.t1_in = """4
5
2 A B
5 B C
4 B D
7 C D
8 C A"""
        cls.t1_exp = """['A', 'B', 'C', 'D']"""

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
        cls.t2_exp ="""['X', 'B', 'C', 'G', 'H', 'P', 'A', 'Z', 'Y', 'J']""" 

        cls.t3_in ="""26
100
1 A B
5 A C
6 A D
7 A E
10 A F
2 A G
4 A H
6 A I
8 A J
1 A K
2 A L
4 A M
3 A N
9 A O
1 A P
2 A Q
3 A R
7 A S
6 A T
2 A U
1 A V
5 A W
6 A X
7 A Y
10 A Z
2 B A
4 B C
6 B D
8 B E
1 B F
2 B G
4 B H
3 B I
9 B J
1 B K
2 B L
3 B M
7 B N
6 B O
2 B P
1 B Q
5 B R
6 B S
7 B T
10 B U
2 B V
4 B W
6 B X
8 B Y
1 B Z
2 C A
4 C B
3 C D
9 C E
1 C F
2 C G
3 C H
7 C I
6 C J
2 C K
1 C L
5 C M
6 C N
7 C O
10 C P
2 C Q
4 C R
6 C S
8 C T
1 C U
2 C V
4 C W
3 C X
9 C Y
1 C Z
2 D A
3 D B
7 D C
6 D E
2 D F
1 D G
5 D H
6 D I 
7 D J
10 D K
2 D L
4 D M
6 D N
8 D O
1 D P
2 D Q
4 D R
3 D S
9 D T
1 D U
2 D V
3 D W
7 D X
6 D Y
2 D Z"""
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
