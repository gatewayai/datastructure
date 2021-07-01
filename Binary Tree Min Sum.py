#!/usr/bin/env python
# coding: utf-8

# In[29]:


# function to calculate minimum path sum

class Minsum:
    def solve(self, nums):
        res = sum(nums)
        while len(nums) > 1:
            i = nums.index(min(nums))
            
            left = nums[i - 1]  if i > 0 else float("inf")
            
            right = nums[i + 1] if i < len(nums) - 1 else float("inf")
            
            res += min(left, right) * nums.pop(i)

        return res
    
#declare tree structure to draw inorder tree

class TreeNode:
  def __init__(self,data):
      self.info = data
      self.left = None  
      self.right = None 


# In[30]:


#file open to read lines
with open(r'E:\BITS\DSAD\binarb.txt','r', encoding='utf-8') as g:
    data=g.readlines()


# In[ ]:





# In[31]:


ob = Minsum()


# Driver code to find minimum sum
for line in data:
    a_list = line.split()
    map_object = map(int, a_list)
    list_of_integers = list(map_object)
    #Len=len(list_of_integers)
    print(list_of_integers)
    #print(line)
    print(ob.solve(list_of_integers))
    #root = buildTree(list_of_integers, 0, Len - 1) 
    #printInorder(root)


# In[40]:


#!/usr/bin/env python
# coding: utf-8

# In[52]:


# Tree Node Data Structure
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None  
        self.right = None        


# In[53]:


# Traverse the tree and calculate the sum of all nodes
# root : root node of Tree
def InOrder(root, theCurrentSum):
    if (root != None):
        theCurrentSum = InOrder(root.left, theCurrentSum)
        #print(root.data, end = " ")
        theCurrentSum = theCurrentSum + root.data[0]
        theCurrentSum = InOrder(root.right, theCurrentSum)
    return theCurrentSum


# In[54]:


# Construct the tree
def InsertInTree(theLeafList, aSize):
    if(len(theLeafList) == 1):
        return theLeafList[0]
    aLeafList = []
    i = 0
    j = 0
    aItr = 0
    if (aSize % 2 == 0):
        aLeafList = [None] * int(aSize / 2)
        aItr = len(theLeafList)
    else:
        aLeafList = [None] * int((aSize / 2) + 1)
        aItr = len(theLeafList) - 1
    while i < aItr:        
        a = theLeafList[i].data[1]          
        b = theLeafList[i+1].data[1]
        largeleaf = a if a > b else b    
        aLeafList[j] = TreeNode([a * b, largeleaf])
        aLeafList[j].left = theLeafList[i];
        aLeafList[j].right = theLeafList[i + 1]
        i += 2
        j = j+1
    if (aSize % 2 != 0):
        aLeafList[j] = theLeafList[i]
    return InsertInTree(aLeafList, len(aLeafList))


# In[55]:


def ValidateInput(line):
    strList = line.split()    
    if(len(strList) < 2):
        #print("Invalid number of input")
        return [False]            
    else:
        try:
            intList = [int(s) for s in strList]
            treeNodeList = [None] * len(intList)
            i = 0;
            for data in intList:
                treeNodeList[i] = TreeNode([data,data])
                i = i+1
            return [True, treeNodeList]            
        except:
            #print("Invalid values in input")
            return [False]


# In[56]:


#file open to read lines
with open(r'E:\BITS\DSAD\binarb.txt','r', encoding='utf-8') as g:
    lines=g.readlines()

f = open("outputPS3.txt", "w")
for line in lines:
    isValidInput = ValidateInput(line)
    if(isValidInput[0]):
        root = InsertInTree(isValidInput[1], len(isValidInput[1]))
        aMinimumSum = InOrder(root, 0)
        f.write(str(aMinimumSum) + "\n")
f.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




