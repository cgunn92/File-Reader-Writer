
import re

#Here are some things to know: the first is that this will create a new file on the computer
#and the new file will be what is written in.
#second is that I am assuming that all sentences in the output file can end in '.'s regardless of the
#original punctuation
#thirdly I am assuming that paragraphs are present anytime there is a newline between text
#instead of the blank line between text

class TextFileReaderWriter():
    
    def extractText(file):
        read = open(file)
        extraction = read.readlines()
        read.close()
        
        return extraction
    
    def insertText(file, text):
        writer = open(file, 'x')
        writer.write(text)
        writer.close()
        
    
class ListManipulator():
        
        #this separates the elements in the paragraph list into discrete paragraphs
    def sepParagraphs(theList):
        sentences = []
        for x in theList:
            sentences.append(re.split('[.!?]', x))
        
        return sentences
        
        #this removes the \n's from the list
    def removeNewLines(theList):    
        for i in theList:
            i.pop(-1)
            
        return theList
        
        # this loop switches the last 2 sentences in a paragraph with more than 3 sentences
    def switchSentences(theList):
        temp = ''
        for i in theList:
            if len(i) > 3:
                temp = i[-1]
                i[-1] = i[-2]
                i[-2] = temp
                
        
        return theList
        
    def capitalize(theList):
        subString = ''
        for i in theList:
            for j in range(len(i)):
                x = re.findall('\A[a-z]', i[j])
                if x:
                    subString = i[j][0].upper()
                    i[j] = re.sub(i[j][0], subString, i[j])

        
        return theList
        
    def replaceName(theList):
        for i in theList:
            for j in range(len(i)):
                i[j] = re.sub('Caleb Gunn', 'His Excellency', i[j])

        return theList
    
    def insertNewLines(theList):
        if len(theList) > 1:
            for i in theList:
                i.append('\n')
            
        return theList
    
    def listToString(theList):
        theString = ''
        for i in theList:
            theString += '. '.join(i)
            
        return theString
    
    def writeToFile(theString, theFile):
        doStuff = open(theFile, 'x')
        doStuff.write(theString)
        doStuff.close()
        
    def trim(theList):
        for i in theList:
            for j in range(len(i)):
                i[j] = i[j].strip()
            
            
        return theList


def main(file1, file2):
    paragraphs = TextFileReaderWriter.extractText(file1)

    sentences = ListManipulator.sepParagraphs(paragraphs)

    sentences = ListManipulator.removeNewLines(sentences)

    sentences = ListManipulator.switchSentences(sentences)

    sentences = ListManipulator.trim(sentences)

    sentences = ListManipulator.capitalize(sentences)
      
    sentences = ListManipulator.replaceName(sentences)
        
    sentences = ListManipulator.insertNewLines(sentences)
        
    finalString = ListManipulator.listToString(sentences)

    TextFileReaderWriter.insertText(file2, finalString)
    
    
main('read.txt', 'writes.txt')