from math import e
from random import randint
import time, graphviz



class Graph(object):
    def __init__(self, n, m, verbose=False) -> None:
        self.n = n
        self.m = m
        self.verbose = verbose
        

    def generate(self)-> float:
        """Generates the current graph
           returns the time taken to generate such graph
        """
        pass

    def add_edge(self,source, dist) -> None:
        """Adds a new Edge to the current Graph"""
        raise NotImplementedError()

    def get_edges(self,) -> list:
        """Returns the edges"""
        raise NotImplementedError()

    def get_vertices(self) ->list:
        """Returns all the vertices"""
        raise NotImplementedError()


    def to_img(self, path):
        """Saves an image of the graph using graphviz"""
        raise NotImplementedError()

    



class GraphA(Graph):

    def __init__(self, n, m, verbose=False) -> None:
        super().__init__(n, m, verbose)
        self.edges = []
        self.vertices = [i for i in range(n)]

    
    def add_edge(self, source, dist) -> None:
        edge = (source, dist)
        if not edge in self.edges: 
            self.edges.append(edge)
    
    def get_edges(self) -> list:
        return list(self.edges)
    
    def get_vertices(self) -> list:
        return list(self.vertices)

    def generate(self)->float:
        start = time.time()
        while len(self.edges) < self.m:
            source, dist = randint(0, self.n - 1), randint(0, self.n - 1)
            if self.verbose: print(f"Adding Edge({source}, {dist})")
            self.add_edge(source, dist)
        gen_time = time.time() - start
        assert len(self.edges) == self.m, AssertionError(f"Number of edges={len(self.edges)} should equals {self.m} ")
        if self.verbose: print(f"Genetated successfully, time = {gen_time}s")
        return gen_time
        


    
        

class GraphAdjList(Graph):

    def __init__(self, n, m, verbose=False) -> None:
        super().__init__(n, m, verbose)
        self.map = {}
        self.counter = 0
    
    def get_vertices(self) -> list:
        return list(self.map.keys())

    def add_edge(self, source, dist) -> None:
        if source in self.map.keys():
            if not dist in self.map[source]:
                self.map[source].append(dist)
        else:
            self.map[source] = [dist]
        self.counter += 1
    def get_edges(self) -> list:
        return [(key, value) for key in self.map.keys() for value in self.map[key] ]

    def _count_edges(self)-> int:
        return sum(list(map(lambda x: len(x), self.map.values())))
    
    def generate(self):
        start = time.time()
        while self.counter  < self.m:
            source, dist = randint(0, self.n - 1), randint(0, self.n - 1)
            if self.verbose: print(f"Adding Edge({source}, {dist})")
            self.add_edge(source, dist)
        gen_time = time.time() - start
        assert self.counter == self.m, AssertionError(f"Number of edges={self.counter} should equals {self.m} ")
        if self.verbose: print(f"Genetated successfully, time = {gen_time}s")
        return gen_time
    
    def to_img(self, filename, dir):
        g = graphviz.Digraph()
        for edge in self.get_edges():
            g.edge(str(edge[0]), str(edge[1]))
        g.render(filename=filename, directory=dir, view=False)
