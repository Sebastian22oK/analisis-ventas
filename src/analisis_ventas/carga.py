"""Lectura y validación de los archivos de ventas."""
from pathlib import Path

import pandas as pd

COLUMNAS = ["fecha", "producto", "categoria", "cantidad", "precio"]


def _validar_ruta(ruta):
    """Convierte la ruta a Path y verifica que el archivo exista."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo {ruta}")
    return ruta


def _validar_columnas(df):
    """Verifica que el DataFrame contenga todas las columnas obligatorias."""
    faltantes = set(COLUMNAS) - set(df.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas: {sorted(faltantes)}")


def cargar_ventas(ruta):
    """Lee un CSV de ventas y verifica que tenga las columnas esperadas.

    Args:
        ruta: ruta del archivo CSV.
    Returns:
        DataFrame con la fecha convertida a datetime.
    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si faltan columnas obligatorias.
    """
    ruta = _validar_ruta(ruta)
    df = pd.read_csv(ruta)
    _validar_columnas(df)
    # Se convierte después de validar columnas para evitar errores de parse_dates
    df["fecha"] = pd.to_datetime(df["fecha"])
    return df


def leer_por_bloques(ruta, tamano=100_000):
    """Genera el archivo por bloques para no cargar todo en memoria.

    Args:
        ruta: ruta del archivo CSV.
        tamano: cantidad máxima de filas por bloque.
    Yields:
        DataFrame correspondiente a cada bloque leído.
    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si faltan columnas obligatorias.
    """
    ruta = _validar_ruta(ruta)
    for bloque in pd.read_csv(ruta, chunksize=tamano):
        _validar_columnas(bloque)
        bloque["fecha"] = pd.to_datetime(bloque["fecha"])
        yield bloque
