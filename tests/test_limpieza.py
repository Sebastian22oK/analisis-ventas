import pandas as pd

from src.analisis_ventas.limpieza import limpiar_ventas


def crear_df():
    return pd.DataFrame({
        "fecha": pd.to_datetime(["2025-01-05", "2025-01-05", "2025-02-10", "2025-02-11"]),
        "producto": ["A", "A", "B", "C"],
        "categoria": ["x", "x", "y", "y"],
        "cantidad": [2, 2, -1, 3],
        "precio": [10.0, 10.0, 5.0, None],
    })


def test_elimina_duplicados_negativos_y_nulos():
    limpio = limpiar_ventas(crear_df())
    assert len(limpio) == 1
    assert limpio.iloc[0]["producto"] == "A"


def test_limpieza_dataframe_vacio():
    vacio = pd.DataFrame({
        "fecha": pd.to_datetime([]),
        "producto": pd.Series(dtype="object"),
        "categoria": pd.Series(dtype="object"),
        "cantidad": pd.Series(dtype="int64"),
        "precio": pd.Series(dtype="float64"),
    })
    assert limpiar_ventas(vacio).empty
