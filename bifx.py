import sys
import re

complement = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}

def findAllSubstrings(substring, string):
    return [m.start() + 1 for m in re.finditer("(?=%s)" % substring, string)]

def findAllReversePalindromes(naString, minLength=1, maxLength=10):
    result = []
    for palindromeLength in range(minLength, maxLength+1):
        for i in range(len(naString)):
            if i + palindromeLength > len(naString):
                continue

            subNA = NAString(naString.string[i:i+palindromeLength])

            if subNA == subNA.reverseComplement():
                result.append((i+1, palindromeLength))

    return result

class NAString:
    
    def __init__(self, string="", filename=None):
        if filename != None:
            with open(filename) as f:
                self.string = f.read().strip()
        else:
            self.string = string

    def __eq__(self, other):
        return self.string == other.string

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    def nucleotideCount(self, nucleotide):
        return self.string.count(nucleotide)

    def rnaFromDna(self):
        return NAString(self.string.replace("T", "U"))

    def reverseComplement(self):
        return NAString("".join(reversed(map(lambda c: complement[c], self.string))))

    def gcContent(self):
        gc = sum([x in ["G", "C"] for x in self.string])
        return float(gc)/float(len(self.string))

class FASTALoader:

    def load(self, fastaString=None, filename=None):
        if filename != None:
            with open(filename) as f:
                fastaString = f.read()

        result = []
        for string in fastaString.split(">")[1:]:
            parts = re.split("\n|\r\n", string, 1)
            na = "".join(re.split("\n|\r\n", parts[1]))
            naString = NAString(na)
            naString.descriptor = parts[0]
            result.append(naString)

        return result

