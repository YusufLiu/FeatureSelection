import cancerModel as cm

class featureTree:

    def __init__(self,children=[],data=[]):
        self.children = children
        self.data = data

    def getChildren(self):
        result = []
        for i in self.children:
            result.append(i.data)
        return result

    def bfs(self, graph,data):
        features = []
        score = []
        visited, queue = set(),[]
        for i in graph.children:
            queue.append(i)

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(vertex.children)
                columns = vertex.data
                columns.append('diagnosis')
                cancerData = data[columns]
                result = cm.LogesticRegression(cancerData) * 100
                if(65 < result):
                    features.append(vertex.data)
                    score.append(result)




        return features,score