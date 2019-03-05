import networkx as nx

##################### TETRAHEDRON #####################

## (x,y)-coordinates for a Schlegel Diagram ##
pos_tetrahedron = {0: (0.8660254037844387, -0.49999999999999983), 1: (6.123233995736766e-17, 1.0), 2: (-0.8660254037844388, -0.4999999999999997), 3: (0.0, 1.6653345369377348e-16)}

edges_tetrahedron = [(0,1), (0,2), (0,3), 
                      (1,2), (1,3), (2,3)]

tetrahedron = nx.Graph()
tetrahedron.add_nodes_from(pos_tetrahedron.keys())
tetrahedron.add_edges_from(edges_tetrahedron)


#####################  CUBE  #####################

## (x,y)-coordinates for a Schlegel Diagram ##
cube_points = [(0,0), (0,3), (3,3), (3,0),
              (1,1), (1,2), (2,2), (2,1)]

## Cube-edge (a,b) connects cube_points[a] to cube_points[b] ##
edges_cube = [(0,4),(1,5),(2,6),(3,7),
             (0,1),(1,2),(2,3),(3,0),
             (4,5), (5,6), (6,7), (7,4)]

## Map integer node labels to (x,y)-coordinates ##
pos_cube = dict((node,point) for node, point in enumerate(cube_points))

## Constructing a cube graph from the cube_points and cube_edges ##
cube = nx.Graph()
cube.add_nodes_from(pos_cube.keys())
cube.add_edges_from(edges_cube)


#####################  OCTAHEDRON  #####################

## (x,y)-coordinates for a Schlegel Diagram ##
octahedron_points = [(0,0), (0.5,1), (1,0),
                    (0.5,0.2), (0.4,0.5), (0.6,0.5)]

## Octahedron-edge (a,b) connects octahedron_points[a] to octahedron_points[b] ##
edges_octahedron = [(0,1), (1,2), (2,0),
                   (3,4), (4,5), (5,3),
                   (0,3), (0,4),
                   (1,4), (1,5),
                   (2,3), (3,5),(2,5)]


pos_octahedron = dict((node,point) for node, point in enumerate(octahedron_points))

## Constructing an octahedron graph from the octahedron_points and octahedron_edges ##
octahedron = nx.Graph()
octahedron.add_nodes_from(pos_octahedron.keys())
octahedron.add_edges_from(edges_octahedron)


#####################   DODECAHEDRON   #####################

## (x,y)-coordinates for a Schlegel Diagram ###
pos_dodecahedron = {0: (1.1888206453689418, 0.38627124296868426), 1: (7.654042494670958e-17, 1.25), 2: (-1.1888206453689418, 0.38627124296868437), 3: (-0.7347315653655916, -1.011271242968684), 4: (0.7347315653655911, -1.0112712429686845), 5: (0.7132923872213651, 0.23176274578121053), 6: (4.592425496802574e-17, 0.75), 7: (-0.7132923872213651, 0.23176274578121064), 8: (-0.4408389392193549, -0.6067627457812105), 9: (0.4408389392193547, -0.6067627457812107), 10: (-0.4755282581475768, -0.15450849718747364), 11: (-9.184850993605148e-17, -0.5), 12: (0.47552825814757677, -0.1545084971874738), 13: (0.2938926261462367, 0.4045084971874736), 14: (-0.29389262614623646, 0.40450849718747384), 15: (-0.2377641290737884, -0.07725424859373682), 16: (-4.592425496802574e-17, -0.25), 17: (0.23776412907378838, -0.0772542485937369), 18: (0.14694631307311834, 0.2022542485937368), 19: (-0.14694631307311823, 0.20225424859373692)}

edges_dodecahedron = [(0,1), (1,2), (2,3), (3,4), (4,0),
                     (0,5), (1,6), (2,7), (3,8), (4,9),
                     (6,14), (14,7), (7,10), (10,8), (8,11),
                     (11,9), (9,12), (12,5), (5,13), (13,6),
                     (10,15), (11,16), (12,17), (13,18), (14,19),
                     (15,16), (16,17), (17,18), (18,19), (19,15)]

dodecahedron = nx.Graph()
dodecahedron.add_nodes_from(pos_dodecahedron.keys())
dodecahedron.add_edges_from(edges_dodecahedron)


#####################   ICOSAHEDRON   #####################

## (x,y)-coordinates for a Schlegel Diagram ###
pos_icosahedron = {0: (1.7320508075688774, -0.9999999999999997), 1: (1.2246467991473532e-16, 2.0), 2: (-1.7320508075688776, -0.9999999999999994), 3: (-0.1299038105676658, 0.32499999999999996), 4: (-2.7554552980815445e-17, 0.1), 5: (0.12990381056766584, 0.3249999999999999), 6: (0.4330127018922193, 0.5), 7: (3.061616997868383e-17, 0.75), 8: (-0.43301270189221924, 0.5000000000000002), 9: (-0.4330127018922193, -5.551115123125783e-17), 10: (-9.184850993605148e-17, -0.25), 11: (0.4330127018922194, 1.6653345369377348e-16)}

edges_icosahedron = [(0,1), (1,2), (2,0),
                     (3,4), (4,5), (5,3),
                    (0,6), (0,11), (0,10),
                    (1,6), (1,7), (1,8),
                    (2,8), (2,9), (2,10),
                    (6,7), (7,8), (8,9),
                    (9,10), (10,11), (11,6),
                    (3,7), (3,8), (3,9),
                    (4,9), (4,10), (4,11),
                    (5,11), (5,6), (5,7)]

icosahedron = nx.Graph()
icosahedron.add_nodes_from(pos_icosahedron.keys())
icosahedron.add_edges_from(edges_icosahedron)