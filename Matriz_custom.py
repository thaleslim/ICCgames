def gerar_matriz (linhas, colunas, valor_inicial = '', fill = False):
    '''
        Gera uma matriz, representada por uma lista de listas,
        de tamanho linhas X colunas; opcionalmente preenchida
        com algum valor inicial.

        Default valor inicial = ''
        Fill decide se: True  -> os valores serão copiados à matriz resultante [dimensão (linha,colunas) mantida]
                        False -> será usada como valor_inicial [aumenta o nº de colunas por linha, ou seja, mais dimensões]
        Exemplo:
                print(gerar_matriz(3,3,gerar_matriz(3,3,1),False))
        TODO: comment
    '''
    
    matriz = []
    if fill and type(valor_inicial) == list:
        matriz = valor_inicial.copy()
        if len(matriz) and type(matriz[0]) == list:
            proceed = True
            for linha in matriz:
                if type(linha) != list:
                    proceed = False
                    break
                elif len(linha) < colunas:
                    for i in range(colunas - len(linha)):
                        linha.append('')
            
            if not proceed:
                return None
            elif len(matriz) < linhas:
                for i in range(linhas - len(matriz)):
                    matriz.append(['']*colunas)

            # filtrar excesso
            matriz = matriz[0:linhas]
            for i in range(len(matriz)):
                matriz[i] = matriz[i][0:colunas]
            
    else:
        for i in range(linhas):
            matriz.append([valor_inicial]*colunas)

    return matriz

def imprime_matriz(matriz):
    '''
        Considerando matriz como uma lista de listas, imprime no IDLE
    '''
    i = 0
    for linha in matriz:
        i += 1
        print(' ')
        j = 0
        for coluna in linha:
            j += 1
            print(' ', end='')
            print(coluna, end='')
            if j < len(linha):
                print(' |', end='')
        if i < len(matriz):
            print('\n ', end='')
            print('_'*(len(linha)*len(matriz)))
    print()

def matriz_quadrada (matriz):
    if len(matriz) == 0:
        return False
    
    check = len(matriz)
    
    for linhas in matriz:
        if len(linhas) != check:
            return False

    return True

import pygame

def draw_matriz(draw_size: "Matrix(nº lines, nº columns)", rect: "(width,height,RGBcolor)" = (0,0,(0,0,0)), screen_size: "(screen_width,screen_height)" = (-1,-1), split:"(height,RGBcolor)" = (10,(88, 11, 28)) ):
    '''
    Desenha no pygame.Surface uma matriz representada com pygame.Rect e linhas
    
    args:
        draw_size: tuple = Dimensões da matriz representada
        screen_size: tuple = Area a ser usada do display
        rect: tuple = Design de cada elemento da matriz
        split: tuple = Design dos separadores de cada rect

    Retorna uma lista de listas com todas as posições dos pygame.Rect impressos
    '''

    if not pygame.display.get_init():
        print("ERROR: display unitialized")
        return None
    
    screen = pygame.display.get_surface()   # Game display

    if screen == None:  # If no display mode has been set
        return None
    
    if screen_size[0] == -1:
        info = pygame.display.Info()
        screen_size = (info.current_w, info.current_h)

    width = rect[0]
    height = rect[1]
    rect_color = rect[2]

    split_width = split[0]
    split_color = split[1]

    x_inicial = x = 0
    y_inicial = y = 0
    
    if draw_size[0] % 2 != 0:
        # TODO: lógica x par
    #else:
                    #       display width                       colunas
        x_inicial = x =  screen_size[0] // 2  - width  // 2 - draw_size[1] // 2 * ( width + split_width )

    if draw_size[1] % 2 != 0:
        # TODO: lógica y par
    #else:
        y_inicial = y =  screen_size[1] // 2  - height // 2 - draw_size[0] // 2 * ( height + split_width )
                    #       display height                      linhas

    # TODO: x_inicial ou y_inicial estiverem fora do mapa, resize

    result = []
    
    for linha in range(draw_size[0]):
        result.append([])
        for coluna in range(draw_size[1]):
            if width != 0 and height != 0:
                pygame.draw.rect(screen, rect_color, (x, y, width, height))
                result[linha].append((x,y))
            
            if coluna < draw_size[1]-1:
                pygame.draw.line(screen, split_color, (x + width + 4, y), (x + width + 4, y + height - 1), split_width)
                x += width + split_width
            else:
                x += width
        
        if linha < draw_size[0]-1:
            pygame.draw.line(screen, split_color, (x_inicial, y + height + 4), (x - 1, y + height + 4), split_width)

        y += height + split_width
        x = x_inicial
    y = y_inicial

    return result
