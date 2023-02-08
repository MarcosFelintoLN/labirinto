from tkinter import *
import os
import time
from PIL import ImageTk, Image


labirinto = [    
    ['1','1','1','1','1','1','1','1','1','1'],
    ['1','0','1','0','0','0','0','0','0','1'],
    ['1','0','1','1','0','1','1','1','0','1'],
    ['1','0','0','0','0','0','0','0','0','1'],
    ['1','0','1','1','1','1','0','1','0','1'],
    ['1','0','0','0','0','1','0','0','0','1'],
    ['1','1','1','1','1','1','0','1','1','1'],
]


saida = (0,1)
chegada = (6,6)

direcao_linha = [1, -1, 0, 0]
direcao_coluna = [0, 0, 1, -1]

pilha = [saida]

casa_visitada = [[False for j in range(len(labirinto[0]))] for i in range(len(labirinto))]
casa_visitada[saida[0]][saida[1]] = True

# Define a variável para armazenar o caminho
caminho = []

while pilha:
    atual = pilha.pop()

    caminho.append(atual)

    if atual == chegada:
        break

    for i in range(4):
        nova_linha = atual[0] + direcao_linha[i]
        nova_coluna = atual[1] + direcao_coluna[i]
        if 0 <= nova_linha < len(labirinto) and 0 <= nova_coluna < len(labirinto[0]) and not casa_visitada[nova_linha][nova_coluna] and labirinto[nova_linha][nova_coluna] != '1':
            pilha.append((nova_linha, nova_coluna))
            casa_visitada[nova_linha][nova_coluna] = True 

    for i in range(len(caminho)):
        x, y = caminho[i]
        labirinto[x][y] = '.'

    for linha in labirinto:
        print(linha)
        

# Verifica se o caminho foi encontrado ou não
if caminho[-1] == chegada:
    print("Caminho encontrado: ", caminho)
else:
    print("Caminho não encontrado.")
    
caminho1 = caminho[0]
posicaoinicialx = caminho1[1]
posicaoinicialy = caminho1[0]
posicaoratox = (caminho1[1])*40
posicaoratoy = (caminho1[0])*40
movimento = caminho

class Rato:
    def __init__(self, cordX, cordY, imageRato, canvas):
        self.cordX = cordX
        self.cordY = cordY
        self.imageRato = imageRato
        self.canvas = canvas

        RatoEnv = self.canvas.create_image(
            self.cordX, self.cordY, image=self.imageRato, anchor=NW
        )

        self.image = RatoEnv

class App(object):
    def __init__(self, app, labirinto, **kwargs):
        self.labirinto = labirinto
        self.app = app
        self.canvas = Canvas(self.app, width=520, height=640)
        self.canvas.pack()

        global imageRato
        global imageQueijo

        imageRato = ImageTk.PhotoImage(Image.open("rato.png").resize((30, 30)))
        imageQueijo = ImageTk.PhotoImage(Image.open("queijo.png").resize((30, 30)))
        
        for row in range(len(self.labirinto)):
            for col in range(len(self.labirinto[0])):
                if self.labirinto[row][col] == '1':
                    self.canvas.create_rectangle(
                        col * 40, row * 40, (col + 1) * 40, (row + 1) * 40, fill="black"
                    )
                else:
                    pass
        
        rato = Rato(posicaoratox, posicaoratoy, imageRato, self.canvas)                
        queijo = self.canvas.create_image(245, 250, image=imageQueijo, anchor=NW)

        posicaoinit = movimento[0]
        inicial1 = posicaoinit[1]
        inicial2 = posicaoinit[0]
        size = len(movimento)
        
        for index in range(1, size):
            posicao = movimento[index]
            posX = posicao[1]
            posY = posicao[0]

            if posY > inicial2 and posX == inicial1:
                x = 0
                y = 40
                inicial1 = posX
                inicial2 = posY

            elif posY < inicial2 and posX == inicial1:
                x = 0
                y = -40
                inicial1 = posX
                inicial2 = posY
                
            elif posY == inicial2 and posX > inicial1:
                x = 40
                y = 0
                inicial1 = posX
                inicial2 = posY

            elif posY == inicial2 and posX < inicial1:
                x = -40
                y = 0
                inicial1 = posX
                inicial2 = posY
                
            self.canvas.move(rato.image, x, y)
            root.update()
            time.sleep(0.5)
        
root = Tk()
app = App(root, labirinto)
root.mainloop()