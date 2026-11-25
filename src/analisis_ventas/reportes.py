"""Generación del resumen de resultados en texto."""
from . import metricas


def construir_resumen(df, n=5):
    """Arma un texto con total general, top de productos y ventas mensuales."""
    lineas = [f"Total general: {metricas.total_general(df):,.2f}", f"Top {n} productos:"]
    lineas += [f"  {p}: {v:,.2f}" for p, v in metricas.top_productos(df, n).items()]
    lineas.append("Ventas por mes:")
    lineas += [f"  {m}: {v:,.2f}" for m, v in metricas.ventas_por_mes(df).items()]
    return "\n".join(lineas)
