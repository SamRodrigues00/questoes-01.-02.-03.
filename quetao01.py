pes: float; polegadas: float; jardas: float; mi: float

pes = float ( input ("Informe a medida em pes: "))
polegadas = pes * 12
jardas = pes / 3
mi = jardas / 1760
print( f"sua medida em POLEGADAS: { round(polegadas,2 ) }, em JARDAS: { round(jardas,2 ) }, em MILHAS: {round(mi,2) }")