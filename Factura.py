class factura:
    def __init__(self, items_vendidos):
        self.items_vendidoos = items_vendidos

def generar_factura(self):
    subtotal = 0
    for item in self.items_vendidos:
        producto = item["producto"]
        cantidad = item["cantidad"]
        subtotal += producto["precio"]* cantidad
        iva = subtotal * 0.19
        total = subtotal + iva
        print("factura:")
        print("detalles de la compra:")
    for item in self.items_vendidos:
        productos = item["producto"]
        cantidad = item["cantidad"]
        print(f"{producto['nombre']}x{cantidad} - ${producto['precio']* cantidad}")
        print(f"subtotal: $ {subtotal: .2f}")
        print(f"iva: ${iva: .2f}")
        print(f"total: ${total:.2f}")