from PIL import Image,ImageOps, ImageDraw, ImageFont
import gerando_grafico_base, gerando_grafico_media_turma,backside_media_generator, backside_dias_generator,gerando_gráfico_dias# importando para executar os codigos
import resize_image as ri
import os


# Obtém o diretório atual do script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói os caminhos relativos à pasta "images"
path_imagem_base = os.path.join(current_directory, 'images', 'base_graf.png')
path_imagem_media = os.path.join(current_directory, 'images', 'media_graf.png')
path_redimensionada = os.path.join(current_directory, 'images', 'media_graf_redimensionada.png')
path_backside_media = os.path.join(current_directory, 'images', 'backside_media_graf.png')
path_backside_dias = os.path.join(current_directory, 'images', 'backside_dias_graf.png')
path_dias = os.path.join(current_directory, 'images', 'dias_graf.png')
path_linha_tracejada = os.path.join(current_directory, 'demais_assets', 'linha_tracejada.png')


# Abrindo imagens
base = Image.open(path_imagem_base)
media = Image.open(path_imagem_media)
backside_media = Image.open(path_backside_media)
backside_media_invertido = ImageOps.flip(backside_media.crop(backside_media.getbbox()))
backside_dias = Image.open(path_backside_dias)
backside_dias_invertido = ImageOps.mirror(backside_dias.crop(backside_dias.getbbox()))
dias = Image.open(path_dias)
dias_invertido = ImageOps.mirror(dias.crop(dias.getbbox()))
linha_tracejada = Image.open(path_linha_tracejada)

draw = ImageDraw.Draw(base)

# Define a fonte e o tamanho do texto
font_path = os.path.join(current_directory, "Poppins-Regular.ttf")
font_path_skema = os.path.join(current_directory, "SkemaProDisplay-Medium.ttf")

font_size = 30
font1 = ImageFont.truetype(font_path, font_size)

font_size = 55
font2 = ImageFont.truetype(font_path, font_size)

font_size = 35
font3 = ImageFont.truetype(font_path, font_size)

font_size = 26
font4 = ImageFont.truetype(font_path_skema, font_size)

font_size = 26
font5 = ImageFont.truetype(font_path, font_size)

a = 48
a1 = -10
text1 = "Média da"
pos1 = (a1+70, 1350+a)

text2 = "Turma"
pos2 = (a1+85, 1375+a)

b = -160
c = -20

text3 = "Cálculo 1 com Professor Ricardo Ramos Fragelli"
pos3 = (b+300+350, 75+c)

text4 = "1 semestre de 2024 - Primeira prova"
pos4 = (b+350+420, 125+c)

text5 = "Dia  " + str(gerando_grafico_base.dia_atual)
pos5 = (120, 220)

text6 = "Entrega"
pos6 = (2040, 220)

text7 = "Grupo"
pos7 = (1086, 1375+a)

text8 = "28h"
pos8 = (364, 350)

text_color = "#000000" #preto
# Adiciona o texto à imagem
draw.text( pos1 , text1, fill=text_color, font=font1)
draw.text( pos2 , text2, fill=text_color, font=font1)
draw.text( pos3 , text3, fill=text_color, font=font2)
draw.text( pos4 , text4, fill=text_color, font=font2)
draw.text( pos5 , text5, fill=text_color, font=font5)
draw.text( pos6 , text6, fill=text_color, font=font5)
draw.text( pos7 , text7, fill=text_color, font=font3)
draw.text( pos8 , text8, fill=text_color, font=font4)

# Corta a imagem para a caixa delimitadora
media = media.crop(media.getbbox())
media_invertida = ImageOps.flip(media)
ri.PNG_ResizeKeepTransparency(path_imagem_media,path_redimensionada,new_width=400,new_height=1040, resample=Image.LANCZOS)
# Salva a imagem redimensionada
media = Image.open(path_redimensionada) #teste

coordx = -75
coordy = gerando_grafico_base.resol*342
ajusty = 48
print(gerando_grafico_base.media_turma)
#if gerando_grafico_base.media_turma 
# Criando a barra da média da turma
base.paste(backside_media, (coordx, 290+ajusty+50),backside_media)  # ajuste a posição conforme necessário
base.paste(backside_media_invertido, (100, 1524-backside_media_invertido.height-180+ajusty),backside_media_invertido)  # ajuste a posição conforme necessário

if 12 < gerando_grafico_base.media_turma <= 14: base.paste(media, (coordx, coordy-33+ajusty),media)  # ajuste a posição conforme necessário
elif 10 < gerando_grafico_base.media_turma <= 12: base.paste(media,(coordx, coordy-32+ajusty),media)  # ajuste a posição conforme necessário
elif 8 < gerando_grafico_base.media_turma <= 10: base.paste(media, (coordx, coordy-18+ajusty),media)  # ajuste a posição conforme necessário
elif 6 < gerando_grafico_base.media_turma <= 8: base.paste(media, (coordx, coordy-10+ajusty),media)  # ajuste a posição conforme necessário
elif 4 < gerando_grafico_base.media_turma <= 6: base.paste(media, (coordx, coordy+ajusty),media)  # ajuste a posição conforme necessário
elif 2 < gerando_grafico_base.media_turma <= 4: base.paste(media, (coordx, coordy+ajusty+20),media)  # ajuste a posição conforme necessário
else: base.paste(media, (coordx, coordy+ajusty+24),media)  # ajuste a posição conforme necessário
base.paste(media_invertida, (100, 1524-media_invertida.height-180+ajusty),media_invertida)

#Criando a barra dos dias
coordx= 200
altura = 55
base.paste(backside_dias, (coordx, 80-altura),backside_dias)  # ajuste a posição conforme necessário
base.paste(backside_dias_invertido, (223, 267-altura),backside_dias_invertido) 
base.paste(dias, (coordx, 80-altura),dias)  # ajuste a posição conforme necessário
base.paste(dias_invertido, (223, 267-altura),dias_invertido) 
base.paste(linha_tracejada, (410,359), linha_tracejada)
# Salva a imagem resultante
base.save(os.path.join(current_directory, 'images', 'imagem_final.png'))
base.show()