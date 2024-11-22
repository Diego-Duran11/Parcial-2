class catalogo:
    def _init_(self):
     self.productos = []
    
def agregar_producto(self, codigo, nombre, precio, categoria):
   producto = {"codigo": codigo, "nombre": nombre, "precio": precio,"categoria": categoria}
   self.productos.append(producto)

def mostrar_productos(self):
    for prod in self.productos:
      print(f"Codigo:{prod['codigo']}, Nombre:{prod['nombre']}, Precio:{prod['precio']}, Categoria:{prod['categoria']}")

def buscar_productos(self, codigo):
   for prod in self.productos:
      if prod["codigo"] == codigo:
         return prod
      return None