def parsear_producto(linea: str):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    pass


def resumen_de_producto(linea: str) -> str:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    pass


def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    pass


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    pass


def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    pass


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    # ejemplos rápidos para visualizar (descomenta cuando implementes)
    # print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    # print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    # print(valor_de_lote(products))                # 126.0
    # print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"
