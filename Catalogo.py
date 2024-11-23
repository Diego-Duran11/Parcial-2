class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, codigo, nombre, precio, categoria):
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria,
        }
        self.productos.append(producto)
    
    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
            return
        print("Catálogo de productos:")
        for prod in self.productos:
            print(
                f"Código: {prod['codigo']}, Nombre: {prod['nombre']}, Precio: {prod['precio']:.2f}, Categoría: {prod['categoria']}"
            )
    
    def buscar_producto(self, codigo):
        for prod in self.productos:
            if prod["codigo"] == codigo:
                return prod
        return None
