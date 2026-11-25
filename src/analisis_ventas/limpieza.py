"""Limpieza de datos de ventas."""


def limpiar_ventas(df):
    """Quita duplicados, filas incompletas y valores no positivos.

    Args:
        df: DataFrame de ventas.
    Returns:
        Copia limpia del DataFrame.
    """
    # Las máscaras booleanas filtran todas las filas a la vez
    df = df.drop_duplicates().dropna(subset=["fecha", "producto", "cantidad", "precio"])
    return df[(df["cantidad"] > 0) & (df["precio"] > 0)].copy()
