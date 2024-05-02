import plotly.graph_objects as go
import os
import gerando_grafico_base as gf
fig1 = go.Figure(go.Bar(
    x=[30],
    y=['Dias restantes'],
    marker=dict(color="#eaeaea",cornerradius=30),
    width=0.2,
    orientation="h",
))

# Remover fundo
fig1.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    title='',
    xaxis=dict(range=[0, 30], title='', visible=False),
    yaxis=dict(title='', visible=False),
    width=1900,
    height=400,
)

if not os.path.exists("images"):
    os.mkdir("images")
fig1.write_image("/home/victor/Documents/TREZENTOS/images/backside_dias_graf.png")
#fig1.show()