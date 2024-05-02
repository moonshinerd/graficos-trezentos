import pandas as pd
import plotly.graph_objects as go
import os
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

# Criar o gráfico de barras
fig = go.Figure(data=go.Bar(x=x_data, y=y_data, marker=dict(color=cores, cornerradius=30),width=0.65))

# Adicionar rótulos aos eixos
fig.update_layout(
    plot_bgcolor='white',

    xaxis_title="Grupo",
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
    margin=dict(l=410*resol,r=185*resol, b=92*2*resol,t=392*resol), #l=410/2,r=185/2, b=92,t=392/2)
    width=largura,  # Definir a largura da figura
    height=altura,  # Definir a altura da figura
    font=dict(family="Poppins"),
)

# Adicionar as imagens
imagens = [
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZLfn-QAL8Q1_SHqkxDAerl4NSpaMrSCtUsh2-UHaOXT8cmW6YlpOC16wAgJuXPY8plRJYr7NKzQTPmv5kioWXHfbMVJawcNDc=w1175-h893", -0.12*linha_grade, -0.05),
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZMmgOvZYv7I-rmA68cLumTUqWM57Y0Qhf9kAlg8q2FfbByIJIWAWm_sB2AbuQuo6djW6Kvt9H51iyh8VJlHCoF8Ek0QMvGm9c=w1920-h968", -0.11*linha_grade, 0.08),
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihYpG9zfwXVWB7Sa-E3wmQqF_XPRfsJDZjQ9Kqn4_YUPHEmklYh_jdFzxEmgS9dBd04eqRHirqXaUVbbLSVpJ6Osm8ZCUtl5FuA=w1920-h298", -0.11*linha_grade, 0.21),
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihakNsQT-BHw26LHyERPjQW6bYUuJ2dA5p8eAzqW1G1-icnAYEi_9uOdTccUPRC010z2yGlz0ki9WNzoq2GEdmDtO0yB3PXQab8=w1920-h927", -0.115*linha_grade, 0.35),
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihbkqmnR5NJ8nPmUl0ikwkCtxcmIrmg8-Bws4ENXc2qYxJ_HG4Qee_F6v9oJQBkXf8Pra_QGE43bJlBQ_8_qH-Da5_3hX4vxxKk=w1920-h968", -0.1115*linha_grade, 0.48),
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihb1MnjKMi7wq4CuWidnVKHK4PI_wWq-7m1OvBIOBg1yJ32Dx6kRarXP_wG13PHQzazknuZgF35oDXa7t24UxYwmy5CI19hL9g=w1920-h968", -0.115*linha_grade, 0.62),
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihYM70mWQfdpEeFLvs-WqnbFIhbLdIjJ-myDwSQ26ewpP9NNakzGpRGAyzOV0TeNTZeVoYKQspRjlgtWF6t85wBtybMKnnxzfb0=w1920-h968", -0.1115*linha_grade, 0.75),
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihYhsGzTGZbVoBMshdjmCOKVJvTykFhYb-zQ8lVappNN2vhae4896hkCrfehvCqwnQkoFQCwfoAWWF4QSEhnaNDc2DUCVdnZXA=w1920-h968", -0.105*linha_grade, 0.9),
    ("https://lh3.googleusercontent.com/u/0/drive-viewer/AKGpihZBq1w-NiUbVSw8fzE3UBCiAbDK6uvI2CTXojLYkFM2cwAXBenfhAa7mDjJ6Ceqn5mdwNLqHCEZyWBXBTBvvtZMamL1zVEIIro=w1920-h968", -0.25, 1.22)
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

# Exibir o gráfico
#fig.show()
