def parsear_producto(linea: str) -> dict:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """
    if not isinstance(linea, str):
        raise ValueError("La línea debe ser una cadena de texto (str).")
    
    partes = linea.split(",")
    if len(partes) != 4:
        raise ValueError("La línea debe contener exactamente 4 elementos separados por comas.")
    
    codigo, nombre, precio_str, cantidad_str = [p.strip() for p in partes]
    
    try:
        precio = float(precio_str)
        if precio < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError(f"Precio inválido: '{precio_str}'. Debe ser un número mayor o igual a 0.")
        
    try:
        cantidad = int(cantidad_str)
        if cantidad < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError(f"Cantidad inválida: '{cantidad_str}'. Debe ser un entero mayor o igual a 0.")
        
    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }


def resumen_de_producto(linea: str) -> str:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    producto = parsear_producto(linea)
    valor = round(producto["precio"] * producto["cantidad"], 1)
    return f"{producto['codigo']} - {producto['nombre']}: ${valor}"


def _validar_lineas(lineas: list) -> None:
    """Función de ayuda interna para validar que la entrada sea una lista no vacía de strings."""
    if not isinstance(lineas, list) or len(lineas) == 0:
        raise ValueError("El argumento debe ser una lista no vacía.")
    for elemento in lineas:
        if not isinstance(elemento, str):
            raise ValueError("Todos los elementos de la lista deben ser cadenas de texto (str).")


def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """
    _validar_lineas(lineas)
    salida = []
    for linea in lineas:
        salida.append(resumen_de_producto(linea))
    return salida


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """
    _validar_lineas(lineas)
    total = 0.0
    for linea in lineas:
        producto = parsear_producto(linea)
        total += producto["precio"] * producto["cantidad"]
    return round(total, 1)


def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    _validar_lineas(lineas)
    
    mejor_linea = lineas[0]
    p_mejor = parsear_producto(mejor_linea)
    max_valor = p_mejor["precio"] * p_mejor["cantidad"]
    
    for linea in lineas[1:]:
        p_actual = parsear_producto(linea)
        valor_actual = p_actual["precio"] * p_actual["cantidad"]
        
        if valor_actual > max_valor:
            max_valor = valor_actual
            mejor_linea = linea
            
    return resumen_de_producto(mejor_linea)


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    print(resumen_de_producto(products[0]))        # "P001 - Lapiz: $50.0"
    print(resumen_de_lotes(products))              # ["P001 - ...", "P002 - ...", "P003 - ..."]
    print(valor_de_lote(products))                 # 126.0
    print(producto_maximo_valor(products))         # "P002 - Cuaderno: $62.5"
