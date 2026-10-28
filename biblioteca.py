from modelos_biblioteca import (
    agregar_categoria,
    registrar_libro,
    registrar_usuario,
    prestar_libro
)

def main():
    print("=== INICIANDO SISTEMA DE BIBLIOTECA ===")
    
    inventario = {}
    usuarios = {}
    categorias = {"Fantasía", "Ciencia Ficción"}
    
    # Registrar libros
    inventario, categorias = registrar_libro(
        inventario, "978-0132350884", "Clean Code", "Robert C. Martin", "Tecnología", categorias
    )
    inventario, categorias = registrar_libro(
        inventario, "978-0201633610", "Design Patterns", "Erich Gamma", "Tecnología", categorias
    )
    
    print("\nCategorías:", categorias)
    print("Inventario:", inventario)
    
    # Registrar usuarios
    registrar_usuario(usuarios, "U001", "Ana Pérez")
    registrar_usuario(usuarios, "U002", "Carlos Gómez")
    
    print("\nUsuarios:", usuarios)
    
    # Realizar préstamo
    print("\n--- Ejecutando Préstamo ---")
    prestar_libro("978-0132350884", "U001", inventario, usuarios)
    
    print("\nInventario actualizado:", inventario)
    print("Estado usuario U001:", usuarios["U001"])

if __name__ == "__main__":
    main()