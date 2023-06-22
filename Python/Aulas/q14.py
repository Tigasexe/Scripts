lucas = 5000
igor = 3000
crescimento_lucas = 0.4 / 100 # / por
crescimento_igor = 0.9 / 100 # / por
anos = 0

while lucas >= igor:
    lucas += lucas * crescimento_lucas
    igor += igor * crescimento_igor
    anos += 1

print(anos)
