import snap


class RandomGraphGenerator:

    def __init__(self, num_nodes, num_edges):
        self.graph = snap.GenRndGnm(snap.PUNGraph, num_nodes, num_edges)

    def retrieve_random_graph(self) -> snap.PUNGraph:
        return self.graph
