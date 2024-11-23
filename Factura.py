class Factura:
    def __init__(self, items_vendidos):
        self.items_vendidos = items_vendidos
    
    def generar_factura(self):
        if not self.items_vendidos:
            print("No hay productos vendidos para generar una factura.")
            return
        
        subtotal = 0
        print("\nFactura:")
        print("Detalles de los productos:")
        for item in self.items_vendidos:
            producto = item["producto"]
            cantidad = item["cantidad"]
            subtotal_producto = producto["precio"] * cantidad
            subtotal += subtotal_producto
            print(f"{producto['nombre']} x{cantidad} - ${subtotal_producto:.2f}")
        
        iva = subtotal * 0.19
        total = subtotal + iva
        
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"IVA (19%): ${iva:.2f}")
        print(f"Total: ${total:.2f}")
