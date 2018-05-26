import numpy as np
import pandas as pd
import featureTree as ft


class TreeGenerator(object):

    def __init__(self):
        pass

    def featureToTree(self, data):
        columns = list(data.columns.values)
        columns.remove('diagnosis')
        columns = columns[:10]

        treeRoot = ft.featureTree(data=[])
        print("Tree generating")
        featuresTree = self.generateChild(treeRoot,columns)
        #featuresTree = self.generateChild(treeRoot, ['a','b','c','d'])

        return featuresTree

    def generateChild(self,Node,unUsedColumns):
        children = []
        #print(unUsedColumns)
        for c in unUsedColumns:
            data = Node.data + [c]
            #print(data)
            childNode = ft.featureTree(data=data)
            temp = unUsedColumns[:] #cant use tem =unUsedColumns,lazy python just give temp the pointer to original data
            temp.remove(c)
            if(temp):
                childs = self.generateChild(childNode,temp)
                children.append(childs)
            #print(childs.children)
            #print(len(children))


        Node.children = children
        return Node



