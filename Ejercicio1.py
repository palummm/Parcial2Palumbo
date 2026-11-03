from Estructuras1 import BinaryTree, Queue
from ListaPokemons import pokemons

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for p in pokemons:
    arbol_nombre.insert_node(p.name, p)
    arbol_numero.insert_node(p.number, p)
    for tipo in p.types:
        arbol_tipo.insert_node(tipo, p)

print("datos del pokemon con numero1")
nodo_buscado = arbol_numero.search(1)
if nodo_buscado is not None:
    print(nodo_buscado.other_values)
else:
    print("No encontrado")

print("buqueda por porximidad de nombre, bul")
def buscar_por_proximidad(root, prefix):
    if root is not None:
        buscar_por_proximidad(root.left, prefix)
        if prefix.lower() in root.value.lower():
            print(root.other_values)
        buscar_por_proximidad(root.right, prefix)
buscar_por_proximidad(arbol_nombre.root, "bul")

print("nombres por tipos especificos")
def imprimir_nombres_por_tipo(root, tipo_buscado):
    if root is not None:
        imprimir_nombres_por_tipo(root.left, tipo_buscado)
        if root.value == tipo_buscado:
            print(f"  - {root.other_values.name}")
        imprimir_nombres_por_tipo(root.right, tipo_buscado)

tipos_buscados = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for tipo in tipos_buscados:
    print(f"Tipo {tipo}:")
    imprimir_nombres_por_tipo(arbol_tipo.root, tipo)

print("listado ascendente por numero")
def inorden(root):
    if root is not None:
        inorden(root.left)
        print(root.other_values)
        inorden(root.right)

inorden(arbol_numero.root)

print("listado ascendente por nombre")
inorden(arbol_nombre.root)

print("listado por nivel por nombre")
def listado_por_nivel(arbol):
    pendings = Queue()
    if arbol.root is not None:
        pendings.arrive(arbol.root)
        while pendings.size() > 0:
            node = pendings.attention()
            print(node.other_values)
            
            if node.left is not None:
                pendings.arrive(node.left)
            if node.right is not None:
                pendings.arrive(node.right)

listado_por_nivel(arbol_nombre)

print("pokemons debiles")
def debiles_frente_a(root, tipos_ataque):
    if root is not None:
        debiles_frente_a(root.left, tipos_ataque)
        es_debil = False
        for debilidad in root.other_values.weaknesses:
            if debilidad in tipos_ataque:
                es_debil = True
        if es_debil:
            print(root.other_values)   
        debiles_frente_a(root.right, tipos_ataque)

debiles_frente_a(arbol_nombre.root, ["Eléctrico", "Roca", "Dragón"])

print("total de pokemons por tipo")
conteo_tipos = {}
def contar_tipos(root):
    if root is not None:
        contar_tipos(root.left)
        for t in root.other_values.types:
            if t in conteo_tipos:
                conteo_tipos[t] += 1
            else:
                conteo_tipos[t] = 1
        contar_tipos(root.right)

contar_tipos(arbol_nombre.root)
for t, cantidad in sorted(conteo_tipos.items()):
    print(f"{t}: {cantidad}")

print("pokemons con megaevolucion y gigamax")
contadores_especiales = {"mega": 0, "gigamax": 0}
def contar_formas(root):
    if root is not None:
        contar_formas(root.left)
        if root.other_values.has_mega:
            contadores_especiales["mega"] += 1
        if root.other_values.has_gigantamax:
            contadores_especiales["gigamax"] += 1
        contar_formas(root.right)

contar_formas(arbol_nombre.root)
print(f"Pokemons con megaevolucion: {contadores_especiales['mega']}")
print(f"Pokemons con forma gigamax: {contadores_especiales['gigamax']}")