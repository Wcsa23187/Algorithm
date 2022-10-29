# 红黑树节点
class RBN(object):
    def __init__(self, data):
        self.data = data  # 数据域
        self.color = 0  # 0红 1黑
        self.left = None
        self.right = None
        self.parent = None


# 红黑树
class RBT(object):
    def __init__(self):
        self.nil = RBN(float('inf'))
        self.root = RBN(float('inf'))
        self.nil.color = 1
        self.list = []

    def treePrint(self):
        self.list=[]
        self.midTraverse(self.root)
        Note = open('LNR.txt', mode='w')
        Note.writelines(self.list)

        self.list = []
        self.firstTraverse(self.root)
        Note = open('NLR.txt', mode='w')
        Note.writelines(self.list)



    # 中序遍历
    def midTraverse(self, x):
        if x == None:
            return
        self.midTraverse(x.left)
        colorStr = ',black\n' if x.color == 1 else ',red\n'
        if x.data != float('inf'):
            m = str(x.data) + colorStr
            self.list.append(m)

        self.midTraverse(x.right)
    # 层次遍历
    def levelTraverse(self):
        x = self.root
        res = []  # 结果
        if x:
            queue = [x]  # 第一层
        else:
            return res

        while len(queue):  # 当下一层没有子节点后停止遍历
            n = len(queue)
            r = []
            for _ in range(n):
                node = queue.pop(0)  # 弹出第一个值
                colorStr = ',black\n' if node.color == 1 else ',red\n'
                if node.data != float('inf'):
                    r.append(str(node.data)+colorStr)
                if node.left:  # 左子树判断
                    queue.append(node.left)
                if node.right:  # 右子树判断
                    queue.append(node.right)
            res.append(r)  # 加入一层的结果

        return res

    # 先序遍历
    def firstTraverse(self, x):
        if x == None:
            return
        colorStr = ',black\n' if x.color == 1 else ',red\n'
        if x.data != float('inf'):
            m = str(x.data) + colorStr
            self.list.append(m)
        self.firstTraverse(x.left)
        self.firstTraverse(x.right)


    # 添加一个节点
    def add(self, x):

        y = self.nil
        root = self.root
        while root.data != float("inf"):
            y = root
            if x.data < root.data:
                root = root.left
            else:
                root = root.right
        x.parent = y

        if y == self.nil:
            self.root = x
        else:
            if x.data < y.data:
                y.left = x
            else:
                y.right = x
        x.left = self.nil
        x.right = self.nil
        x.color = 0
        self.addFix(x)

    # 调整红黑树
    def addFix(self, x):
        # print(x.data)
        # print(x.parent.color)
        # red 0 black 1
        while x.parent.color == 0:
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y.color == 0:
                    print("case1")
                    x.parent.color = 1
                    y.color = 1
                    x.parent.parent.color = 0
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        print("case2")
                        x = x.parent

                        self.rotateLeft(x)
                    print("case3")

                    # print(x.parent.data)
                    x.parent.color = 1
                    x.parent.parent.color = 0
                    self.rotateRight(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y.color == 0:
                    print("case4")
                    x.parent.color = 1
                    y.color = 1
                    x.parent.parent.color = 0
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        print("case5")
                        x = x.parent
                        self.rotateRight(x)
                    print("case6")
                    x.parent.color = 1
                    x.parent.parent.color = 0
                    self.rotateLeft(x.parent.parent)
        self.root.color = 1

    def rotateRight(self, p):

        y = p.left

        p.left = y.right
        if y.right.data != float("inf"):
            y.right.parent = p
        y.parent = p.parent
        if p.parent.data == float("inf"):
            self.root = y
        else:
            if p == p.parent.right:
                p.parent.right = y
            else:
                p.parent.left = y
        y.right = p
        p.parent = y

    # 左旋 p 支点
    def rotateLeft(self, p):
        y = p.right
        p.right = y.left
        if y.left.data != float("inf"):
            y.left.parent = p
        y.parent = p.parent
        if p.parent.data == float("inf"):
            self.root = y
        else:
            if p == p.parent.left:
                p.parent.left = y
            else:
                p.parent.right = y
        y.left = p
        p.parent = y


if __name__ == '__main__':
    rbt = RBT()
    # list = [12, 1, 9, 2, 0, 11, 7, 19, 4, 15, 18, 5, 14, 13, 10, 16, 6, 3, 8, 17]
    with open("insert.txt", "r") as f:
        length = f.readline()
        data = f.readline()
        data = data.split()

    list = []
    for i in range(len(data)):
        list.append(int(data[i]))

    for x in list:
        rbt.add(RBN(x))

    print('=====================================================')
    rbt.treePrint()
    res = rbt.levelTraverse()
    list =[]
    for x in range(len(res)):
        for i in range(len(res[x])):
            list.append(res[x][i])
    Note = open('LOT.txt', mode='w')
    Note.writelines(list)



