from pathlib import Path

folderPath = Path(__file__).resolve().parent.parent

class Node:
    def __init__(self , value = None , next  = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self ,id = '' , value = ''):
        self.nodes = Node(None)

    def addNode(self, node):
        newNode = Node(node)
        currentNode = self.nodes
        if currentNode.next is None:
            currentNode.next = newNode
        else:
            while currentNode and currentNode.next is None:
                currentNode = currentNode.next
            currentNode = newNode
        return self        


class Transcript:
    def __init__(self):
        self.contents = []
        self.participants = set()
       

    def readAndFormatTheContents(self):
        for filePath in folderPath.rglob('*.txt'):
           isTranscriptPath = self.getTranscriptPath(filePath)
           if isTranscriptPath:
               with filePath.open('r' , encoding="utf-8") as file:
                   contents  = file.read()
                   words = []
                   linkedList = LinkedList()
                   for idx, char in enumerate(contents):
                        if self.isValidChar(char):
                            words.append(char)
                        member = self.getMembers(char , idx , contents)
                        if member not in self.participants:    
                            linkedList.addNode(member)
                        if char == " ": 
                            if len(words):
                                charBuffers = self.getCharChunks(words)
                                self.contents.append(charBuffers)
                                words = []                                
        return self          
                           
    def getCharChunks(self, charStreams):
        return "".join(charStreams)

    def getMembers(self, char, idx , contents):
        member = []
        if char == '\n' or idx == 0:
            start = idx if idx == 0 else idx + 1
            for i in range(start, len(contents)):
                if contents[i] == ':':
                    return "".join(member).strip()
                if contents[i] == '\n':
                    break
                member.append(contents[i])
        return ""


    
    def isValidChar(self, char):
        return (ord(char) >= 97 and ord(char) <= 122)  or (ord(char) >= 65 and  ord(char)  <= 90)      

    def getTranscriptPath(self, path):
        return str(path.relative_to(folderPath)) == 'transcript.txt'


transcript = Transcript()
transcript.readAndFormatTheContents()

