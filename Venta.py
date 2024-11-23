class Venta:
    def __init__(self):
        self.items_vendidos = [] 
    
    def agregar_venta(self, catalogo, codigo_producto, cantidad):
        producto = catalogo.buscar_producto(codigo_producto)
        if producto:
            self.items_vendidos.append({"producto": producto, "cantidad": cantidad})
        else:
            print("Producto no encontrado.")
    
    def mostrar_ventas(self):
        if not self.items_vendidos:
            print("No hay ventas registradas.")
            return
        print("Ventas realizadas:")
        for item in self.items_vendidos:
            producto = item["producto"]
            cantidad = item["cantidad"]
            print(
                f"Producto: {producto['nombre']}, Cantidad: {cantidad}, Precio Unitario: {producto['precio']:.2f}, Subtotal: {producto['precio'] * cantidad:.2f}"
            )
