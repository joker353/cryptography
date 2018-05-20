import random
import cv2
import binascii

seed = 123

random.seed(seed)

img = cv2.imread('gessler_code.png',-1)

pix = list(range(0, img.shape[0]*img.shape[1]))

buffer = []
message = []
decode = True


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    print(n)
    return int2bytes(n).decode(encoding, errors)


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


while decode and len(pix) > 0:
    pos = pix[random.randint(0, len(pix)-1)]
    pix.remove(pos)
    cr = pos // img.shape[0]
    cc = pos - (pos // img.shape[0]) * img.shape[0]
    print(img[cr, cc][0] & 0x01)
    buffer.append(img[cr, cc][0] & 0x01)
    if len(buffer) == 7:
        buffer = ''.join(map(str, buffer))
        print(buffer)
        val = text_from_bits(buffer)
        buffer = []
        print('val = ' + val )
        if ord(val) == 127:
            decode = False
        else:
            message.append(val)

message = ''.join(map(str, message))
print(message)


