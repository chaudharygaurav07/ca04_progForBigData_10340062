
import unittest

from CA_04_10340062 import Commit, data,commits

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = data
        self.commits = commits

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))
		
    def test_number_of_commits(self):
         self.assertEqual(422, len(commits))
         

    def test_first_commit(self):
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])   

    
if __name__ == '__main__':
    unittest.main()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        

