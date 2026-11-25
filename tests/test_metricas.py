import pandas as pd
import pytest

from src.analisis_ventas import metricas
from src.analisis_ventas.carga import cargar_ventas


@pytest.fixture
def df():
    return pd.DataFrame({
        "fecha": pd.to_datetime(["2025-01-05", "2025-01-20", "2025-02-10"]),
        "producto": ["A", "B", "A"],
        "categoria": ["x", "y", "x"],
        "cantidad": [2, 1, 3],
        "precio": [10.0, 60.0, 10.0],
    })


def test_total_general(df):
    assert metricas.total_general(df) == 110.0


def test_ventas_por_producto(df):
    assert metricas.ventas_por_producto(df)["A"] == 50.0


def test_top_productos_ordena_descendente(df):
    top = metricas.top_productos(df, 2)
    assert list(top.index) == ["B", "A"]


def test_ventas_por_mes(df):
    meses = metricas.ventas_por_mes(df)
    assert meses.iloc[0] == 80.0 and meses.iloc[1] == 30.0


def test_total_por_bloques_coincide(tmp_path, df):
    ruta = tmp_path / "v.csv"
    df.to_csv(ruta, index=False)
    assert metricas.total_por_bloques(ruta, tamano=2) == 110.0


def test_archivo_inexistente_lanza_error():
    with pytest.raises(FileNotFoundError):
        cargar_ventas("no_existe.csv")


def test_columnas_faltantes_lanza_error(tmp_path):
    ruta = tmp_path / "incompleto.csv"
    ruta.write_text("producto,categoria,cantidad,precio\nA,x,1,10\n", encoding="utf-8")
    with pytest.raises(ValueError, match=r"Faltan columnas: \['fecha'\]"):
        cargar_ventas(ruta)


def test_metricas_dataframe_vacio():
    vacio = pd.DataFrame({
        "fecha": pd.to_datetime([]),
        "producto": pd.Series(dtype="object"),
        "categoria": pd.Series(dtype="object"),
        "cantidad": pd.Series(dtype="int64"),
        "precio": pd.Series(dtype="float64"),
    })
    assert metricas.total_general(vacio) == 0.0
    assert metricas.top_productos(vacio, 5).empty
    assert metricas.ventas_por_mes(vacio).empty
