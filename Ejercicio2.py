from Estructuras2 import Graph

g = Graph(is_dir=False)

personajes = [
    ("Luke Skywalker", 6),
    ("Darth Vader", 6),
    ("Yoda", 6),
    ("Boba Fett", 3),
    ("C-3PO", 9),
    ("Leia", 6),
    ("Rey", 3),
    ("Kylo Ren", 3),
    ("Chewbacca", 7),
    ("Han Solo", 5),
    ("R2-D2", 9),
    ("BB-8", 3)
]

for nombre, total_episodios in personajes:
    g.add_vertex(nombre, total_episodios)

relaciones = [
    (3, "Luke Skywalker", "Darth Vader"),
    (4, "Luke Skywalker", "Leia"),
    (5, "Luke Skywalker", "R2-D2"),
    (4, "Luke Skywalker", "C-3PO"),
    (3, "Luke Skywalker", "Yoda"),
    (5, "Han Solo", "Chewbacca"),
    (4, "Han Solo", "Leia"),
    (3, "Han Solo", "Luke Skywalker"),
    (9, "C-3PO", "R2-D2"),
    (3, "Rey", "Kylo Ren"),
    (3, "Rey", "BB-8"),
    (3, "Rey", "Chewbacca"),
    (1, "Yoda", "Chewbacca"),
    (2, "Boba Fett", "Darth Vader"),
    (2, "Boba Fett", "Han Solo"),
    (4, "C-3PO", "Leia"),
    (5, "R2-D2", "Leia"),
    (3, "Darth Vader", "Yoda")
]

for peso, origen, destino in relaciones:
    g.add_edge(peso, origen, destino)

print("arbol de expancion minimo")
for nodo_inicio in ["C-3PO", "Yoda", "Leia"]:
    min_tree = g.kruskal(nodo_inicio)
    print(f"\a arbol de expansion minimo desde '{nodo_inicio}'")
    peso_total_mst = 0
    if isinstance(min_tree, str):
        for edge in min_tree.split(';'):
            if '|' in edge:
                orig, dest, w = edge.split('|') 
                print(f"  Origen: {orig} -> Destino: {dest} | Peso (Episodios): {w}")
                peso_total_mst += int(w)
        print(f"Peso total del MST: {peso_total_mst}")
    else:
        print(min_tree)

print("episodios compartidos numero max")
max_episodios = 0
pares_maximos = set()

for vertex in g:
    for edge in vertex.edges:
        if edge.weight > max_episodios:
            max_episodios = edge.weight
            pares_maximos.clear()
        if edge.weight == max_episodios:
            par = tuple(sorted([vertex.value, edge.destination]))
            pares_maximos.add(par)

print(f"el num max de episodios que comparten dos personajes es: {max_episodios}")
print("Pares de personajes que coinciden con este numero:")
for par in pares_maximos:
    print(f"  - {par[0]} y {par[1]}")

rutas_a_calcular = [("C-3PO", "R2-D2"), ("Yoda", "Darth Vader")]

for origen, destino_final in rutas_a_calcular:
    print(f"\nBuscando camino mas corto desde '{origen}' hasta '{destino_final}':")
    if g.exist_path(origen, destino_final):
        paths = g.dijkstra(origen)
        destination = destino_final
        peso_total = None
        camino_completo = []

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == destination:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                destination = value[2]
        
        camino_completo.reverse()
        print(f'El camino más corto es: {" -> ".join(camino_completo)} con un costo total de {peso_total}')
    else:
        print(f"No existe un camino entre {origen} y {destino_final}.")

print("personajes que aparecieron en los 9 nuevos episodios")
print("Personajes:")
for vertex in g:
    if vertex.other_values == 9:
        print(f"  - {vertex.value}")