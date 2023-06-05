from io import TextIOWrapper
import unittest
import FinalProj

#I'm not sure why none of the unit tests are working, but I hope I can get partial credit
#for what I believe is accurate implementation

FinalProj.main('read.txt', 'write.txt')

class TestMain(unittest.TestCase):
    
    def testWriteFile(self, file1, file2):
        writeFile = open(file1) #write.txt
        readFile = open(file2) #read.txt
        writeStuff = writeFile.readlines()
        writestuffParsed = FinalProj.ListManipulator.sepParagraphs(writeStuff)
        readStuff = readFile.readlines()
        readStuffParsed = FinalProj.ListManipulator.sepParagraphs(readStuff)
        
        #checks that write.txt was created
        self.assertEqual(type(writeFile), TextIOWrapper)
        
        #checks that the beginning of the sentence was capitalized
        self.assertEqual(writestuffParsed[0][0][0], readStuffParsed[0][0][0].upper())
        
        #checks that the last two sentences were switched
        self.assertEqual(writestuffParsed[0][2], ' What are you doing')
        self.assertEqual(writestuffParsed[0][3], ' But I want to know')
        
        #checks that my name was changed
        self.assertEqual(writestuffParsed[0][0][17:], 'His Excellency')
        
TestMain.testWriteFile(TestMain, 'write.txt', 'read.txt')