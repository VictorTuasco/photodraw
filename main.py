import cv2
import os

def transformar_desenho (arquivo, qtd_filtro):
    img = cv2.imread(f'images/{arquivo}') # importa a imagem
    img_pb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #tranforma em preto e branco
    img_inverse = cv2.bitwise_not(img_pb)#inverte as cores da imagem
    img_blur =cv2.GaussianBlur(img_inverse, (qtd_filtro, qtd_filtro), 0)
    img_blur_inverse = cv2.bitwise_not(img_blur)
    img_desenho = cv2.divide(img_pb, img_blur_inverse, scale=256.0)

    cv2.imwrite(f'img_tratada/{arquivo}', img_desenho)

lista_arquivos = os.listdir('images')

for arquivo in lista_arquivos:
    transformar_desenho(arquivo, 55)