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

def inverse_mod(k, p):
    """ Retorna o inverso modular de k mod p. """
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        return p - inverse_mod(-k, p)
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s % p

def is_on_curve(x, y):
    """ Verifica se o ponto está na curva. """
    return (y * y - x * x * x - A * x - B) % P == 0

def point_add(point1, point2):
    """ Adiciona dois pontos na curva. """
    if point1 is None:
        return point2
    if point2 is None:
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 != y2:
        return None

    if x1 == x2:
        m = (3 * x1 * x1 + A) * inverse_mod(2 * y1, P)
    else:
        m = (y2 - y1) * inverse_mod(x2 - x1, P)

    x3 = m * m - x1 - x2
    y3 = m * (x1 - x3) - y1
    return (x3 % P, -y3 % P)

def scalar_mult(k, point):
    """ Multiplica um escalar por um ponto na curva. """
    result = None
    addend = point

    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1

    return result

def generate_private_key():
    """ Gera uma chave privada aleatória. """
    return int(binascii.hexlify(os.urandom(32)), 16) % N

def generate_public_key(private_key):
    """ Gera a chave pública correspondente. """
    return scalar_mult(private_key, (Gx, Gy))

def encrypt_message(message, public_key):
    """ Criptografa uma mensagem usando a chave pública do destinatário. """
    message_bytes = message.encode()  # converte a string em uma sequência de bytes
    k = generate_private_key()
    R = scalar_mult(k, (Gx, Gy))
    S = scalar_mult(k, public_key)
    xS, _ = S

    # Use os 16 primeiros bytes de xS como chave para XOR
    aes_key = hashlib.sha256(xS.to_bytes((xS.bit_length() + 7) // 8, byteorder='big')).digest()[:16]

    # Criptografa a mensagem usando XOR simples
    encrypted_message = bytes(a ^ b for a, b in zip(message_bytes, aes_key))
    return (R, encrypted_message)

def decrypt_message(encrypted_message, private_key):
    """ Descriptografa uma mensagem usando a chave privada do destinatário. """
    try:
        R, ciphertext = encrypted_message  # redireciona a tupla, R é o ponto e ciphertext é a mensagem criptografada
        S = scalar_mult(private_key, R)
        xS, _ = S

        # Use os 16 primeiros bytes de xS como chave para XOR
        aes_key = hashlib.sha256(xS.to_bytes((xS.bit_length() + 7) // 8, byteorder='big')).digest()[:16]

        # Descriptografa a mensagem usando XOR simples
        decrypted_message = bytes(a ^ b for a, b in zip(ciphertext, aes_key)) #zip cria uma tupla
        return decrypted_message.decode()  # retorna de bytes para texto
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None

def main():
    # Solicita ao usuário que insira uma mensagem
    message = input("Enter a message to encrypt: ")

    # Gera as chaves do remetente
    sender_private_key = generate_private_key()
    sender_public_key = generate_public_key(sender_private_key)
    print("Sender Private Key:", hex(sender_private_key))
    print("Sender Public Key: (", hex(sender_public_key[0]), ",", hex(sender_public_key[1]), ")")

    # Gera as chaves do destinatário
    receiver_private_key = generate_private_key()
    receiver_public_key = generate_public_key(receiver_private_key)
    print("Receiver Private Key:", hex(receiver_private_key))
    print("Receiver Public Key: (", hex(receiver_public_key[0]), ",", hex(receiver_public_key[1]), ")")

    # Criptografa a mensagem com a chave pública do destinatário
    encrypted_message = encrypt_message(message, receiver_public_key)
    print("Encrypted Message:", encrypted_message)

    # Solicita as chaves necessárias para a descriptografia
    receiver_private_key_input = int(input("Enter the receiver's private key in hex: "), 16)
    sender_public_key_input_x = int(input("Enter the sender's public key X in hex: "), 16)
    sender_public_key_input_y = int(input("Enter the sender's public key Y in hex: "), 16)
    sender_public_key_input = (sender_public_key_input_x, sender_public_key_input_y)

    # Descriptografa a mensagem com a chave privada do destinatário
    decrypted_message = decrypt_message(encrypted_message, receiver_private_key_input)
    if decrypted_message is None:
        print("Failed to decrypt the message.")
    else:
        if decrypted_message == message:
            print("Decrypted Message:", decrypted_message)
            print("Descriptografia feita com sucesso")
        else:
            print("Decrypted Message:", decrypted_message)
            print("Descriptografia errada! A chave está incorreta")

    
main()
