class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = {}

    def agregar_producto(self, nombre, precio, cantidad):
        if precio > 0 and cantidad > 0:
            if nombre in self.productos:
                self.productos[nombre]['cantidad'] += cantidad
                print(f"✅ Se actualizó la cantidad de '{nombre}'.")
            else:
                self.productos[nombre] = {'precio': precio, 'cantidad': cantidad}
                print(f"✅ Se agregó el producto '{nombre}'.")
        else:
            print("❌ Error: El precio y la cantidad deben ser valores positivos.")

    def vender_producto(self, nombre, cantidad):
        if nombre not in self.productos:
            print(f"❌ Error: El producto '{nombre}' no existe.")
        elif cantidad <= 0:
            print("❌ Error: La cantidad a vender debe ser positiva.")
        elif self.productos[nombre]['cantidad'] >= cantidad:
            self.productos[nombre]['cantidad'] -= cantidad
            print(f"✅ Se vendieron {cantidad} unidades de '{nombre}'.")
        else:
            print(f"❌ Error: No hay suficiente stock. Stock actual: {self.productos[nombre]['cantidad']}.")

    def mostrar_inventario(self):
        print(f"\n--- Inventario de {self.nombre_tienda} ---")
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for nombre, datos in self.productos.items():
                print(f"Producto: {nombre} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")
        print("-----------------------------------")

    def producto_mas_caro(self):
        if not self.productos:
            return None, None
        
        nombre_caro = max(self.productos, key=lambda p: self.productos[p]['precio'])
        precio_caro = self.productos[nombre_caro]['precio']
        return nombre_caro, precio_caro

def main():
    mi_tienda = InventarioTienda("Mi Tienda")
    
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Producto más caro")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                mi_tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("❌ Entrada inválida. Asegúrate de ingresar números para precio y cantidad.")

        elif opcion == '2':
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
                mi_tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print("❌ Entrada inválida. La cantidad debe ser un número entero.")

        elif opcion == '3':
            mi_tienda.mostrar_inventario()

        elif opcion == '4':
            nombre_caro, precio_caro = mi_tienda.producto_mas_caro()
            if nombre_caro:
                print(f"🤑 El producto más caro es '{nombre_caro}' con un precio de ${precio_caro}.")
            else:
                print("El inventario está vacío.")
                
        elif opcion == '5':
            print("👋 Saliendo del programa. ¡Hasta la próxima!")
            break
            
        else:
            print("❌ Opción no válida. Por favor, elige de 1 a 5.")

if __name__ == "__main__":
    main()