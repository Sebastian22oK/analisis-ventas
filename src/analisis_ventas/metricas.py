"""Cálculo de métricas de ventas con operaciones vectorizadas."""
from .carga import leer_por_bloques
from .limpieza import limpiar_ventas


def agregar_total(df):
    """Añade la columna total como cantidad por precio."""
    return df.assign(total=df["cantidad"] * df["precio"])


def total_general(df):
    """Devuelve la suma de todas las ventas."""
    return float((df["cantidad"] * df["precio"]).sum())


def ventas_por_producto(df):
    """Devuelve una serie con el total vendido por producto."""
    return agregar_total(df).groupby("producto")["total"].sum()


def top_productos(df, n=5):
    """Devuelve los n productos con mayores ventas."""
    # nlargest evita ordenar a mano toda la serie
    return ventas_por_producto(df).nlargest(n)


def ventas_por_mes(df):
    """Devuelve el total vendido por mes."""
    # Se agrupa por periodo mensual sin convertir las fechas a texto
    meses = df["fecha"].dt.to_period("M")
    return agregar_total(df).groupby(meses)["total"].sum()


def total_por_bloques(ruta, tamano=100_000):
    """Suma el total de un archivo grande procesándolo por bloques."""
    # El generador entrega un bloque a la vez y mantiene bajo el uso de memoria
    return sum(total_general(limpiar_ventas(b)) for b in leer_por_bloques(ruta, tamano))
