k_vuc = input('k_vuc: ')

if k_vuc == 'KV1':
  d_k_vuc = 0.75
elif k_vuc == 'KV2-NT':
  d_k_vuc = 0.5
elif k_vuc == 'KV2':
  d_k_vuc = 0.25

d_toan = input('d_toan: ')
d_van = input('d_van: ')
d_anh = input('d_anh: ')
sum = d_k_vuc + int(d_toan) + int(d_van) + int(d_anh)
print(str(sum))
