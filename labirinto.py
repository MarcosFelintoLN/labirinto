from tkinter import *
import os
import time
from PIL import ImageTk, Image


# Define o labirinto como uma matriz
labirinto = [    
    ['1','1','1','1','1','1','1','1','1','1'],
    ['1','0','0','0','0','0','0','0','0','1'],
    ['1','0','1','1','1','1','1','1','0','1'],
    ['1','0','0','0','0','0','0','0','0','1'],
    ['1','0','1','0','1','1','1','1','0','1'],
    ['1','0','0','0','0','1','0','0','0','1'],
    ['1','1','1','1','1','1','C','1','1','1']
]

# Define a posição inicial e a posição final
saida = (0,1)
chegada = (6,6)

# Define a direção para cada movimento
direcao_linha = [1, -1, 0, 0]
direcao_coluna = [0, 0, 1, -1]

# Define a pilha para armazenar o caminho
pilha = [saida]

# Define a matriz para marcar os lugares visitados

casa_visitada = [[False for j in range(len(labirinto[0]))] for i in range(len(labirinto))]
casa_visitada[saida[0]][saida[1]] = True

# Define a variável para armazenar o caminho
caminho = []

while pilha:
    # Pega a última posição na pilha
    atual = pilha.pop()

    # Adiciona a posição atual ao caminho
    caminho.append(atual)

    # Se a posição atual é o final, interrompe o loop
    if atual == chegada:
        break

    # Verifica os próximos movimentos possíveis
    for i in range(4):
        nova_linha = atual[0] + direcao_linha[i]
        nova_coluna = atual[1] + direcao_coluna[i]
        if 0 <= nova_linha < len(labirinto) and 0 <= nova_coluna < len(labirinto[0]) and not casa_visitada[nova_linha][nova_coluna] and labirinto[nova_linha][nova_coluna] != '1':
            pilha.append((nova_linha, nova_coluna))
            casa_visitada[nova_linha][nova_coluna] = True 

    # Atualiza o labirinto com o caminho percorrido até o momento
    '''for i in range(len(caminho)):
        x, y = caminho[i]
        labirinto[x][y] = '0' '''

    # Imprime o labirinto atualizado com o caminho
    '''for linha in labirinto:
        print(linha)'''
        

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
        posicaoinicial1 = posicaoinit[1]
        posicaoinicial2 = posicaoinit[0]
        size = len(movimento)
        
        for index in range(1, size):
            posicao = movimento[index]
            posicaoX = posicao[1]
            posicaoY = posicao[0]

            if posicaoY > posicaoinicial2 and posicaoX == posicaoinicial1:
                x = 0
                y = 40
                posicaoinicial1 = posicaoX
                posicaoinicial2 = posicaoY

            if posicaoY < posicaoinicial2 and posicaoX == posicaoinicial1:
                x = 0
                y = -40
                posicaoinicial1 = posicaoX
                posicaoInicial2 = posicaoY
                
            if posicaoY == posicaoinicial2 and posicaoX > posicaoinicial1:
                x = 40
                y = 0
                posicaoinicial1 = posicaoX
                posicaoInicial2 = posicaoY

            if posicaoY == posicaoinicial2 and posicaoX < posicaoinicial1:
                x = -40
                y = 0
                posicaoinicial1 = posicaoX
                posicaoinicial2 = posicaoY
                
            self.canvas.move(rato.image, x, y)
            root.update()
            time.sleep(0.5)
        
root = Tk()
app = App(root, labirinto)
root.mainloop()