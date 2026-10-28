def agregar_categoria(categorias: set, nueva_categoria: str) -> set:
    """Agrega una nueva categoría al conjunto y retorna el conjunto actualizado."""
    categorias.add(nueva_categoria)
    return categorias


def registrar_libro(inventario: dict, isbn: str, titulo: str, autor: str, categoria: str, categorias: set) -> tuple:
    """Registra un libro en el inventario y actualiza el conjunto de categorías."""
    info_libro = (titulo, autor, categoria)
    inventario[isbn] = info_libro
    categorias = agregar_categoria(categorias, categoria)
    return inventario, categorias


def registrar_usuario(usuarios: dict, id_usuario: str, nombre: str) -> dict:
    """Registra un usuario con su nombre y una lista vacía para libros prestados."""
    usuarios[id_usuario] = {
        "nombre": nombre,
        "libros_prestados": []
    }
    return usuarios


def prestar_libro(isbn: str, id_usuario: str, inventario: dict, usuarios: dict) -> dict:
    """Gestiona el préstamo de un libro, moviéndolo del inventario al usuario."""
    if isbn not in inventario:
        print(f"Error: El libro con ISBN '{isbn}' no está disponible.")
        return inventario
        
    if id_usuario not in usuarios:
        print(f"Error: El usuario con ID '{id_usuario}' no está registrado.")
        return inventario
        
    usuarios[id_usuario]["libros_prestados"].append(isbn)
    inventario.pop(isbn)
    
    print(f"Préstamo exitoso: Libro {isbn} asignado a {usuarios[id_usuario]['nombre']}.")
    return inventario