l = float(input('Largura da parede: '))
a = float(input('Altura de parede: '))
area = l * a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))