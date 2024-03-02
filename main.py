import Crypto.Random
import Crypto.Util.number
import hashlib

  
# Parámetros para Alice y Bob
bits = 1024
e = 65537

# Alice
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
nA = pA * qA
phiA = (pA - 1) * (qA - 1)
dA = Crypto.Util.number.inverse(e, phiA)

# Bob
pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
nB = pB * qB
phiB = (pB - 1) * (qB - 1)
dB = Crypto.Util.number.inverse(e, phiB)

mensaje_original = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eu justo eu mauris hendrerit tincidunt nec a velit. Nam vel justo id urna efficitur rhoncus ac ac elit. Quisque dapibus quam vel justo dictum, vitae convallis odio ultricies. Etiam tincidunt, arcu eu tincidunt bibendum, eros mi consequat libero, eu dapibus arcu dolor ac ex. In hac habitasse platea dictumst. Nullam non libero nunc. In fringilla, orci a imperdiet semper, ligula neque cursus elit, at interdum tortor libero a libero. Ut commodo tellus nec felis sagittis, ut vestibulum urna vestibulum. Integer in libero non libero feugiat sagittis. Nunc bibendum lectus sit amet vestibulum accumsan. Fusce vel pharetra mauris. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus tincidunt orci vel malesuada vehicula. Phasellus vestibulum ligula sed felis dictum, id pharetra tortor rhoncus.Aenean auctor mi a justo posuere, ut vulputate velit bibendum. Proin vitae enim vitae dolor hendrerit ultrices. Curabitur ut orci vel elit fermentum tincidunt. Praesent pellentesque ligula nec turpis pharetra, non cursus elit ullamcorper. Integer ut ante eu leo congue iaculis vel vel turpis. Nullam suscipit malesuada turpis, sit amet commodo orci iaculis a. Morbi euism"  

#Dividir el mensaje en partes de 128 caracteres
partes_mensaje = [mensaje_original[i:i+128] for i in range(0, len(mensaje_original), 128)]

#Cifrar cada parte del mensaje con la llave pública de Bob

mensajes_cifrados = []
for parte in partes_mensaje:
    m = int.from_bytes(parte.encode(), 'big')
    c = pow(m, e, nB)
    mensajes_cifrados.append(c)


mensajes_descifrados = []
for cifrado in mensajes_cifrados:
    m = pow(cifrado, dB, nB)
    mensaje_descifrado = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
    mensajes_descifrados.append(mensaje_descifrado)


mensaje_recibido = ''.join(mensajes_descifrados)
print(mensaje_recibido)
hash_mensaje_original = hashlib.sha256(mensaje_original.encode()).hexdigest()
hash_mensaje_recibido = hashlib.sha256(mensaje_recibido.encode()).hexdigest()


if hash_mensaje_original == hash_mensaje_recibido:
  print("La autenticidad del mensaje ha sido verificada.")
else:
  print("La autenticidad del mensaje NO ha sido verificada.")









