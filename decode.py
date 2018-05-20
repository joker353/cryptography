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


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


while len(pix) > 0:
    pos = pix[random.randint(0, len(pix)-1)]
    pix.remove(pos)
    cr = pos // img.shape[0]
    cc = pos - (pos // img.shape[0]) * img.shape[0]
    buffer.append(img[cr, cc][0] & 0x01)
    if len(buffer) == 8:
        buffer = ''.join(map(str, buffer))
        n = int(buffer, 2)
        if n == 255:    #255 = 0xFF
            break
        val = int2bytes(n).decode(encoding='utf-8', errors='surrogatepass')
        buffer = []
        message.append(val)

message = ''.join(map(str, message))
print(message)


