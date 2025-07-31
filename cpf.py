import random
#Esse código verifica se um CPF está correto de acordo com o algoritmo de criação de CPFs da Receita Federal
#funções
def verificador_1(cpf:str) -> bool:
    """Analisa o cpf e verifica se o 1º dígito
    verificador é válido"""
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if(resto == 0) or (resto == 1):
        if(cpf[9] == 0):
            return True
        else:
            return False
    else:
        verif = str(11 - resto)
        if(verif == cpf[9]):
            return True
        else:
            return False
        
def verificador_2(cpf:str) -> bool:
    """Analisa o cpf e verifica se o 2º dígito
        verificador é válido"""
    soma = 0
    for i in range(1, 10):
        soma += int(cpf[i]) * (10 - (i - 1))
    resto = soma % 11
    if(resto == 0) or (resto == 1):
        if(cpf[10] == 0):
            return True
        else:
            return False
    else:
        verif = str(11 - resto)
        if(verif == cpf[10]):
            return True
        else:
            return False
        
def cpf_verdadeiro(cpf:str) -> str:
    if(verificador_1(cpf)) and (verificador_2(cpf)):
        msg = 'Este cpf é válido'
    else:
       msg = 'Este cpf não é válido'
    return msg


def gerar_cpf() -> str:
    """Gera um cpf verificado"""
    nums = [random.randint(0, 9) for i in range(9)]
    cpf = ''.join(str(i) for i in nums)
    soma = 0
    for i in range(9):
        soma += nums[i] * (10 - i)
    #d1    
    resto = soma % 11
    if(resto == 0) or (resto == 1):
        cpf += '0'
    else:
        verif = 11 - resto
        cpf += str(verif)
    soma = 0
    #d2
    for i in range(1, 10):
        soma += int(cpf[i]) * (10 - (i - 1))
    resto = soma % 11
    if(resto == 0) or (resto == 1):
        cpf += '0'
    else:
        verif = 11 - resto
        cpf += str(verif)

    cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    return cpf

#main
cpf = input('Informe um CPF(sem pontos ou hífens): ')
print(cpf_verdadeiro(cpf))

qntd = int(input('Informe quantos CPFs deseja gerar: '))
for i in range(qntd):
    print(gerar_cpf())