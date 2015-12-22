from __future__ import division
import unittest
import bifx

class NAStringTest(unittest.TestCase):

    def test_createFromFile(self):
        self.assertEqual(bifx.NAString(filename="data/testDna.txt"), bifx.NAString("ACTG"))

    def test_nucleotideCount(self):
        self.assertEqual(bifx.NAString("").nucleotideCount("A"), 0)
        self.assertEqual(bifx.NAString("A").nucleotideCount("A"), 1)
        self.assertEqual(bifx.NAString("AA").nucleotideCount("A"), 2)
        self.assertEqual(bifx.NAString("AC").nucleotideCount("A"), 1)
        self.assertEqual(bifx.NAString("ACA").nucleotideCount("A"), 2)
        self.assertEqual(bifx.NAString("").nucleotideCount("C"), 0)
        self.assertEqual(bifx.NAString("C").nucleotideCount("C"), 1)
        self.assertEqual(bifx.NAString("CC").nucleotideCount("C"), 2)
        self.assertEqual(bifx.NAString("AC").nucleotideCount("C"), 1)
        self.assertEqual(bifx.NAString("CAC").nucleotideCount("C"), 2)

        testStr = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

        self.assertEqual(bifx.NAString(testStr).nucleotideCount("A"), 20)
        self.assertEqual(bifx.NAString(testStr).nucleotideCount("C"), 12)
        self.assertEqual(bifx.NAString(testStr).nucleotideCount("G"), 17)
        self.assertEqual(bifx.NAString(testStr).nucleotideCount("T"), 21)

    def test_rnaFromDna(self):
        self.assertEqual(bifx.NAString("").rnaFromDna(), bifx.NAString(""))
        self.assertEqual(bifx.NAString("A").rnaFromDna(), bifx.NAString("A"))
        self.assertEqual(bifx.NAString("T").rnaFromDna(), bifx.NAString("U"))
        self.assertEqual(bifx.NAString("TT").rnaFromDna(), bifx.NAString("UU"))
        self.assertEqual(bifx.NAString("ATAT").rnaFromDna(), bifx.NAString("AUAU"))

        testStr = "GATGGAACTTGACTACGTAAATT"
        expectedStr = "GAUGGAACUUGACUACGUAAAUU"

        self.assertEqual(bifx.NAString(testStr).rnaFromDna(), bifx.NAString(expectedStr))

    def test_equivalence(self):
        self.assertEqual(bifx.NAString(""), bifx.NAString(""))
        self.assertEqual(bifx.NAString("A"), bifx.NAString("A"))
        self.assertNotEqual(bifx.NAString("A"), bifx.NAString(""))

    def test_str(self):
        self.assertEqual(str(bifx.NAString("")), "")
        self.assertEqual(str(bifx.NAString("A")), "A")

    def test_reverseComplement(self):
        self.assertEqual(bifx.NAString("").reverseComplement(), bifx.NAString(""))
        self.assertEqual(bifx.NAString("A").reverseComplement(), bifx.NAString("T"))
        self.assertEqual(bifx.NAString("AT").reverseComplement(), bifx.NAString("AT"))
        
        testStr = "AAAACCCGGT"
        expectedStr = "ACCGGGTTTT"

        self.assertEqual(bifx.NAString(testStr).reverseComplement(), bifx.NAString(expectedStr))

    def test_gcContent(self):
        self.assertAlmostEqual(bifx.NAString("A").gcContent(), 0)
        self.assertAlmostEqual(bifx.NAString("G").gcContent(), 1)
        self.assertAlmostEqual(bifx.NAString("GC").gcContent(), 1)
        self.assertAlmostEqual(bifx.NAString("AG").gcContent(), 0.5)
        self.assertAlmostEqual(bifx.NAString("AGT").gcContent(), 1/3)
        self.assertAlmostEqual(bifx.NAString("AGTA").gcContent(), 0.25)
        self.assertAlmostEqual(bifx.NAString("AGCA").gcContent(), 0.5)

        testStr1 = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
        self.assertAlmostEqual(bifx.NAString(testStr1).gcContent(), 0.5375)

        testStr2 = "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
        self.assertAlmostEqual(bifx.NAString(testStr2).gcContent(), 0.5357142857142857)

        testStr3 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
        self.assertAlmostEqual(bifx.NAString(testStr3).gcContent(), 0.6091954022988506)

    def test_len(self):
        self.assertEqual(len(bifx.NAString("")), 0)
        self.assertEqual(len(bifx.NAString("A")), 1)
        self.assertEqual(len(bifx.NAString("AC")), 2)

if __name__ == '__main__':
    unittest.main()
