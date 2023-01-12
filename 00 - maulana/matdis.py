stop=False
while not(stop):
  print("iMPLEMENTASI")
  print("Analogikan pernyataan Kalimat 1 sebagai p atau ~p dan Kalimat 2 sebagai q atau ~q")
  p=str(input("Kalimat 1 : "))
  q=str(input("Kalimat 2 : "))
  print("\n")
  print("1. Konvers")
  print("2. Invers")
  print("3. Kontraposisi")
  print("4. Stop")
  tekan=input("masukkan pilihan anda=")
  if tekan =='1':
      p,q=q,p      
      print('Konversi dari p => q adalah = ',p," => ",q,"Hasilnya")
  elif tekan =='2':
      p = "~(p)"
      q = "~(q)"
      print('Konversi dari p => q adalah = ',p," => ",q,"Hasilnya")
  elif tekan =='3':
      p = "~(q)"
      q = "~(p)"
      print('Konversi dari p => q adalah = ',p," => ",q,"Hasilnya")
  elif tekan =="4":
    stop=True       
  inp=input('lagi (y/t) ?')
  if inp=='t':
        stop=True