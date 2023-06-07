from pyDatalog import pyDatalog

## HECHOS
pyDatalog.assert_fact('progenitor', 'alejandro', 'fernando')
pyDatalog.assert_fact('progenitor', 'alejandro', 'raul')
pyDatalog.assert_fact('progenitor', 'sabina', 'raul')
pyDatalog.assert_fact('progenitor', 'sabina', 'fernando')
pyDatalog.assert_fact('progenitor', 'raul', 'andre')
pyDatalog.assert_fact('progenitor', 'raul', 'eduardo')
pyDatalog.assert_fact('progenitor', 'vanessa', 'andre')
pyDatalog.assert_fact('progenitor', 'vanessa', 'eduardo')
pyDatalog.assert_fact('progenitor', 'fernando', 'leonardo')
pyDatalog.assert_fact('progenitor', 'fernando', 'camila')
pyDatalog.assert_fact('progenitor', 'karina', 'leonardo')
pyDatalog.assert_fact('progenitor', 'karina', 'camila')
pyDatalog.assert_fact('progenitor', 'eduardo', 'gabriela')
pyDatalog.assert_fact('progenitor', 'andre', 'maria')

## REGLAS
pyDatalog.load("hermano(H1, H2) <= progenitor(P, H1) & progenitor(P, H2) & (H1 != H2)")
pyDatalog.load("abuelo(A, N) <= progenitor(A, P) & progenitor(P, N)")
pyDatalog.load("tio(T, S) <= progenitor(P, S) & hermano(T, P)")
pyDatalog.load("madre(M, H) <= progenitor(M, H) & (M != H) & (M[-1] == 'a')")
pyDatalog.load("primo(P, Q) <= progenitor(P1, P) & progenitor(P2, Q) & hermano(P1, P2)")
pyDatalog.load("hijo(H, M) <= progenitor(M, H)")
pyDatalog.load("nieto(N, A) <= progenitor(A, P) & progenitor(P, N)")
pyDatalog.load("bisabuelo(A, B) <= progenitor(A, P) & progenitor(P, Q) & progenitor(Q, B) & (A != B)")
pyDatalog.load("bisnieto(B, A) <= progenitor(A, P) & progenitor(P, Q) & progenitor(Q, B) & (A != B)")

print(f"Hermanos:{pyDatalog.ask('hermano(H1, H2)')}\n")
print(f"Abuelos: {pyDatalog.ask('abuelo(alejandro, X)')}\n")
print(f"Tios: {pyDatalog.ask('tio(T, andre)')}\n")
print(f"madres: {pyDatalog.ask('madre(M, H)')}\n")
print(f"Primos: {pyDatalog.ask('primo(eduardo, Q)')}\n")
print(f"hijos: {pyDatalog.ask('hijo(fernando, B)')}\n")
print(f"nietos: {pyDatalog.ask('nieto(andre, B)')}\n")
print(f"bisabuelo: {pyDatalog.ask('bisabuelo(A, gabriela)')}\n")
print(f"bisnieto: {pyDatalog.ask('bisnieto(B, alejandro)')}\n")



