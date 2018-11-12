def filtra_input(loop, split = False, marker = ' '):
    '''
        filtra e separa inputs de acordo com a demanda
        loop   = nº de enters
        split  = devo separar o input
        marker = marcador ded separação
    '''

    function_out = []

    for i in range(loop):           # conta o número de strings inseridas
        console_in = input()
        function_out.append(console_in)

    if split:                       # checa se deve separar o input
        update_out = []
        for string in function_out:
            for substring in string.split(marker):
                update_out.append(substring)   
        function_out = update_out

    return function_out

def update_log(log, update, close_log = False):
    '''
        Retorna o log de erros atualizado
        Atualmente é uma string
    '''
    
    if log == "" :
        log = "ERROR:"

    log += "\n-> " + update

    if close_log:
        if log == "":
            log += "Tudo Suave, nenhum erro detectado."
        else:
            log += "\n -> Favor corrigir os erros acima."

    return log
