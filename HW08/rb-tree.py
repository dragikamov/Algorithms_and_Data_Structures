class Node:

  def __init__(self, key, color = True):
    self.color = color
    self.key = key
    self.left = self.right = self.parent = NilNode.instance()
    
  def __str__(self):
    if self.color==True:
      s = str(self.key) + "R"
    else:
      s = str(self.key) + "B"
    if self.left:
      s = s + " " + "L" + self.left.__str__()
    if self.right:
      s = s + " " + "R" + self.right.__str__()
    return s

  def __bool__(self):
    return True


class NilNode(Node):
  __instance__ = None

  @classmethod
  def instance(self):
    if self.__instance__ is None:
      self.__instance__ = NilNode()
    return self.__instance__

  def __init__(self):
    self.color = False
    self.key = None
    self.left = self.right = self.parent = None

  def __bool__(self):
    return False

class RedBlackTree:
  
  def __init__(self):
    self.root = NilNode.instance()
    self.size = 0
    
  def __str__(self):
    return ("\n(root.size = %d)\n" % self.size)  + str(self.root)

  def insert(self, key):
    self.add(Node(key))
    
  def add(self, x):
    self.__insert_helper(x)
    x.color = True
    while x != self.root and x.parent.color == True:
      if x.parent == x.parent.parent.left:
        y = x.parent.parent.right
        if y and y.color == True:
          x.parent.color = False
          y.color = False
          x.parent.parent.color = True
          x = x.parent.parent
        else:
          if x == x.parent.right:
            x = x.parent
            self.rotateLeft(x)
          x.parent.color = False
          x.parent.parent.color = True
          self.rotateRight(x.parent.parent)
      else:
        y = x.parent.parent.left
        if y and y.color == True:
          x.parent.color = False
          y.color = False
          x.parent.parent.color = True
          x = x.parent.parent
        else:
          if x == x.parent.left:
            x = x.parent
            self.rotateRight(x)
          x.parent.color = False
          x.parent.parent.color = True
          self.rotateLeft(x.parent.parent)
    self.root.color = False

  def delete(self, z):
    if not z.left or not z.right:
      y = z
    else:
      y = self.successor(z)
    if not y.left:
      x = y.right
    else:
      x = y.left
    x.parent = y.parent

    if not y.parent:
      self.root = x
    else:
      if y == y.parent.left:
        y.parent.left = x
      else:
        y.parent.right = x

    if y != z: z.key = y.key

    if y.color == False:
      self.__delete_fixup(x)

    self.size -= 1
    return y

  def getMinimum(self, x = None):
    if x is None: x = self.root
    while x.left:
      x = x.left
    return x

  def getMaximum(self, x = None):
    if x is None: x = self.root
    while x.right:
      x = x.right
    return x

  def successor(self, x):
    if x.right:
      return self.minimum(x.right)
    y = x.parent
    while y and x == y.right:
      x = y
      y = y.parent
    return y

  def predecessor(self, x):
    if x.left:
      return self.maximum(x.left)
    y = x.parent
    while y and x == y.left:
      x = y
      y = y.parent
    return y

  def search(self, key, x = None):
    if x is None: x = self.root
    while x and x.key != key:
      if key < x.key:
        x = x.left
      else:
        x = x.right
    return x

  def is_empty(self):
    return bool(self.root)

  def black_height(self, x = None):
    if x is None: x = self.root
    height = 0
    while x:
      x = x.left
      if not x or x.is_black():
        height += 1
    return height

  def rotateLeft(self, x):
    y = x.right
    x.right = y.left
    if y.left: y.left.parent = x
    y.parent = x.parent
    if not x.parent:
      self.root = y
    else:
      if x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
    y.left = x
    x.parent = y

  def rotateRight(self, x):
    y = x.left
    x.left = y.right
    if y.right: y.right.parent = x
    y.parent = x.parent
    if not x.parent:
      self.root = y
    else:
      if x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
    y.right = x
    x.parent = y

  def __insert_helper(self, z):
    y = NilNode.instance()
    x = self.root
    while x:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    
    z.parent = y
    if not y:
      self.root = z
    else:
      if z.key < y.key:
        y.left = z
      else:
        y.right = z
    
    self.size += 1

  def __delete_fixup(self, x):
    while x != self.root and x.color == False:
      if x == x.parent.left:
        w = x.parent.right
        if w.color == True:
          w.color = False
          x.parent.color = True
          self.rotateLeft(x.parent)
          w = x.parent.right
        if w.left.color == False and w.right.color == False:
          w.color = True
          x = x.parent
        else:
          if w.right.color == False:
            w.left.color = False
            w.color = True
            self.rotateRight(w)
            w = x.parent.right
          w.color = x.parent.color
          x.parent.color = False
          w.right.color = False
          self.rotateLeft(x.parent)
          x = self.root
      else:
        w = x.parent.left
        if w.color == True:
          w.color = False
          x.parent.color = True
          self.rotateRight(x.parent)
          w = x.parent.left
        if w.right.color == False and w.left.color == False:
          w.color = True
          x = x.parent
        else:
          if w.left.color == False:
            w.right.color = False
            w.color = True
            self.rotateLeft(w)
            w = x.parent.left
          w.color = x.parent.color
          x.parent.color = False
          w.left.color = False
          self.rotateRight(x.parent)
          x = root
    x.color = False

def main():
  import random
  tree = RedBlackTree()
  l=[14, 42, 35, 7, 26, 17]
  print("List: ",l)
  random.shuffle(l)
  print("Shuffled list: ",l)
  for i in range(6):
    tree.insert(l[i])

  print(tree)

main()
