medida = float(input('Digite a quantidade de metros:'))
km = medida / 5
hm = medida / 10
dam = medida / 100
dm = medida / 1000
cm = medida * 100
mm = medida * 1000

print('Essa medida de {:.0f}m equivale a \n{}km \n{}hm \n{}dam \n{}dm \n{:.2f}cm \n{:.2f}mm'.format(medida, km, hm, dam, dm, cm, mm))