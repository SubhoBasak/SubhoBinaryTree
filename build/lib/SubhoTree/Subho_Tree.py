class node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root = None
        self.stack = []

    def add(self, val):
        """
        This func add the val to the binary tree, as we know if the val is greater than the parent node then it will go to the
        the left side of the parent and if the value is smaller than the parent node then it will go to the right side of the
        parent node.

        :param val: type may be integer or node
        :return: (integer) 0, if value added into the root node; 1 if value added into the left side of the parent node; 2 if
        value added into hte right side of the parent node; -1 if value already in the tree.
        """

        if type(val) == node:
            val = val.val
        if type(val) == int:
            pass

        if self.root == None:
            self.root = node(val)
            return 0
        else:
            return self.__add(self.root, val)

    def __add(self, cur_node, val):
        if val < cur_node.val:
            if cur_node.left_child == None:
                cur_node.left_child = node(val)
                return 1
            else:
                return self.__add(cur_node.left_child, val)
        elif val > cur_node.val:
            if cur_node.right_child == None:
                cur_node.right_child = node(val)
                return 2
            else:
                return self.__add(cur_node.right_child, val)
        else:
            return -1

    def show(self, order = 'pre_order'):
        """
        print all the values store in the tree according to the order parameter.

        :param order: {"pre_order", "in_order", "post_order"} (string type)
        :return:
        """
        self.stack = []
        if order == 'pre_order':
            if self.root != None:
                self.__pre_order(self.root)
        elif order == 'in_order':
            if self.root != None:
                self.__in_order(self.root)
        elif order == 'post_order':
            if self.root != None:
                self.__post_order(self.root)
        elif order == 'level_order':
            if self.root != None:
                self.stack.append(self.root)
                self.__level_order(0)
        else:
            raise ValueError('invalid order \"%d\": supported orders are {\"pre_order\", \"in_order\", \"post_order\"}\n'%(order))
        for n in self.stack:
            print(n.val, end = ' ')
        print()

    def __pre_order(self, cur_node):
        self.stack.append(cur_node)
        if cur_node.left_child != None:
            self.__pre_order(cur_node.left_child)
        if cur_node.right_child != None:
            self.__pre_order(cur_node.right_child)

    def __in_order(self, cur_node):
        if cur_node.left_child != None:
            self.__in_order(cur_node.left_child)
        self.stack.append(cur_node)
        if cur_node.righ_child != None:
            self.__in_order(cur_node.righ_child)

    def __post_order(self, cur_node):
        if cur_node.left_child != None:
            self.__post_order(cur_node.left_child)
        if cur_node.right_child != None:
            self.__post_order(cur_node.right_child)
        self.stack.append(cur_node.val)

    def __level_order(self, indx):
        flag = 0
        if self.stack[indx].left_child != None:
            self.stack.append(self.stack[indx].left_child)
            flag = 1
        if self.stack[indx].right_child != None:
            self.stack.append(self.stack[indx].right_child)
            flag = 1
        if flag:
            self.__level_order(indx+1)

    def __add__(self, other):
        if type(other) == int:
            pass
        elif type(other) == node and type(other.val) == int:
            self.add(other.val)
