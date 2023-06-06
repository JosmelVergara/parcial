from pyDatalog import pyDatalog
##HECHOS
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

##REGLAS
pyDatalog.load("hermano(H1,H2) <= progenitor(P,H1) & progenitor(P, H2) & (H1!=H2)")
pyDatalog.load("abuelo(A,N) <= progenitor(A,P) & progenitor(P,N)")
pyDatalog.load("tio(T,S) <= progenitor(P,S) & hermano(T,P)")

##print(pyDatalog.ask('progenitor(raul,X)'))
print(pyDatalog.ask('hermano(H1, H2)'))
print(pyDatalog.ask('abuelo(alejandro, X)'))
print(pyDatalog.ask('tio(T, andre)'))


