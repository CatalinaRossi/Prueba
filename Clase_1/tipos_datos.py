# STRINGS
a = "eSTO ES UNA CADENA"
b = "Esto es otra cadena"

print(a, type(a))
print(b, type(b))

c = str(120.56)
print(c, type(c))

print(a[0:4])
print(a[-1])

# METODOS DE LOS STRINGS
print(a.lower())
print(a.upper())
print(len(a.split()))

# LISTA
lista_1 = ["Hola", 4, 2.5, True, [1,2,3,4], ("a", "b")]
print(lista_1)
print(type(lista_1))
print(len(lista_1))
print(lista_1[2])

var_uno = lista_1[4]
print(var_uno)

# METODOS DE LAS LISTAS
print(lista_1.append("lista"))
print(lista_1)

print(lista_1.index(("a", "b")))
lista_1.insert(1, 5)
print(lista_1)

# DICCIONARIO
usuario = {
   "nombre": "Octavio", 
   "apellido": "Gomez",
   "edad": 38,
   "hobbies": ["Futbol", "Musica"],
   "mascotas": False
}

print(usuario)
print(usuario["edad"])
print(len(usuario))

#METODOS DE DICCIONARIOS

print(usuario.get("hobbies"))
print(usuario.get("Puesto", "no encontrado"))

keys_usuario = list(usuario.keys())
print(usuario.get(keys_usuario[0]))

print(usuario.values())