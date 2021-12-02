from separar_ip import separar, descobrir_binarios, descobrir_mascara_bin, calc_mascara
from separar_ip import descobrir_rede, descobrir_broadcast


class CalcIpv4:
    def __init__(self, ip=None, cidr=None, mascara=None):
        self.ip = ip
        self.cidr = cidr
        self.mascara = mascara
        self.numeros_ips = 0
        self.ip_da_rede = 0
        self.ip_broadcast = 0
        self.binarios = (128, 64, 32, 16, 8, 4, 2, 1)  # Utilizados para conversão de decimal para binário

    def switch(self):
        if self.cidr is None:
            self.descobrir_cidr()

        if self.mascara is None:
            self.descobrir_mascara()

    def autenticador(self):  # Verifica se foi fornecido um IP e pelo menos um CIDR ou máscara
        if self.ip is None:
            return False

        if self.mascara is None and self.cidr is None:
            return False

        return True

    def descobrir_cidr(self):
        mascara_subrede_bin = descobrir_binarios(separar(self.mascara))

        cidr = 0
        for quadrante in mascara_subrede_bin:
            for num in quadrante:
                if num == '1':
                    cidr += 1

        self.cidr = cidr
        return cidr

    def descobrir_mascara(self):
        aux = calc_mascara(descobrir_mascara_bin(self.cidr))
        mascara_subrede = ''

        for i in range(len(aux)):
            mascara_subrede += str(aux[f'q{i + 1}'])
            if i != 3:
                mascara_subrede += '.'

        self.mascara = mascara_subrede
        return mascara_subrede

    def descobrir_numero_ips(self):
        ips_disponiveis = (2 ** (32 - self.cidr)) - 2

        self.numeros_ips = ips_disponiveis
        return ips_disponiveis

    def descobrir_ip_rede(self):
        ip = descobrir_rede(self.ip, self.cidr)
        ip_rede = ''

        for i in range(len(ip)):
            ip_rede += str(ip[f'q{i + 1}'])
            if i != 3:
                ip_rede += '.'

        self.ip_da_rede = ip_rede
        return ip_rede

    def descobrir_broadcast(self):
        ip = descobrir_broadcast(self.ip, self.cidr)
        ip_broad = ''

        for i in range(len(ip)):
            ip_broad += str(ip[f'q{i + 1}'])
            if i != 3:
                ip_broad += '.'

        self.ip_broadcast = ip_broad
        return ip_broad

