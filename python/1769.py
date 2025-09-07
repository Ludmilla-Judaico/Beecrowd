def verificador_1(cpf:str) -> bool:
    """Analisa o cpf e verifica se o 1º dígito
    verificador é válido"""
    soma = 0
    for i in range(1, 10):
        soma += int(cpf[i - 1]) * i
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