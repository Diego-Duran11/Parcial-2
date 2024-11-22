from Catalogo import catalogo
class venta:
    def __init__(self):
        self.items_vendidos = []

def agregar_venta(self, catalogo, codigo_producto, cantidad):
    producto = catalogo.buscar_producto(codigo_producto)
    if producto:
        self.items_vendidos.append({"producto": producto, "cantidad": cantidad})
    else:
        print("producto no encontrado")

def motrar_ventas(self):
    for item in self.item_vendidos:
        producto = item["producto"]
        print(f"Nombre:{producto['nombre']}, Cantidad{producto['cantidad']}, Precio:{producto['precio']}")
    