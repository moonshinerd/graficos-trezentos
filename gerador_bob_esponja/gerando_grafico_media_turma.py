import gerando_grafico_base as gf
import pandas as pd
import plotly.graph_objects as go
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
media = gf.media_turma
if media < 0.5: media = 0.5
if 0 <= media < 2:
  cor='#e8e8e8'
elif 2 <= media < 4:
  cor='#ef5eeb'
elif 4 <= media < 6:
  cor='#ef9c8e'
elif 6 <= media < 8:
  cor='#0ea84c'
elif 8 <= media < 10:
  cor='#f4ea6e'
elif 10 <= media < 12:
  cor='#a57449'
elif 12 <= media < 14:
  cor='#56d19f'
else:
  cor='#62b3ef' 
fig1 = go.Figure(go.Bar(
    x=['Média da Turma'],
    y=[media],
    marker=dict(color=cor,cornerradius=30),
    width=0.2,
))

# Remover fundo
fig1.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    title='',
    xaxis=dict(title='', visible=False),
    yaxis=dict(range=[0, 14.5], title='', visible=False),
    width=400,
    height=1040,
)


fig1.write_image(os.path.join(current_dir, 'images', 'media_graf.png'))
#fig1.show()
