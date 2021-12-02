def separar(ip_usuario):
    quadrantes = ip_usuario.split('.')
    quadrantes = {
        'q1': quadrantes[0],
        'q2': quadrantes[1],
        'q3': quadrantes[2],
        'q4': quadrantes[3]

    }

    return quadrantes


def descobrir_binarios(valor):
    quadrantes_binarios = []

    for i, v in valor.items():
        bits = 8
        num = str(bin(int(v)))
        num = num.replace('0b', '')
        num = '0' * (bits-len(num)) + num
        quadrantes_binarios.append(num)

    return quadrantes_binarios


def descobrir_mascara_bin(valor):
    mascara_binario = ''
    for i in range(32):  # 32 bits
        if i < valor:
            mascara_binario += '1'
            if i == 7 or i == 15 or i == 23:
                mascara_binario += '.'

        if i >= valor:
            mascara_binario += '0'
            if i == 7 or i == 15 or i == 23:
                mascara_binario += '.'

    return mascara_binario


def calc_mascara(valor):
    binarios = (128, 64, 32, 16, 8, 4, 2, 1)
    quadrantes = valor.split('.')
    enderecos = {}

    for quadrante in range(len(quadrantes)):
        soma = 0
        aux = 0

        if quadrante == 0:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
            enderecos['q1'] = soma

        if quadrante == 1:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
            enderecos['q2'] = soma

        if quadrante == 2:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
            enderecos['q3'] = soma

        if quadrante == 3:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
            enderecos['q4'] = soma

    return enderecos


def descobrir_rede(var, cidr):
    ip = descobrir_binarios(separar(var))
    ip = ''.join(ip)
    ip = list(ip)

    for i in range(len(ip)):
        if i >= cidr:
            ip[i] = '0'

    ip = ''.join(ip)

    binario = ''
    for i in range(len(ip)):
        binario += ip[i]
        if i == 7 or i == 15 or i == 23:
            binario += '.'

    binarios = (128, 64, 32, 16, 8, 4, 2, 1)
    quadrantes = binario.split('.')

    enderecos = {}

    for quadrante in range(len(quadrantes)):
        soma = 0
        aux = 0

        if quadrante == 0:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
                else:
                    aux += 1
            enderecos['q1'] = soma

        if quadrante == 1:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
                else:
                    aux += 1
            enderecos['q2'] = soma

        if quadrante == 2:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
                else:
                    aux += 1

            enderecos['q3'] = soma

        if quadrante == 3:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
                else:
                    aux += 1

            enderecos['q4'] = soma
    return enderecos


def descobrir_broadcast(var, cidr):
    ip = descobrir_binarios(separar(var))
    ip = ''.join(ip)
    ip = list(ip)

    for i in range(len(ip)):
        if i >= cidr:
            ip[i] = '1'

    ip = ''.join(ip)

    binario = ''
    for i in range(len(ip)):
        binario += ip[i]
        if i == 7 or i == 15 or i == 23:
            binario += '.'

    binarios = (128, 64, 32, 16, 8, 4, 2, 1)
    quadrantes = binario.split('.')

    enderecos = {}

    for quadrante in range(len(quadrantes)):
        soma = 0
        aux = 0

        if quadrante == 0:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
                else:
                    aux += 1
            enderecos['q1'] = soma

        if quadrante == 1:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
                else:
                    aux += 1
            enderecos['q2'] = soma

        if quadrante == 2:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
                else:
                    aux += 1

            enderecos['q3'] = soma

        if quadrante == 3:
            for i in quadrantes[quadrante]:
                if i == '1':
                    soma += binarios[int(aux)]
                    aux += 1
                else:
                    aux += 1

            enderecos['q4'] = soma

    return enderecos
