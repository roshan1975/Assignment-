import unittest
import index

class TestStringProcessor(unittest.TestCase):
    def test_reverse(self):
        r1 = index.reverse_word("Knowledge")
        self.assertEqual(r1,"egdelwonK")
        
        r2 = index.reverse_word("Python")
        self.assertEqual(r2,"nohtyP")
        
        r3 = index.reverse_word("World")
        self.assertEqual(r3,"dlroW")
        
        r4 = index.reverse_word("Home")
        self.assertEqual(r4,"emoH")
        
        r5 = index.reverse_word("Check")
        self.assertEqual(r5,"kcehC")
        
    def test_count_vowels(self):
        r1 = index.count_vowels("Ramadan")
        self.assertNotEqual(r1,4)
        
        r2 = index.count_vowels("Education")
        self.assertEqual(r2,5)
        
        r3 = index.count_vowels("Motivation")
        self.assertEqual(r3,5)
        
        r4 = index.count_vowels("Believe")
        self.assertEqual(r4,4)
        
        r5 = index.count_vowels("Discipline")
        self.assertNotEqual(r5,5)
        
    def test_word_count(self):
        r1 = index.word_count("I love Python")
        self.assertNotEqual(r1,1)
        
        r2 = index.word_count("Hi! Python World")
        self.assertEqual(r2,3)
        
        r3 = index.word_count("More Practice")
        self.assertNotEqual(r3,3)
        
        r4 = index.word_count("Eid Ul Fitr")
        self.assertNotEqual(r4,2)
        
        r5 = index.word_count("School Gang")
        self.assertEqual(r5,2)
        
    def test_empty_string(self):
        r1  =index.reverse_word("")
        self.assertNotEqual(r1,"nice")
        
        r2 = index.count_vowels("")
        self.assertNotEqual(r2,1)
        
        r3 = index.word_count("")
        self.assertEqual(r3,0)
        
        r4 = index.reverse_word("")
        self.assertNotEqual(r4,3)
        
        r5 = index.word_count("")
        self.assertNotEqual(r5,2)
        
    def test_uppercase_vowels(self):
        r1 = index.count_vowels("AEIOU")
        self.assertEqual(r1,5)
        
        r2 = index.count_vowels("EDUCATION")
        self.assertNotEqual(r2,4)
        
        r3 = index.count_vowels("ENGLISH")
        self.assertEqual(r3,2)
        
        r4 = index.count_vowels("MATHEMATICS")
        self.assertEqual(r4,4)
        
        r5 = index.count_vowels("MESSI")
        self.assertNotEqual(r5,3)
        
    def test_true(self):
        r1 = index.count_vowels("AEIOU")
        self.assertTrue(r1 == 5)
        
        r2 = index.word_count("Tree Plantation Is Good")
        self.assertTrue(r2 == 4)
        
        r3 = index.count_vowels("Everyone should perform the five daily prayers")
        self.assertTrue(r3 == 15)
        
        r4 = index.reverse_word("Everyone should perform the five daily prayers")
        self.assertTrue(r4 == "sreyarp yliad evif eht mrofrep dluohs enoyrevE")
        
        r5 = index.word_count("Python Learning is Good")
        self.assertTrue(r5 == 4)
        
    def test_False(self):
        r1 = index.count_vowels("Fear")
        self.assertFalse(r1 > 3)
            
        r2 = index.count_vowels("Fire")
        self.assertFalse(r2 > 5)
            
        r3 = index.word_count("Fire Is Dangerous")
        self.assertFalse(r3 > 4)
            
        r4 = index.count_vowels("Tree Plantation")
        self.assertFalse(r4 > 7)
            
        r5 = index.word_count("Tree Plantation")
        self.assertFalse(r5 > 4)
        
    def test_raises(self):
        with self.assertRaises(TypeError):
            index.reverse_word(123)
            
        with self.assertRaises(TypeError):
            index.reverse_word(None)
            
        with self.assertRaises(TypeError):
            index.count_vowels(676)
            
        with self.assertRaises(TypeError):
            index.word_count(None)
            
        with self.assertRaises(TypeError):
            index.word_count(599)
        
if __name__=="__main__":
    unittest.main()


