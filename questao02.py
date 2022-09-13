kg = float ( input ( "informe a quantidade de ração do saco em kg: ") )
pesosaco = kg * 1000
gato1 = float( input ( f"informe em gramas quanto o gato 1 consome por dia: ") )
gato2 = float( input ( f"informe em gramas quanto o gato 2 consome por dia: ") )
tot5dias = pesosaco - (gato1 * 5 + gato2 * 5)
print( f"O resultado apos 5 dias é: { tot5dias } gramas. ")