"""Punto de entrada: python main.py data/ventas.csv"""
import argparse
import logging

from src.analisis_ventas.carga import cargar_ventas
from src.analisis_ventas.limpieza import limpiar_ventas
from src.analisis_ventas.reportes import construir_resumen

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


def main():
    """Carga, limpia y muestra el resumen de ventas."""
    parser = argparse.ArgumentParser(description="Análisis de ventas")
    parser.add_argument("ruta", help="archivo CSV de ventas")
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()
    # Se limpia antes de calcular para que todas las métricas usen los mismos datos
    df = limpiar_ventas(cargar_ventas(args.ruta))
    logging.info("Filas válidas: %d", len(df))
    print(construir_resumen(df, args.top))


if __name__ == "__main__":
    main()
