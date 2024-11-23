from catalogo import Catalogo
from venta import Venta
from factura import Factura

def mostrar_menu():
    print("\nSistema de Facturación Electrónica")
    print("1. Mostrar catálogo de productos")
    print("2. Agregar producto al catálogo")
    print("3. Registrar venta")
    print("4. Generar factura")
    print("5. Salir")

def main():
    catalogo = Catalogo()
    venta = Venta()

    catalogo.agregar_producto("001", "Refrigerador", 1200, "Línea Blanca")
    catalogo.agregar_producto("002", "Licuadora", 300, "Pequeños Electrodomésticos")
    catalogo.agregar_producto("003", "Televisor", 800, "Entretenimiento")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            catalogo.mostrar_productos()
        
        elif opcion == "2":
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            categoria = input("Categoría del producto: ")
            catalogo.agregar_producto(codigo, nombre, precio, categoria)
            print("Producto agregado exitosamente.")
        
        elif opcion == "3":
            codigo = input("Ingrese el código del producto: ")
            cantidad = int(input("Cantidad a vender: "))
            venta.agregar_venta(catalogo, codigo, cantidad)
        
        elif opcion == "4":
            factura = Factura(venta.items_vendidos)
            factura.generar_factura()
            venta.items_vendidos = []
            
        elif opcion == "5":
            print("Saliendo del sistema. ¡Gracias por usar nuestro programa!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
