from pathlib import Path

folderPath = Path(__file__).resolve().parent.parent

class Node:
    def __init__(self , id = '' , children  =''):
        self.id = ''
        self.value = ''


class Graph:
    def __init__(self):
        self.nodes = []

class ReadTranscript:
    def __init__(self):
        for filePath in folderPath.rglob('*.txt'):
           isTranscriptPath = self.getTranscriptPath(filePath)
           if isTranscriptPath:
               print(filePath)
               with filePath.open('r' , encoding="utf-8") as file:
                   content  = file.read()
                   print(content)

    def getTranscriptPath(self, path):
        return str(path.relative_to(folderPath)) == 'transcript.txt'

ReadTranscript()

