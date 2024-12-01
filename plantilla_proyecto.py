# Importar las librerías necesarias
from dash import Dash, html, dcc  # Dash para construir el dashboard, html para componentes básicos, dcc para gráficos
import plotly.express as px       # Plotly Express para generar gráficos interactivos
import pandas as pd               # Pandas para manejar y procesar datos

# Crear la aplicación Dash
app = Dash(__name__)  # __name__ se usa para inicializar la app Dash

# ----------------------- DATOS ---------------------------
# Puedes usar un dataset predefinido de Plotly para propósitos educativos
df = px.data.gapminder()

# -------------------- GRÁFICOS --------------------------
# Crear gráficos con Plotly usando los datos del DataFrame
fig1 = px.line(
    df[df['country'] == 'India'], 
    x='year', 
    y='gdpPercap', 
    title='Crecimiento PIB - India'
)  # Gráfico de línea mostrando el PIB per cápita de India

fig2 = px.bar(
    df[df['year'] == 2007], 
    x='continent', 
    y='pop', 
    title='Población por Continente'
)  # Gráfico de barras mostrando la población por continente en 2007

fig3 = px.scatter(
    df, 
    x='gdpPercap', 
    y='lifeExp', 
    color='continent', 
    title='PIB vs Esperanza de Vida'
)  # Gráfico de dispersión que relaciona PIB y esperanza de vida

fig4 = px.histogram(
    df, 
    x='lifeExp', 
    title='Distribución Esperanza de Vida'
)  # Histograma mostrando la distribución de la esperanza de vida

# --------------------- DISEÑO ---------------------------
# Crear el layout de la aplicación
app.layout = html.Div([  # html.Div es el contenedor principal
    # Título del dashboard
    html.H1(
        "Mi Dashboard Interactivo", 
        style={'textAlign': 'center', 'fontSize': '24px', 'marginBottom': '20px'}
    ),
    
    # Primera fila de gráficos (2 gráficos en paralelo)
    html.Div([
        # Primera celda con el gráfico 1
        html.Div([dcc.Graph(figure=fig1)], 
                 style={'width': '50%', 'display': 'inline-block'}),
        # Segunda celda con el gráfico 2
        html.Div([dcc.Graph(figure=fig2)], 
                 style={'width': '50%', 'display': 'inline-block'})
    ], style={'display': 'flex'}),
    
    # Segunda fila de gráficos (2 gráficos en paralelo)
    html.Div([
        # Tercera celda con el gráfico 3
        html.Div([dcc.Graph(figure=fig3)], 
                 style={'width': '50%', 'display': 'inline-block'}),
        # Cuarta celda con el gráfico 4
        html.Div([dcc.Graph(figure=fig4)], 
                 style={'width': '50%', 'display': 'inline-block'})
    ], style={'display': 'flex'}),
    
    # Pie de página
    html.Footer(
        "Autor: [Tu Nombre]", 
        style={'textAlign': 'right', 'fontSize': '12px', 'marginTop': '20px'}
    )
])

# --------------------- EJECUCIÓN ------------------------
# Iniciar el servidor para ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
# Importar las librerías necesarias
from dash import Dash, html, dcc  # Dash para construir el dashboard, html para componentes básicos, dcc para gráficos
import plotly.express as px       # Plotly Express para generar gráficos interactivos
import pandas as pd               # Pandas para manejar y procesar datos

# Crear la aplicación Dash
app = Dash(__name__)  # __name__ se usa para inicializar la app Dash

# ----------------------- DATOS ---------------------------
# Puedes usar un dataset predefinido de Plotly para propósitos educativos
df = px.data.gapminder()

# -------------------- GRÁFICOS --------------------------
# Crear gráficos con Plotly usando los datos del DataFrame
fig1 = px.line(
    df[df['country'] == 'India'], 
    x='year', 
    y='gdpPercap', 
    title='Crecimiento PIB - India'
)  # Gráfico de línea mostrando el PIB per cápita de India

fig2 = px.bar(
    df[df['year'] == 2007], 
    x='continent', 
    y='pop', 
    title='Población por Continente'
)  # Gráfico de barras mostrando la población por continente en 2007

fig3 = px.scatter(
    df, 
    x='gdpPercap', 
    y='lifeExp', 
    color='continent', 
    title='PIB vs Esperanza de Vida'
)  # Gráfico de dispersión que relaciona PIB y esperanza de vida

fig4 = px.histogram(
    df, 
    x='lifeExp', 
    title='Distribución Esperanza de Vida'
)  # Histograma mostrando la distribución de la esperanza de vida

# --------------------- DISEÑO ---------------------------
# Crear el layout de la aplicación
app.layout = html.Div([  # html.Div es el contenedor principal
    # Título del dashboard
    html.H1(
        "Mi Dashboard Interactivo", 
        style={'textAlign': 'center', 'fontSize': '24px', 'marginBottom': '20px'}
    ),
    
    # Primera fila de gráficos (2 gráficos en paralelo)
    html.Div([
        # Primera celda con el gráfico 1
        html.Div([dcc.Graph(figure=fig1)], 
                 style={'width': '50%', 'display': 'inline-block'}),
        # Segunda celda con el gráfico 2
        html.Div([dcc.Graph(figure=fig2)], 
                 style={'width': '50%', 'display': 'inline-block'})
    ], style={'display': 'flex'}),
    
    # Segunda fila de gráficos (2 gráficos en paralelo)
    html.Div([
        # Tercera celda con el gráfico 3
        html.Div([dcc.Graph(figure=fig3)], 
                 style={'width': '50%', 'display': 'inline-block'}),
        # Cuarta celda con el gráfico 4
        html.Div([dcc.Graph(figure=fig4)], 
                 style={'width': '50%', 'display': 'inline-block'})
    ], style={'display': 'flex'}),
    
    # Pie de página
    html.Footer(
        "Autor: [Tu Nombre]", 
        style={'textAlign': 'right', 'fontSize': '12px', 'marginTop': '20px'}
    )
])

# --------------------- EJECUCIÓN ------------------------
# Iniciar el servidor para ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
