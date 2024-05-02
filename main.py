from PIL import Image,ImageOps, ImageDraw, ImageFont
import gerando_grafico_base, gerando_grafico_media_turma,backside_media_generator # importando para executar os codigos
import resize_image as ri

path_imagem_base = '/home/victor/Documents/TREZENTOS/images/base_graf.png'
path_imagem_media = '/home/victor/Documents/TREZENTOS/images/media_graf.png'
path_redimensionada = "/home/victor/Documents/TREZENTOS/images/media_graf_redimensionada.png"
path_backside = "/home/victor/Documents/TREZENTOS/images/backside_graf.png"
# Abrindo imagens
base = Image.open(path_imagem_base)
media = Image.open(path_imagem_media)
backside = Image.open(path_backside)

caixa_delimitadora_media = media.getbbox()

backside_invertido = ImageOps.flip(backside.crop(backside.getbbox()))

draw = ImageDraw.Draw(base)

# Defina a fonte e o tamanho do texto
font_path = "/home/victor/Documents/TREZENTOS/Poppins-Regular.ttf"
font_size = 24
font = ImageFont.truetype(font_path, font_size)

text1 = "Média da"
pos1 = (70, 1350)

text2 = "Turma"
pos2 = (85, 1375)
text_color = "#000000" #preto
# Adicione o texto à imagem
draw.text( pos1 , text1, fill=text_color, font=font)
draw.text( pos2 , text2, fill=text_color, font=font)
# Corte a imagem para a caixa delimitadora
media = media.crop(caixa_delimitadora_media)
media_invertida = ImageOps.flip(media)
ri.PNG_ResizeKeepTransparency(path_imagem_media,path_redimensionada,new_width=400,new_height=1040)
# Salve a imagem redimensionada
media = Image.open(path_redimensionada)

coordx = -75
coordy = gerando_grafico_base.resol*342

# Cole a segunda imagem na primeira
base.paste(backside, (coordx, 290),backside)  # ajuste a posição conforme necessário
base.paste(backside_invertido, (100, 1524-backside_invertido.height-180),backside_invertido)  # ajuste a posição conforme necessário
base.paste(media, (coordx, coordy),media)  # ajuste a posição conforme necessário
base.paste(media_invertida, (100, 1524-media_invertida.height-180),media_invertida)  # ajuste a posição conforme necessário


# Salve a imagem resultante
base.save('/home/victor/Documents/TREZENTOS/images/imagem_final.png')
base.show()