import subprocess

for n in range(100 * 100):
  print('[*]', n)
  s = subprocess.check_output(['txt/{:04x}.txt'.format(n)])
  print(s)
  if s.startswith(b'ADCTF_'):
    print(s)
    break
