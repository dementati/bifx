import unittest
import bifx

class FASTALoaderTest(unittest.TestCase):
    
    def test_load_emptyString(self):
        loader = bifx.FASTALoader()
        self.assertEqual(len(loader.load("")), 0)

    def test_load_emptyFile(self):
        loader = bifx.FASTALoader()
        self.assertEqual(len(loader.load(filename="data/empty.txt")), 0)

    def test_load_testFile(self):
        loader = bifx.FASTALoader()
        NAs = loader.load(filename="data/testFasta.txt")
        self.assertEqual(len(NAs), 3)
        self.assertEquals(NAs[0].descriptor, "test1")
        self.assertEquals(NAs[0].string, "")
        self.assertEquals(NAs[1].descriptor, "test2")
        self.assertEquals(NAs[1].string, "ACTG")
        self.assertEquals(NAs[2].descriptor, "test3")
        self.assertEquals(NAs[2].string, "")

    def test_load_singleEmptyNA(self):
        loader = bifx.FASTALoader()

        NAs = loader.load(">\n")

        self.assertEqual(len(NAs), 1)
        self.assertEqual(NAs[0].descriptor, "")
        self.assertEqual(NAs[0].string, "")

    def test_load_singleEmptyNAMultiline(self):
        loader = bifx.FASTALoader()

        NAs = loader.load(">\n\n")

        self.assertEqual(len(NAs), 1)
        self.assertEqual(NAs[0].descriptor, "")
        self.assertEqual(NAs[0].string, "")

    def test_load_singleEmptyNAMultilineWindows(self):
        loader = bifx.FASTALoader()

        NAs = loader.load(">\r\n\r\n\r\n")

        self.assertEqual(len(NAs), 1)
        self.assertEqual(NAs[0].descriptor, "")
        self.assertEqual(NAs[0].string, "")

    def test_load_singleEmptyNAWindows(self):
        loader = bifx.FASTALoader()

        NAs = loader.load(">\r\n")

        self.assertEqual(len(NAs), 1)
        self.assertEqual(NAs[0].descriptor, "")
        self.assertEqual(NAs[0].string, "")

    def test_load_singleNADesc(self):
        loader = bifx.FASTALoader()

        NAs = loader.load(">test\n")

        self.assertEqual(len(NAs), 1)
        self.assertEqual(NAs[0].descriptor, "test")

    def test_load_singleNAString(self):
        loader = bifx.FASTALoader()

        NAs = loader.load(">\nA")

        self.assertEqual(len(NAs), 1)
        self.assertEqual(NAs[0].string, "A")

    def test_load_twoLineNAString(self):
        loader = bifx.FASTALoader()

        NAs = loader.load(">\nA\nT")

        self.assertEqual(len(NAs), 1)
        self.assertEqual(NAs[0].string, "AT")

    def test_load_twoNAs(self):
        loader = bifx.FASTALoader()

        NAs = loader.load(">test1\nA\n>test2\nT")

        self.assertEqual(len(NAs), 2)
        self.assertEqual(NAs[0].descriptor, "test1")
        self.assertEqual(NAs[0].string, "A")
        self.assertEqual(NAs[1].descriptor, "test2")
        self.assertEqual(NAs[1].string, "T")

    def test_load_testFile2(self):
        loader = bifx.FASTALoader()
        NAs = loader.load(filename="data/testFasta2.txt")
        self.assertEqual(len(NAs), 3)
        self.assertEqual(NAs[0].descriptor, "Rosalind_6404")
        self.assertEqual(NAs[0].string, "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG")
        self.assertEqual(NAs[1].descriptor, "Rosalind_5959")
        self.assertEqual(NAs[1].string, "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC")
        self.assertEqual(NAs[2].descriptor, "Rosalind_0808")
        self.assertEqual(NAs[2].string, "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")

    def test_load_testFile3(self):
        loader = bifx.FASTALoader()
        NAs = loader.load(filename="data/testFasta3.txt")
        self.assertEqual(len(NAs), 1)

if __name__ == '__main__':
    unittest.main()
