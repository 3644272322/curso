import numpy as np
import plotly.graph_objects as go

# Parámetros base
eje_bx = 0
eje_by = 0

# Rango de valores para los ejes
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Crear la malla (grid)
X, Y = np.meshgrid(x, y)

# Calcular la función
Z = (X - eje_bx)**2 + ((Y - eje_by)**2) / 0.5

# Crear la figura 3D con Plotly
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])

# Personalizar el gráfico
fig.update_layout(
    title="Superficie de f(x, y) = (x - bx)² + (y - by)² / 0.5",
    scene=dict(
        xaxis_title='eje_ax (x)',
        yaxis_title='eje_ay (y)',
        zaxis_title='f(x, y)'
    ),
    width=700,
    height=600
)

# Mostrar el gráfico
fig.show()
