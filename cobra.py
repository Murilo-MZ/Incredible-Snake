from operator import truediv
import pygame
import time
import random


pygame.init()
pygame.mixer.init

nome = input("Digite seu Nome: ")
emailJogador = input("Digite seu email: ")


branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
 
dis_largura = 1280
dis_altura = 960
 
dis = pygame.display.set_mode((dis_largura, dis_altura))
pygame.display.set_caption('Jogo da cobrinha')
 
clock = pygame.time.Clock()
 
block_cobra = 10
velocidade_cobra = 20
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def jogo():
    while True:
        nome
        emailJogador
        f = open("registro.dat", "a")
        f.write("\n")
        f.write(nome)
        f.write("\n")
        f.write(emailJogador)
        f.write("\n")
        f.close()
        break
    
    
 
def Sua_Pontuação(Pontuação):
    valor = score_font.render("Pontuação: " + str(Pontuação), True, preto)
    dis.blit(valor, [0, 0])
 
 
 
def a_cobra(block_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(dis, preto, [x[0], x[1], block_cobra, block_cobra])
 
 
def mensagem(msg, cor):
    mesg = font_style.render(msg, True, cor)
    dis.blit(mesg, [dis_largura / 6, dis_altura / 3])
 
 
def loopJogo():
    

    acaba_jogo = False
    fecha_jogo = False
 
    x1 = dis_largura / 2
    y1 = dis_altura / 2
 
    x1_muda = 0
    y1_muda = 0
 
    lista_cobra = []
    Largura_Cobra = 1
 
    comidax = round(random.randrange(0, dis_largura - block_cobra) / 10.0) * 10.0
    comiday = round(random.randrange(0, dis_altura - block_cobra) / 10.0) * 10.0
    
    pygame.mixer.music.load("assets/SuperNintendo.wav")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)


 
    while not acaba_jogo:


        while fecha_jogo == True:


            
            dis.fill(vermelho)
            mensagem("Perdeu! Pressione ENTER para Jogar novamenteou ESC para sair", preto)
            Sua_Pontuação(Largura_Cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        acaba_jogo = True
                        fecha_jogo = False
                    if event.key == pygame.K_RETURN:
                        loopJogo()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                acaba_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_muda = -block_cobra
                    y1_muda = 0
                elif event.key == pygame.K_RIGHT:
                    x1_muda = block_cobra
                    y1_muda = 0
                elif event.key == pygame.K_UP:
                    y1_muda = -block_cobra
                    x1_muda = 0
                elif event.key == pygame.K_DOWN:
                    y1_muda = block_cobra
                    x1_muda = 0
 
        if x1 >= dis_largura or x1 < 0 or y1 >= dis_altura or y1 < 0:
            fecha_jogo = True
            pygame.mixer.music.load("assets/mortePacman.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)   
        x1 += x1_muda
        y1 += y1_muda
        dis.fill(verde)
        pygame.draw.rect(dis, vermelho, [comidax, comiday, block_cobra, block_cobra])
        cabeça_Cobra = []
        cabeça_Cobra.append(x1)
        cabeça_Cobra.append(y1)
        lista_cobra.append(cabeça_Cobra)
        if len(lista_cobra) > Largura_Cobra:
            del lista_cobra[0]
            
 
        for x in lista_cobra[:-1]:
            if x == cabeça_Cobra:
                fecha_jogo = True
                
 
        a_cobra(block_cobra, lista_cobra)
        Sua_Pontuação(Largura_Cobra - 1)
        
 
        pygame.display.update()
 
        if x1 == comidax and y1 == comiday:
            comidax = round(random.randrange(0, dis_largura - block_cobra) / 10.0) * 10.0
            comiday = round(random.randrange(0, dis_altura - block_cobra) / 10.0) * 10.0
            Largura_Cobra += 1
 
        clock.tick(velocidade_cobra)
 
    pygame.quit()
    quit()
 
 
jogo()
loopJogo()
