from PIL import Image,ImageOps, ImageDraw, ImageFont
import gerando_grafico_base, gerando_grafico_media_turma,backside_media_generator # importando para executar os codigos
import resize_image as ri

path_imagem_base = '/home/victor/Documents/TREZENTOS/images/base_graf.png'
path_imagem_media = '/home/victor/Documents/TREZENTOS/images/media_graf.png'
path_redimensionada = "/home/victor/Documents/TREZENTOS/images/media_graf_redimensionada.png"
path_backside_media = "/home/victor/Documents/TREZENTOS/images/backside_media_graf.png"
path_backside_dias = "/home/victor/Documents/TREZENTOS/images/backside_dias_graf.png"

# Abrindo imagens
base = Image.open(path_imagem_base)
media = Image.open(path_imagem_media)
backside_media = Image.open(path_backside_media)
backside_media_invertido = ImageOps.flip(backside_media.crop(backside_media.getbbox()))
backside_dias = Image.open(path_backside_dias)
backside_dias_invertido = ImageOps.flip(backside_dias.crop(backside_dias.getbbox()))

draw = ImageDraw.Draw(base)

# Define a fonte e o tamanho do texto
font_path = "/home/victor/Documents/TREZENTOS/Poppins-Regular.ttf"
font_size = 24
font1 = ImageFont.truetype(font_path, font_size)

font_size = 40
font2 = ImageFont.truetype(font_path, font_size)

text1 = "Média da"
pos1 = (70, 1350)

text2 = "Turma"
pos2 = (85, 1375)

text3 = "Cálculo 1 com Professor Ricardo Ramos Fragelli"
pos3 = (300+400, 75)

text4 = "1 semestre de 2024 - Segunda prova"
pos4 = (350+450, 125)

text_color = "#000000" #preto
# Adiciona o texto à imagem
draw.text( pos1 , text1, fill=text_color, font=font1)
draw.text( pos2 , text2, fill=text_color, font=font1)
draw.text( pos3 , text3, fill=text_color, font=font2)
draw.text( pos4 , text4, fill=text_color, font=font2)


# Corta a imagem para a caixa delimitadora
media = media.crop(media.getbbox())
media_invertida = ImageOps.flip(media)
ri.PNG_ResizeKeepTransparency(path_imagem_media,path_redimensionada,new_width=400,new_height=1040)
# Salva a imagem redimensionada
media = Image.open(path_redimensionada)

coordx = -75
coordy = gerando_grafico_base.resol*342

# Criando a barra da média da turma
base.paste(backside_media, (coordx, 290),backside_media)  # ajuste a posição conforme necessário
base.paste(backside_media_invertido, (100, 1524-backside_media_invertido.height-180),backside_media_invertido)  # ajuste a posição conforme necessário
base.paste(media, (coordx, coordy),media)  # ajuste a posição conforme necessário
base.paste(media_invertida, (100, 1524-media_invertida.height-180),media_invertida)  # ajuste a posição conforme necessário

#Criando a barra dos dias


# Salva a imagem resultante
base.save('/home/victor/Documents/TREZENTOS/images/imagem_final.png')
base.show()