import slide_left_to_right as slr
import slide_right_to_left as srl
import horizontal_split as hs
import vertical_split as vs

print()
print('Escolha o tipo da transição:')
print('1 - Slide esquerda pra direita')
print('2 - Slide direita pra esquerda')
print('3 - Split Horizontal')
print('4 - Split Vertical')
type = input()
type = int(type)

if type == 1:
    slr.slide_left_to_right()

elif type == 2:
    srl.slide_right_to_left()

elif type == 3:
    hs.horizontal_split()

elif type == 4:
    vs.vertical_split()

else:
    print('Tipo de transição inválida!')