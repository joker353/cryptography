import random
import cv2

img = cv2.imread('gessler.jpg', -1)

seed = 123

random.seed(seed)

message = "Gesslerowa43892ddwe342SL@a[35"
message += chr(0xFF)

msg_binary = ''
for m in message:
    m_bin = ''.join(format(ord(m), 'b'))
    x = 8 - len(m_bin)
    zero = ''
    for i in range(x):
        zero += '0'
    msg_binary += zero + m_bin

print(msg_binary)

pix = list(range(0, img.shape[0]*img.shape[1]))

for m_bit in msg_binary:
    pos = pix[random.randint(0, len(pix) - 1)]
    pix.remove(pos)
    cr, cc = pos//img.shape[0], pos - (pos//img.shape[0])*img.shape[0]
    img[cr, cc][0] = (img[cr, cc][0] & 0xFE) + int(m_bit)

cv2.imwrite('gessler_code.png', img)

