def towerOfHanoi(lempengan,asal,tujuan,bantuan):
    if lempengan == 1:
        print('Pindahkan Lempengan #%d Dari Tower %s Ke Tower %s'%(lempengan,asal,tujuan))
    else:
        towerOfHanoi(lempengan-1,asal,bantuan,tujuan)
        print('Pindahkan Lempengan #%d Dari Tower %s Ke Tower %s'%(lempengan,asal,tujuan))
        towerOfHanoi(lempengan-1,bantuan,tujuan,asal)
        
towerOfHanoi(4,'A','C','B')
'''
PINDAHKAN 4 LEMPENGAN DARI A KE C
1. (Asumsi) Pindahkan 3 Lempengan Dari A ke B
    1.a. (Asumsi) Pindahkan 2 Lempengan Dari A Ke C
        1.a.a. (Asumsi) Pindahkan 1 Lempengan Dari A ke B
            Pindahkan Lempengan Ke 1 dari A Ke B
        1.a.b. Pindahkan Lempengan Ke 2 Dari A Ke C
        1.a.c. (asumsi) Pindahkan Lempengan Dari B Ke C
            Pindahkan Lempengan Ke 2 Dari B Ke C
    1.b. Pindahkan Lempengan Ke 3 Dari A Ke B
    1.c. (Asumsi) Pindahkan 2 Lempengan Dari C Ke B
2. Pindahkan Lempengan ke 4 Dari A Ke C
3. (Asumsi) Pindahkan 3 Lempengan Dari B Ke C
4. 
'''
PINDAHKAN 4 LEMPENGAN DARI A KE C
1. (Asumsi) Pindahkan 3 Lempengan Dari A ke B
    1.a. (Asumsi) Pindahkan 2 Lempengan Dari A Ke C
        1.a.a. (Asumsi) Pindahkan 1 Lempengan Dari A ke B
            Pindahkan Lempengan Ke 1 dari A Ke B
        1.a.b. Pindahkan Lempengan Ke 2 Dari A Ke C
        1.a.c. (asumsi) Pindahkan Lempengan Dari B Ke C
            Pindahkan Lempengan Ke 2 Dari B Ke C
    1.b. Pindahkan Lempengan Ke 3 Dari A Ke B
    1.c. (Asumsi) Pindahkan 2 Lempengan Dari C Ke B
        1.c.a. (Asumsi) Pindahkan 1 lempengan dari C ke A
            Pindahkan lempengan ke 1 dari C ke A
        1.c.b. Pindahkan lempengan 2 dari C ke B
        1.c.c (Asumsi) Pindahkan 1 lempengan dari A ke B
            Pindahkan lempengan ke 1 dari A ke B
2. Pindahkan Lempengan ke 4 Dari A Ke C
3. (Asumsi) Pindahkan 3 Lempengan Dari B Ke C
4.
