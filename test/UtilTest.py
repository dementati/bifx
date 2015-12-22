import unittest
import bifx
import re

class UtilTest(unittest.TestCase):

    def test_findAllSubstrings(self):
        self.assertEqual(bifx.findAllSubstrings("", ""), [1])
        self.assertEqual(bifx.findAllSubstrings("A", ""), [])
        self.assertEqual(bifx.findAllSubstrings("", "A"), [1, 2])
        self.assertEqual(bifx.findAllSubstrings("A", "A"), [1])
        self.assertEqual(bifx.findAllSubstrings("AA", "AA"), [1])
        self.assertEqual(bifx.findAllSubstrings("AT", "ATAT"), [1, 3])
        self.assertEqual(bifx.findAllSubstrings("ATAT", "GATATATGCATATACTT"), [2, 4, 10])

    def test_findAllReversePalindromes(self):
        self.assertEqual(bifx.findAllReversePalindromes(bifx.NAString("")), [])
        self.assertEqual(bifx.findAllReversePalindromes(bifx.NAString("GC")), [(1, 2)])
        self.assertEqual(bifx.findAllReversePalindromes(bifx.NAString("AT")), [(1, 2)])
        self.assertEqual(bifx.findAllReversePalindromes(bifx.NAString("GCATGC"), 6, 6), [(1, 6)])

        testStr = "TCAATGCATGCGGGTCTATATGCAT"
        expectedResult = [
            (4, 6),
            (5, 4),
            (6, 6),
            (7, 4),
            (17, 4),
            (18, 4),
            (20, 6),
            (21, 4)
        ]
        self.assertEqual(set(bifx.findAllReversePalindromes(bifx.NAString(testStr), 4, 12)), set(expectedResult))

if __name__ == '__main__':
    unittest.main()
