from PIL import Image


def vegetacao(original):
    W, H = original.size
    img = Image.new("RGB", (W, H))
    
    for i in range(W):
        for j in range(H):
            px = original.getpixel((i, j))
    
            if(2*px[1] - px[0] - px[2] <= px[1]/5):
                px = [0, 0, 0]
    
            img.putpixel((i, j), (px[0], px[1], px[2]))

    return img

#definindo imagem
img01  = Image.open("planta01.jpg")
w01, h01 = img01.size

img02 = Image.open("planta02.jpg")
w02, h02 = img02.size

new01  = Image.new("RGB", (w01, h01))
new02  = Image.new("RGB", (w02, h02)) 

new01 = vegetacao(img01)
new02 = vegetacao(img02)

new02.show()
img02.show()