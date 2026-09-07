from pathlib import Path

folderPath = Path(__file__).resolve().parent.parent


class Node:
    def __init__(self ,id ='' ) -> None:
        self.id = id
        self.turns = []
        self.lines = [] # actual lines in transcript for debugging

    def __repr__(self):
        return f"Node({self.id!r}, turns={self.turns}, lines={self.lines})"

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.prevNode = None

    def addNodeAndEdge(self, adjacentNode , turn , line ):
        if adjacentNode in self.nodes:
            self.nodes[adjacentNode].turns.append(turn)
            self.nodes[adjacentNode].lines.append(line)
            if adjacentNode in  self.edges[self.prevNode]:
                self.edges[self.prevNode][adjacentNode] += 1
            else:
                self.edges[self.prevNode][adjacentNode] = 1    
            self.prevNode = adjacentNode    
        else:
            self.prevNode = adjacentNode
            self.nodes[adjacentNode] = Node(adjacentNode)
            self.edges[self.prevNode] = {}
        return self

    def __repr__(self):
        rows = [f"Graph with {len(self.nodes)} nodes"]
        for name, node in self.nodes.items():
            rows.append(f"  {name}: {len(node.turns)} turns at offsets {node.turns}")
        rows.append("edges:")
        for src, targets in self.edges.items():
            for dst, weight in targets.items():
                rows.append(f"  {src} -> {dst} (x{weight})")
        return "\n".join(rows)


class Transcript:
    def __init__(self):
        self.contents = []
        self.graph = Graph()
       

    def readAndFormatTheContents(self):
        for filePath in folderPath.rglob('*.txt'):
           isTranscriptPath = self.getTranscriptPath(filePath)
           if isTranscriptPath:
               with filePath.open('r' , encoding="utf-8") as file:
                   contents  = file.read()
                   words = []
                   graph = self.graph
                   for idx, char in enumerate(contents):
                        if self.isValidChar(char):
                            words.append(char)
                        [member , turn , line] = self.getMembers(char , idx , contents)
                        if member:
                            graph.addNodeAndEdge(member , turn , line)
                        if char == " ": 
                            if len(words):
                                charBuffers = self.getCharChunks(words)
                                self.contents.append(charBuffers)
                                words = []                                
        return self          
                           
    def getCharChunks(self, charStreams):
        return "".join(charStreams)

    def getMembers(self, char, idx , contents):
        members = []
        if char == '\n' or idx == 0:
            start = idx if idx == 0 else idx + 1
            for i in range(start, len(contents)):
                if contents[i] == ':':
                    member = "".join(members).strip()
                    return [member , start , i ]
                if contents[i] == '\n':
                    break
                members.append(contents[i])
        return ["" , 0 , 0]


    
    def isValidChar(self, char):
        return (ord(char) >= 97 and ord(char) <= 122)  or (ord(char) >= 65 and  ord(char)  <= 90)      

    def getTranscriptPath(self, path):
        return str(path.relative_to(folderPath)) == 'transcript.txt'


transcript = Transcript()
transcript.readAndFormatTheContents()

print(transcript.graph)
print()
print("words:", transcript.contents)


