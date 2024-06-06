import os
import hashlib
import binascii

# Parâmetros da curva prime256v1 (secp256r1)
P = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
A = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
B = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
Gx = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
Gy = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162cb8b6fae4a13945d898c296
N = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

# Gera o inverso modular de k mod p
def inverso_mod(k, p):
    """ Retorna o inverso modular de k mod p. """
    if k == 0:
        raise ZeroDivisionError('divisão por zero')
    if k < 0:
        return p - inverso_mod(-k, p)
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quociente = old_r // r
        old_r, r = r, old_r - quociente * r
        old_s, s = s, old_s - quociente * s
        old_t, t = t, old_t - quociente * t
    return old_s % p

# Verifica se o ponto está na curva
def esta_na_curva(x, y):
    """ Verifica se o ponto está na curva. """
    return (y * y - x * x * x - A * x - B) % P == 0

# Adiciona os pontos na curva
def adicionar_pontos(ponto1, ponto2):
    """ Adiciona dois pontos na curva. """
    if ponto1 is None:
        return ponto2
    if ponto2 is None:
        return ponto1

    x1, y1 = ponto1
    x2, y2 = ponto2

    if x1 == x2 and y1 != y2:
        return None

    if x1 == x2:
        m = (3 * x1 * x1 + A) * inverso_mod(2 * y1, P)
    else:
        m = (y2 - y1) * inverso_mod(x2 - x1, P)

    x3 = m * m - x1 - x2
    y3 = m * (x1 - x3) - y1
    return (x3 % P, -y3 % P)

# Multiplica um escalar por um ponto na curva
def multiplicar_escalar(k, ponto):
    """ Multiplica um escalar por um ponto na curva. """
    resultado = None
    somando = ponto

    while k:
        if k & 1:
            resultado = adicionar_pontos(resultado, somando)
        somando = adicionar_pontos(somando, somando)
        k >>= 1

    return resultado

# Gera a chave privada
def gerar_chave_privada():
    """ Gera uma chave privada aleatória. """
    return int(binascii.hexlify(os.urandom(32)), 16) % N

# Gera a chave pública
def gerar_chave_publica(chave_privada):
    """ Gera a chave pública correspondente. """
    return multiplicar_escalar(chave_privada, (Gx, Gy))

# Criptografa a mensagem
def criptografar_mensagem(mensagem, chave_publica):
    """ Criptografa uma mensagem usando a chave pública do destinatário. """
    bytes_mensagem = mensagem.encode()
    k = gerar_chave_privada()
    R = multiplicar_escalar(k, (Gx, Gy))
    S = multiplicar_escalar(k, chave_publica)
    xS, _ = S

    # Use os 16 primeiros bytes de xS como chave para XOR
    chave_aes = hashlib.sha256(xS.to_bytes((xS.bit_length() + 7) // 8, byteorder='big')).digest()[:16]

    # Criptografa a mensagem usando XOR simples
    mensagem_criptografada = bytes(a ^ b for a, b in zip(bytes_mensagem, chave_aes))
    return (R, mensagem_criptografada)

# Descriptografa a mensagem
def descriptografar_mensagem(mensagem_criptografada, chave_privada):
    """ Descriptografa uma mensagem usando a chave privada do destinatário. """
    R, texto_cifrado = mensagem_criptografada
    S = multiplicar_escalar(chave_privada, R)
    xS, _ = S

    # Use os 16 primeiros bytes de xS como chave para XOR
    chave_aes = hashlib.sha256(xS.to_bytes((xS.bit_length() + 7) // 8, byteorder='big')).digest()[:16]

    # Descriptografa a mensagem usando XOR simples
    mensagem_descriptografada = bytes(a ^ b for a, b in zip(texto_cifrado, chave_aes))
    return mensagem_descriptografada.decode()

def principal():
    # Solicita ao usuário que insira uma mensagem
    mensagem = input("Digite uma mensagem para criptografar: ")

    # Gera as chaves do remetente
    chave_privada_remetente = gerar_chave_privada()
    chave_publica_remetente = gerar_chave_publica(chave_privada_remetente)
    print("Chave Privada do Remetente:", hex(chave_privada_remetente))
    print("Chave Pública do Remetente: (", hex(chave_publica_remetente[0]), ",", hex(chave_publica_remetente[1]), ")")

    # Gera as chaves do destinatário
    chave_privada_destinatario = gerar_chave_privada()
    chave_publica_destinatario = gerar_chave_publica(chave_privada_destinatario)
    print("Chave Privada do Destinatário:", hex(chave_privada_destinatario))
    print("Chave Pública do Destinatário: (", hex(chave_publica_destinatario[0]), ",", hex(chave_publica_destinatario[1]), ")")

    # Criptografa a mensagem com a chave pública do destinatário
    mensagem_criptografada = criptografar_mensagem(mensagem, chave_publica_destinatario)
    print("Mensagem Criptografada:", mensagem_criptografada)

    # Solicita ao usuário que insira a chave privada do destinatário
    Chv = int(input("Digite a chave privada do destinatário: "), 16)
    if(Chv==chave_privada_destinatario):
      #Descriptografa a mensagem com a chave privada do destinatário
      mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, Chv)
      print("Mensagem Descriptografada:", mensagem_descriptografada)

      # Verifica se a mensagem descriptografada é igual à mensagem original
      if mensagem_descriptografada == mensagem:
          print("Descriptografia bem-sucedida, a mensagem corresponde à original.")
      else:
          print("Descriptografia falhou, a mensagem não corresponde à original.")
    else:
        print("Erro! Decriptogração não autorizada!")


    #


i = 0
while(i==0):
    principal()
    print("Deseja testar outra mensagem? \n 0)Sim \n 1)Não")
    t = int(input())
    if(t==1):
        print("Desligando....")
        i = 1