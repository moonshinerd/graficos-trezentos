import pandas as pd
import plotly.graph_objects as go
import os
from PIL import Image
# Carregar o DataFrame
df = pd.read_excel("/home/victor/Documents/TREZENTOS/trezentosteste999.xlsx")
resol = 1
linha_grade = 1.1
media_turma = media_y_data = df.iloc[:, 1].mean()
dias_totais = 30
dia_atual = 15
porcent_graf_dias = (dia_atual / dias_totais) * 30

# Extrair os dados para os eixos x e y
x_data = df.iloc[:, 0].tolist()  # Primeira coluna
y_data = df.iloc[:, 1].tolist()  # Segunda coluna

#caso o valor do grupo seja igual a zero
# Verifique quais elementos são iguais a 0
for i in range(len(y_data)):
    if y_data[i] == 0:
        y_data[i] += 0.5

# Definir a largura e a altura da figura
largura = 2173*resol  # Defina o valor desejado
altura = 1524*resol  # Defina o valor desejado

# Lista para armazenar as cores das barras
cores = []

# Iterar sobre os valores de y para atribuir as cores correspondentes
for y in y_data:
    if 0 <= y < 2:
      cores.append('#e8e8e8')
    elif 2 <= y < 4:
      cores.append('#ef5eeb')
    elif 4 <= y < 6:
      cores.append('#ef9c8e')
    elif 6 <= y < 8:
      cores.append('#0ea84c')
    elif 8 <= y < 10:
      cores.append('#f4ea6e')
    elif 10 <= y < 12:
      cores.append('#a57449')
    elif 12 <= y < 14:
      cores.append('#56d19f')
    else:
      cores.append('#62b3ef')  # Cor padrão para outros valores
fonte_ttf_externa = "/home/victor/Documents/TREZENTOS/Poppins-Regular.ttf"
# Criar o gráfico de barras
fig = go.Figure(data=go.Bar(x=x_data, y=y_data, marker=dict(color=cores, cornerradius=30),width=0.65))

# Adicionar rótulos aos eixos
a=50
fig.update_layout(
    plot_bgcolor='white',

    xaxis_title="",
    yaxis_title="",
    title="",
    yaxis=dict(range=[0, 14.5],
        showgrid=True,  # Mostra as linhas de marcação no eixo y
        gridcolor='#919191',
        tickvals=list(range(0, 15, 2)),  # Especifica as posições dos ticks a cada 2 unidades
        ticktext=[f"{val}h" for val in range(0, 15, 2)],
        tickfont=dict(size=14*resol*2)
        ),
    xaxis=dict(
        tickvals=x_data,
        tickfont=dict(size=14*resol*2),  # Aumenta o tamanho da fonte dos números no eixo x
        titlefont=dict(size=20*resol*2)
        ),
    margin=dict(l=410*resol,r=185*resol, b=92*2*resol-a,t=392*resol+a), #l=410/2,r=185/2, b=92,t=392/2)
    width=largura,  # Definir a largura da figura
    height=altura,  # Definir a altura da figura
    font=dict(family=fonte_ttf_externa,
              color= "#000000"),
)

# Adicionar as imagens


# Obtém o diretório atual do script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói os caminhos relativos à pasta "bob_esponja"
path_imagem_0hour = os.path.join(current_directory, 'Bob_esponja_assets', '0hours.png')
path_imagem_2hour = os.path.join(current_directory, 'Bob_esponja_assets', '2hours.png')
path_imagem_4hour = os.path.join(current_directory, 'Bob_esponja_assets', '4hours.png')
path_imagem_6hour = os.path.join(current_directory, 'Bob_esponja_assets', '6hours.png')
path_imagem_8hour = os.path.join(current_directory, 'Bob_esponja_assets', '8hours.png')
path_imagem_10hour = os.path.join(current_directory, 'Bob_esponja_assets', '10hours.png')
path_imagem_12hour = os.path.join(current_directory, 'Bob_esponja_assets', '12hours.png')
path_imagem_14hour = os.path.join(current_directory, 'Bob_esponja_assets', '14hours.png')
path_imagem_logounb = os.path.join(current_directory, 'demais_assets', 'logo_unb.png')
path_imagem_logotrezentos = os.path.join(current_directory, 'demais_assets', 'trezentos.png')

a=0.045
imagens = [
    (path_imagem_0hour, -0.12*linha_grade, -0.05),
    (path_imagem_2hour, -0.11*linha_grade, 0.08),
    (path_imagem_4hour, -0.11*linha_grade, 0.21),
    (path_imagem_6hour, -0.115*linha_grade, 0.35),
    (path_imagem_8hour, -0.1115*linha_grade, 0.48),
    (path_imagem_10hour, -0.115*linha_grade, 0.62),
    (path_imagem_12hour, -0.1115*linha_grade, 0.75),
    (path_imagem_14hour, -0.105*linha_grade, 0.9),
    (path_imagem_logotrezentos, -0.25, 1.225+a),
    (path_imagem_logounb, 0.999, 1.22+a)
]

for imagem_url, x, y in imagens:
    fig.add_layout_image(
        dict(
            source=imagem_url,
            x=x,  # Posição x no canto inferior esquerdo do layout
            y=y,  # Posição y no canto inferior esquerdo do layout
            xref="paper",
            yref="paper",
            sizex=0.15,  # Ajuste conforme necessário
            sizey=0.15,  # Ajuste conforme necessário
            xanchor="left",  # Ancoragem à esquerda
            yanchor="bottom"  # Ancoragem na parte inferior
        )
    )

# Salvar a imagem
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("/home/victor/Documents/TREZENTOS/images/base_graf.png")
'''
base = Image.open("/home/victor/Documents/TREZENTOS/images/base_graf.png")
base.show()
'''