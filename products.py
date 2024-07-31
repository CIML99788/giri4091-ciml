import requests
import json

def GetAllproducts():
    url = 'https://fakestoreapi.com/products'
    respuesta = requests.get(url).json()

    print("Listado de productos")
    print('-------------')
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

def GetProduct():
    product_id = input("Ingrese el ID del producto que desea buscar: ")
    url = f'https://fakestoreapi.com/products/{product_id}'
    respuesta = requests.get(url).json()

    print(f"Detalles del producto con ID {product_id}")
    print('-------------')
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

def AddProduct():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    descripcion = input("Ingrese la descripción del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    imagen = input("Ingrese la URL de la imagen del producto: ")
    

    producto = {
        'title': nombre,
        'price': precio,
        'description': descripcion,
        'category': categoria,
        'image': imagen
    }

    url = 'https://fakestoreapi.com/products'
    respuesta = requests.post(url, json=producto).json()

    print("Producto agregado exitosamente")
    print('-------------')
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

def UpdateProduct():
    product_id = input("Ingrese el ID del producto que desea modificar: ")
    nombre = input("Ingrese el nuevo nombre del producto: ")
    precio = float(input("Ingrese el nuevo precio del producto: "))
    descripcion = input("Ingrese la nueva descripción del producto: ")
    categoria = input("Ingrese la nueva categoría del producto: ")
    imagen = input("Ingrese la nueva URL de la imagen del producto: ")

    producto = {
        'title': nombre,
        'price': precio,
        'description': descripcion,
        'category': categoria,
        'image': imagen
    }

    url = f'https://fakestoreapi.com/products/{product_id}'
    respuesta = requests.put(url, json=producto).json()

    print(f"Producto con ID {product_id} modificado exitosamente")
    print('-------------')
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

def DeleteProduct():
    product_id = input("Ingrese el ID del producto que desea eliminar: ")
    url = f'https://fakestoreapi.com/products/{product_id}'
    respuesta = requests.delete(url).json()

    print(f"Producto con ID {product_id} eliminado exitosamente")
    print('-------------')
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

def mostrar_menu():
    print("\nAdministración de Productos:")
    print("1. Consultar todos los productos")
    print("2. Consultar un producto en específico")
    print("3. Agregar un nuevo producto")
    print("4. Modificar producto en específico")
    print("5. Eliminar un producto")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")
    
    if opcion == '1':
        GetAllproducts()
    elif opcion == '2':
        GetProduct()
    elif opcion == '3':
        AddProduct()
    elif opcion == '4':
        UpdateProduct()    
    elif opcion == '5':
        DeleteProduct()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")
