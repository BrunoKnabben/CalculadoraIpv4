from calc_ipv4 import CalcIpv4
from sys import exit

menu = 0

while not menu == 3:
    print('\t-= CALCULADORA IPV4 =-\t')
    print('\nOPÇÕES:')
    print('\t[1] Calcular informando MÁSCARA')
    print('\t[2] Calcular informando CIDR')
    print('\t[3] Sair')

    try:
        menu = int(input('\n'))
    except ValueError:
        print('Opção inválida.')

    if menu == 1:
        ip = str(input('IP: '))
        mascara = str(input('MÁSCARA: '))
        print('\n\n\n\n\n\n\n\n')

        ipv4 = CalcIpv4(ip=ip, mascara=mascara)

        if not ipv4.autenticador():
            print('Erro! Verifique os dados informados.')
        else:
            ipv4.switch()
            print('IP:', ipv4.ip)
            print('CIDR:', ipv4.descobrir_cidr())
            print('MÁSCARA:', ipv4.mascara)
            print("IP's DISPONÍVEIS:", ipv4.descobrir_numero_ips())
            print('REDE:', ipv4.descobrir_ip_rede())
            print('BROADCAST:', ipv4.descobrir_broadcast())
            print()

    if menu == 2:
        ip = str(input('IP: '))
        cidr = int(input('CIDR: '))
        print('\n\n\n\n\n\n\n\n')

        ipv4 = CalcIpv4(ip=ip, cidr=cidr)

        if not ipv4.autenticador():
            print('Erro! Verifique os dados informados.')
        else:
            ipv4.switch()
            print('IP:', ipv4.ip)
            print('CIDR:', ipv4.cidr)
            print('MÁSCARA:', ipv4.descobrir_mascara())
            print("IP's DISPONÍVEIS:", ipv4.descobrir_numero_ips())
            print('REDE:', ipv4.descobrir_ip_rede())
            print('BROADCAST:', ipv4.descobrir_broadcast())
            print()

    if menu == 3:
        exit()
