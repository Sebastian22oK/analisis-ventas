# Análisis de ventas

Programa en Python que carga un archivo CSV de ventas, limpia los datos y calcula el
total general, los productos más vendidos y las ventas por mes.

## Requisitos
Python 3.10 o superior y las librerías de `requirements.txt`.

## Instalación
```bash
pip install -r requirements.txt
```

## Uso
```bash
python main.py data/ventas.csv --top 5
```

## Formato del CSV
Columnas obligatorias: `fecha`, `producto`, `categoria`, `cantidad` y `precio`.
Las filas duplicadas, incompletas o con cantidad o precio no positivos se descartan.

## Estructura
- `src/analisis_ventas/`: módulos `carga`, `limpieza`, `metricas` y `reportes`.
- `main.py`: punto de entrada por línea de comandos.
- `codigo_original.py`: script inicial antes de la refactorización.
- `tests/`: pruebas automatizadas con `pytest`.
- `.github/workflows/ci.yml`: integración continua con GitHub Actions.

## Pruebas
```bash
python -m pytest -q
```

## Autor
Lita Daniel
