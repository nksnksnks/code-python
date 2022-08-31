t = int(input())
while t > 0:
    d,m = map(int, input().split())
    if (m == 3 and d >= 21 and d <=31) or (m == 4 and d <=19):
        print('Bach Duong')
    if (m == 4 and d >= 20 and d <=30) or (m == 5 and d <=20):
        print('Kim Nguu')
    if (m == 5 and d >= 21 and d <=31) or (m == 6 and d <=20):
        print('Song Tu')
    if (m == 6 and d >= 21 and d <=30) or (m == 7 and d <=22):
        print('Cu Giai')
    if (m == 7 and d >= 23 and d <=31) or (m == 8 and d <=22):
        print('Su Tu')
    if (m == 8 and d >= 23 and d <=31) or (m == 9 and d <=22):
        print('Xu Nu')
    if (m == 9 and d >= 23 and d <=30) or (m == 10 and d <=22):
        print('Thien Binh')
    if (m == 10 and d >= 23 and d <=31) or (m == 11 and d <=22):
        print('Thien Yet')
    if (m == 11 and d >= 23 and d <=30) or (m == 12 and d <=21):
        print('Nhan Ma')
    if (m == 12 and d >= 22 and d <=31) or (m == 1 and d <=19):
        print('Ma Ket')
    if (m == 1 and d >= 20 and d <=31) or (m == 2 and d <=18):
        print('Bao Binh')
    if (m == 2 and d >= 19 and d <=29) or (m == 3 and d <=20):
        print('Song Ngu')
    t-=1