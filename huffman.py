import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
        
         # symbol name (character) 
        self.symbol = symbol
        
        self.left = left
        self.right = right
        
         # tree direction (0/1) 
        self.huff = ''
    #This method is used to compare two nodes based on their frequencies. It's used for comparison when adding nodes to the priority queue.
    def __lt__(self, other):
        return self.freq < other.freq

def buildHuffmanTree(chars, freq):
    nodes = []
    
    # converting characters and frequencies into huffman tree nodes 
    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x]))

    while len(nodes) > 1:
        #top most nodes of the minHeap with minimum frequencies
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        
        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1
        
        # combine the 2 smallest nodes to create new node as their parent 
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)

    return nodes[0]

#to print huffman codes for all symbols in the newly created Huffman tree 
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
    
    # if node is not an edge node then traverse inside it 
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    
    # if node is edge node then display its huffman code 
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")


def main():
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [5, 9, 12, 13, 16, 45]
    
    #input_string = input("Enter a string: ")
    #input_string="aabbccccccccdddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffff"

    
    # char_frequency = Counter(input_string) #from collections import Counter 
    # chars = list(char_frequency.keys())
    # freq = [char_frequency[char] for char in chars]
    
    huffmanTree = buildHuffmanTree(chars, freq)
    printNodes(huffmanTree)

if __name__ == "__main__":
    main()
 
