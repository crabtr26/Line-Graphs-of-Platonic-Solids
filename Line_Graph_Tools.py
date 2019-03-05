import networkx as nx
import numpy as np

def my_line_graph(G, pos):
    
    LG_points = []
    LG_edges = []
    for i,edge in enumerate(G.edges):
        end1 = edge[0] 
        end2 = edge[1] 
        LG_points.append(tuple((np.array(pos[end1]) + np.array(pos[end2]))/2))
        for j,e in enumerate(G.edges):
            if j != i:
                if e[0] in edge or e[1] in edge:
                    LG_edges.append((i,j))

    LG_pos = dict((node, tuple(point)) for node,point in enumerate(LG_points))
    LG = nx.Graph()
    LG.add_nodes_from(LG_pos.keys())
    LG.add_edges_from(LG_edges)
    
    return LG, LG_pos

def get_polygon_coordinates(n, A=1, theta = 0, xshift = 0, yshift = 0):
    
    coordinates = []
    for i in range(0, n):
        
        shift = theta + (np.pi / 2) - (2 * np.pi) / n 
        angle = ( (2 * i * np.pi) / n ) + shift
        x = A*np.cos(angle) + xshift
        y = A*np.sin(angle) + yshift
        coordinates.append((x,y))
        
    return coordinates

def poly_graph(n):

    pos = dict(enumerate(get_polygon_coordinates(n)))
    edges = list(zip(range(0,n-1), list(range(1,n)))) + [(n-1,0)]
    G = nx.Graph()
    G.add_nodes_from(pos.keys())
    G.add_edges_from(edges)
    
    return G, pos
