import winsound
# duration = 5000  # millisecond
# freq = 37  # Hz
# winsound.Beep(freq, duration)
A = 1600
B = 800
C = 400
D = 200
E = 100
F = 50
# //低音
L1 = 262
L2 = 294
L3 = 330
L4 = 349
L5 = 392
L6 = 440
L7 = 493
# //高音
N1 = 532
N2 = 588
N3 = 660
N4 = 698
N5 = 784
N6 = 880
N7 = 988
# //半弦音
H1 = 1046
H2 = 1175
H3 = 1319
H4 = 1397
H5 = 1568
H6 = 1760
H7 = 1976

# winsound.PlaySound('ALARM8', winsound.SND_ASYNC)
# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
# winsound.PlaySound("*", winsound.SND_ALIAS)


def beep(f, d):
    winsound.Beep(f, d)
    
beep(N2, C)
beep(L5, C)
beep(N1, C)
# beep(0, C)
beep(N2, C)
beep(L5, C)
beep(N1, C)
# beep(0, C)