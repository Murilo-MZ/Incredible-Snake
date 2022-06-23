# Incredible-Snake
Snake Game


Bernardo Menegaz Corral - 1130199 - Bernardo18072003@gmail.com

Murilo Macedo Zanette - 1127846 - murilozanette888@gmail.com 

Para nosso projeto de Game 2d, nos baseamos em códigos de alguns projetos de ‘snake games’ que encontramos na internet, tendo uma metodologia similar a trabalhada em sala de aula. Em nosso jogo da cobrinha, é game over quando a cobra atinge os limites da tela. Além disso, adicionamos efeitos sonoros tais como: uma música de ambientação correspondente a temática proposta, além de sons referentes a ‘morte’ da cobra, e a cada ponto ganho. Adicionamos também, uma tela para o display do jogo, juntamente com um contador para pontos acumulados.
  
Commits

Após a instalação do pygame, a primeira coisa para nosso projeto funcionar foi a criação da tela. Para a criação da tela, foi necessário utilizar a função display.set_mode(). Além das funções init() e quit() que servem para abrir e fechar o jogo (início e final de código). Foram utilizadas também as funções: update() que serve para atualizar quaisquer alterações ocorridas no jogo e flip(), que funciona de maneira semelhante à função update(). A diferença é que o método update() atualiza apenas as alterações feitas (no entanto, se nenhum parâmetro for passado, atualiza a tela completa), mas o método flip() refaz a tela completa novamente. Assim a tela aparecerá, mas se encerra segundos depois. Para resolver isso, utilizamos um while loop. Assim, a tela não se encerra logo em seguida, e a partir daí, usamos a função event.get(), e setamos o nome do jogo como “Incredible Snake”, usando o display.set_caption().

Depois que a tela foi finalizada, mudamos a cor de exibição do preto (padrão) para branco, usando a função fill(). Fizemos com que a cobra funcionasse, criando as variáveis de cor para a tela, comida e a cobra. Fizemos a cobra de forma retangular usando a função draw.rect() que ajudou a criar o tamanho e cor certos. Para mover a cobra, utilizamos a classe keydown do pygame, que são:  K_UP, K_DOWN, K_LEFT e K_RIGHT, para fazer a cobrinha se mexer para cima, baixo, esquerda e direita, respectivamente. E criamos novas variáveis: x1_muda e y1_muda para a atualização das coordenadas x e y.
Como citado anteriormente, no “Incredible Snake”, se o usuário atingir as bordas da tela, ele perde. Para especificar isso, usamos a função 'if' para definir os limites das coordenadas x e y da cobra serem menores ou iguais às da tela.

A partir daqui, adicionamos a comida à tela, além de incluir a opção de jogar novamente ou sair do jogo quando o usuário perder. Em sequência, trabalhamos no código de aumentar o corpo da cobra ao comer a comida, além de fazer com que, se a cobra colidir com o próprio corpo o jogo acaba. E por último, criamos a pontuação do jogador. Para fazer isso, criamos a def Sua_Pontuação(), que mostrará, basicamente, o comprimento da cobra subtraído por 1 que é o tamanho inicial da cobra.
