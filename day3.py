def part1(input):
    temp = [0]*12
    for num in input:
        for i in range(len(num)):
            if int(num[i]) == 1:
                temp[i] += 1
            else:
                temp[i] -= 1
    for i in range(len(temp)):
        if temp[i] > 0:
            temp[i] = 1
        else:
            temp[i] = 0
    gamma = ""
    epsilon = ""
    for i in range(len(temp)):
        gamma += str(temp[i])
        if temp[i] == 1:
            epsilon += "0"
        else:
            epsilon += "1"
    
    
    result = int(gamma, base=2) * int(epsilon, base=2)
    return gamma, epsilon, result
    

class TreeNode:
    def __init__(self, data):
        self.data = data
        # We only create a node the first time we see it, so the inital value
        # is set to one sighting.
        self.weight = 1
        self.leftChild = None
        self.rightChild = None
    
    def increment(self):
        self.weight += 1
        
    def printTree(self):
        if self.left:
            self.left.printTree()
        print("(b"+str(self.data)+",w"+str(self.weight)+")"),
        if self.right:
            self.right.printTree()

def part2(input):
    oxygenRating = ""
    co2Rating = ""
    """
    This solution gives the answer with a single pass of the input file.
    We do this by creating a simple tree with weights + values, where the 
    values are the binary digits and the weights are the # of times we have seen
    the value in that position. With this we can get all possible permutations
    stored in one data structure.
    
    For example, there are only two permutations of a 1-digit binary number, 
    0 and 1. This is an easy tree to make - a default root node and the two options
    beneath it. There are 4 permutations of a 2-digit binary number, 00 01 10 10.
    This can be stored as a tree with 5 nodes.
         r
       /  \
      0    1 
     / \  / \
    0  1 0  1
    
    For the solution to part 2, you can simply follow the highest/lowest weight
    at each node.
    """ 
    root = TreeNode("DefaultNumber")                        # Start tree with a non 0 or 1 (throwaway node)
    for num in input:                                       # Scan through every number in our input list
        depthTracker = root                                 # Start at the top of the tree (don't know if we have a 0 or 1 yet)
        for i in range(len(num)):                           # For every bit in this record:
            if int(num[i]) == 0:                            # Check if it is a 0 or 1
                if depthTracker.leftChild == None:          # If we have never seen a child permutation with this value, create a child
                    depthTracker.leftChild = TreeNode(0)    # Create a child node (new nodes automatically get a weight of 1)
                    depthTracker = depthTracker.leftChild   # move one level deeper in the tree
                else:
                    depthTracker.leftChild.weight += 1      # If we *have* seen this before, increment the weight
                    depthTracker = depthTracker.leftChild   # move one level deeper in the tree
            else:                                           # Repeat for 1's
                if depthTracker.rightChild == None:
                    depthTracker.rightChild = TreeNode(1)
                    depthTracker = depthTracker.rightChild
                else:
                    depthTracker.rightChild.weight += 1
                    depthTracker = depthTracker.rightChild


    # 02 rating rules: find where weight of 1 (right subtree) >= weight of 0
    depthTracker = root
    for i in range(len(num)):
        if depthTracker.leftChild == None:
            oxygenRating += str(depthTracker.rightChild.data)
            depthTracker = depthTracker.rightChild
        elif depthTracker.rightChild == None:
            oxygenRating += str(depthTracker.leftChild.data)
            depthTracker = depthTracker.leftChild
        elif depthTracker.leftChild.weight > depthTracker.rightChild.weight:
            oxygenRating += str(depthTracker.leftChild.data)
            depthTracker = depthTracker.leftChild
        elif depthTracker.leftChild.weight == depthTracker.rightChild.weight:
            oxygenRating += str(depthTracker.rightChild.data)
            depthTracker = depthTracker.rightChild
        else:
            oxygenRating += str(depthTracker.rightChild.data)
            depthTracker = depthTracker.rightChild
    
    # C02 rating rules: find where weight of 0 >= weight of 1
    depthTracker = root
    for i in range(len(num)):
        if depthTracker.leftChild == None:
            co2Rating += str(depthTracker.rightChild.data)
            depthTracker = depthTracker.rightChild
        elif depthTracker.rightChild == None:
            co2Rating += str(depthTracker.leftChild.data)
            depthTracker = depthTracker.leftChild
        elif depthTracker.leftChild.weight < depthTracker.rightChild.weight:
            co2Rating += str(depthTracker.leftChild.data)
            depthTracker = depthTracker.leftChild
        elif depthTracker.leftChild.weight == depthTracker.rightChild.weight:
            co2Rating += str(depthTracker.leftChild.data)
            depthTracker = depthTracker.leftChild
        else:
            co2Rating += str(depthTracker.rightChild.data)
            depthTracker = depthTracker.rightChild
    
    return int(oxygenRating, base=2), int(co2Rating, base=2), int(oxygenRating, base=2) * int(co2Rating, base=2)

if __name__ == '__main__':
    i=list(open("3.txt").read().splitlines())
    print(part1(i))
    print(part2(i))