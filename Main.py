from Catalogo import catalogo
from Venta import venta
from Factura import factura

def mostrar_menu():
    print("\nSistema de Facturación Electrónica")
    print("1. Mostrar catálogo de productos")
    print("2. Agregar producto al catálogo")
    print("3. Registrar venta")
    print("4. Generar factura")
    print("5. Salir")

def main():
    catalogo = catalogo()
    venta = venta()
    
    catalogo.agregar_producto("001", "Refrigerador", 1200, "Línea Blanca")
    catalogo.agregar_producto("002", "Licuadora", 300, "Pequeños Electrodomésticos")
    catalogo.agregar_producto("003", "Televisor", 800, "Entretenimiento")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\nCatálogo de Productos:")
            catalogo.mostrar_productos()
        
        elif opcion == "2":
            print("\nAgregar un nuevo producto:")
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            categoria = input("Categoría del producto: ")
            catalogo.agregar_producto(codigo, nombre, precio, categoria)
            print("Producto agregado exitosamente.")
        
        elif opcion == "3":
            print("\nRegistrar una venta:")
            codigo = input("Ingrese el código del producto: ")
            cantidad = int(input("Cantidad a vender: "))
            venta.agregar_venta(catalogo, codigo, cantidad)
        
        elif opcion == "4":
            print("\nGenerar Factura:")
            if venta.items_vendidos:
                factura = factura(venta.items_vendidos)
                factura.generar_factura()
                venta.items_vendidos = []  
            else:
                print("No hay productos vendidos para generar una factura.")
        
        elif opcion == "5":
            print("Saliendo del sistema. ¡Gracias por usar nuestro programa!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
