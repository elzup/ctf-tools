from PIL import Image

for n in range(100 * 100):
  s = ''
  im = Image.open('images/{:04x}.png'.format(n))

  for y in range(29):
    for x in range(29):
      s += 'X' if im.getpixel((x * 3, y * 3)) == (0, 0, 0) else '_'
    s += '\n'

  open('txt/{:04x}.txt'.format(n), 'w').write(s)
