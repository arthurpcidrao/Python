import random
from datetime import datetime, timedelta

class Estacionamento:
    def __init__(self, linhas, colunas):
        self.matriz = [['' for _ in range(colunas)] for _ in range(linhas)]
        self.veiculos = {}
        self.estatisticas = {
            'vagas_totais': linhas * colunas,
            'vagas_ocupadas': 0,
            'turistas': 0,
            'total_faturado': 0,
            'quantidade_clientes': 0,
            'estatisticas_estado': {'Tocantins': 0, 'Mato Grosso': 0, 'Mato Grosso do Sul': 0}
        }

    def mostrar_interface(self):
        while True:
            print("\n### Interface do Estacionamento ###")
            print("1. Adicionar um carro")
            print("2. Remover um carro")
            print("3. Ver lista de carros")
            print("4. Ver estatísticas")
            print("5. Sair")

            opcao = input("Escolha uma opção: ").upper()

            if opcao == '1':
                placa = input("Digite a placa do veículo a ser adicionado: ").upper()
                while not self.validar_placa(placa):
                    print("Placa inválida. Tente novamente.")
                    placa = input("Digite a placa do veículo a ser adicionado: ").upper()
                self.entrada_veiculo(placa)
            elif opcao == '2':
                while True:
                    placa = input("Digite a placa do veículo a ser removido: ").upper()
                    if self.validar_placa(placa) and placa in self.veiculos:
                        self.saida_veiculo(placa)
                        break
                    else:
                        print("Placa inválida ou veículo não encontrado. Tente novamente.")
            elif opcao == '3':
                self.ver_lista_carros()
            elif opcao == '4':
                self.ver_estatisticas()
            elif opcao == '5':
                print("Saindo da interface.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def validar_placa(self, placa):
        # Verifica se a placa segue o padrão LLLNNNN ou LLLNLNN
        if len(placa) == 7 and placa[:3].isalpha() and placa[3:].isdigit():
            return True
        elif len(placa) == 7 and placa[:3].isalpha() and placa[3].isdigit() and placa[4].isalpha() and placa[5:].isdigit():
            return True

        return False

    def entrada_veiculo(self, placa, horario_entrada=None):
        if horario_entrada is None:
            horario_entrada = datetime.now()

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] == '':
                    self.matriz[i][j] = placa
                    self.veiculos[placa] = {'entrada': horario_entrada, 'posicao': (i, j)}
                    self.estatisticas['vagas_ocupadas'] += 1

                    estado = self.verificar_regiao(placa)
                    if estado:
                        self.estatisticas['estatisticas_estado'][estado] += 1
                    else:
                        self.estatisticas['turistas'] += 1

                    numero_vaga = self.obter_numero_vaga(i, j)
                    print(f"Veículo de placa {placa} estacionado na vaga '{numero_vaga}'")
                    return
        print("Estacionamento lotado. Não foi possível estacionar o veículo.")

    def saida_veiculo(self, placa):
        if placa in self.veiculos:
            entrada = self.veiculos[placa]['entrada']
            saida = datetime.now()
            tempo_estacionado = saida - entrada
            valor_cobrado = self.calcular_valor(tempo_estacionado.total_seconds() / 3600)
            posicao = self.veiculos[placa]['posicao']

            numero_vaga = self.obter_numero_vaga(*posicao)

            print(f"Veículo de placa {placa} saiu do estacionamento.")
            print(f"Tempo estacionado: {tempo_estacionado}")
            print(f"Valor a ser cobrado: R$ {valor_cobrado:.2f}")
            print(f"Vaga liberada: '{numero_vaga}'")

            estado = self.verificar_regiao(placa)
            if estado:
                self.estatisticas['estatisticas_estado'][estado] -= 1
            else:
                self.estatisticas['turistas'] -= 1

            self.matriz[posicao[0]][posicao[1]] = ''
            del self.veiculos[placa]
            self.estatisticas['vagas_ocupadas'] -= 1
            self.estatisticas['total_faturado'] += valor_cobrado
            self.estatisticas['quantidade_clientes'] += 1
        else:
            print(f"Veículo de placa {placa} não encontrado no estacionamento.")

    def calcular_valor(self, horas):
        tolerancia = 0.25
        valor_base = 5.00
        valor_hora_adicional = 2.00

        if horas <= tolerancia:
            return 0.00
        elif 0 < horas <= 3:
            return valor_base
        else:
            horas_adicionais = horas - 3
            return valor_base + valor_hora_adicional * (horas_adicionais // 1 + 1)

    def verificar_regiao(self, placa):
        regioes = {
            'Tocantins': [('MVL', 'MXG'), ('OLH', 'OLN'), ('OYA', 'OYC'), ('QKA', 'QKM'), ('QWA', 'QWF'), ('RSA', 'RSF')],
            'Mato Grosso': [('JXZ', 'KAU'), ('NIY', 'NJW'), ('NPC', 'NPQ'), ('NTX', 'NUG'), ('OAP', 'OBS'),
                            ('QBA', 'QCZ'), ('RAK', 'RAZ'), ('RRI', 'RRZ')],
            'Mato Grosso do Sul': [('HQF', 'HTW'), ('NRF', 'NSD'), ('OOG', 'OOU'), ('QAA', 'QAZ'), ('REW', 'REZ'),
                                   ('RWA', 'RWJ')]
        }

        prefixo = placa[:3]

        for estado, limites in regioes.items():
            for limite_inf, limite_sup in limites:
                if limite_inf <= prefixo <= limite_sup:
                    return estado

        return None

    def obter_numero_vaga(self, i, j):
        linhas, colunas = len(self.matriz), len(self.matriz[0])
        return i * colunas + j + 1

    def gerar_carros_exemplo(self, quantidade=50):
        for _ in range(quantidade):
            placa = self.gerar_placa_aleatoria()
            horario_entrada = self.gerar_horario_entrada_aleatorio()
            self.entrada_veiculo(placa, horario_entrada)

    def gerar_placa_aleatoria(self):
        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numeros = '0123456789'
        return f'{random.choice(letras)}{random.choice(letras)}{random.choice(letras)}' \
               f'{random.choice(numeros)}{random.choice(numeros)}{random.choice(numeros)}{random.choice(numeros)}'

    def gerar_horario_entrada_aleatorio(self):
        agora = datetime.now()
        delta_tempo = timedelta(minutes=random.randint(10, 240))
        return agora - delta_tempo

    def ver_lista_carros(self):
        print("\nLista de carros estacionados:")
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                placa = self.matriz[i][j]
                if placa:
                    numero_vaga = self.obter_numero_vaga(i, j)
                    print(f"Vaga '{numero_vaga}': Veículo de placa {placa}")

    def ver_estatisticas(self):
        vagas_disponiveis = self.estatisticas['vagas_totais'] - self.estatisticas['vagas_ocupadas']
        porcentagem_vagas_disponiveis = (vagas_disponiveis / self.estatisticas['vagas_totais']) * 100

        print("\n### Estatísticas do Estacionamento ###")
        print(f"Vagas Totais: {self.estatisticas['vagas_totais']}")
        print(f"Vagas Ocupadas: {self.estatisticas['vagas_ocupadas']}")
        print(f"Vagas Disponíveis: {vagas_disponiveis}")
        print(f"Porcentagem de Vagas Disponíveis: {porcentagem_vagas_disponiveis:.2f}%")
        print(f"Turistas (placas fora da região): {self.estatisticas['turistas']}")
        print(f"Média Faturada por Cliente: R$ {self.calcular_media_faturada():.2f}")
        print(f"Quantidade de Clientes Atendidos: {self.estatisticas['quantidade_clientes']}")
        print("\n### Estatísticas da Região ###")
        for estado, quantidade in self.estatisticas['estatisticas_estado'].items():
            print(f"{estado}: {quantidade} veículos")

    def calcular_media_faturada(self):
        if self.estatisticas['quantidade_clientes'] == 0:
            return 0.00
        return self.estatisticas['total_faturado'] / self.estatisticas['quantidade_clientes']

# Exemplo de uso:
estacionamento = Estacionamento(linhas=10, colunas=10)
for _ in range(50):
    placa = estacionamento.gerar_placa_aleatoria()
    horario_entrada = estacionamento.gerar_horario_entrada_aleatorio()
    estacionamento.entrada_veiculo(placa, horario_entrada)

# Mostrar a interface para interagir com os carros gerados
estacionamento.mostrar_interface()