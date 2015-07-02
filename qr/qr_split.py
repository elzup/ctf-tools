from PIL import Image

p = 'images/{:04x}.png'
im = Image.open('qrgarden.png')

for x in range(100):
  for y in range(100):
    o = Image.new('RGB', (87, 87))
    o.paste(im.crop((x * 87, y * 87, (x + 1) * 87, (y + 1) * 87)), (0, 0))
    o.save(p.format(x + 100 * y))
