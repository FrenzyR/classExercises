# Imos a implementar o xogo do tres en raia. Para iso imos a ir por partes.
# Lembra que o tablero é de 3 x 3. Fara representalo quizais sexa o mellor representalo cunha lista de listas.
# - Inicializa a estrutura a baleiro.
# - Imprime o taboleiro.
# - Podes facer que X represente unha ficha do xogador 1 e O a do xogador 2
# - Fai unha función que nos indique se temos un gañador ou non.
# - Utiliza test para comprobar os casos posibles, non teñen que ser todos, pero algúns si.
# - Implementa agora o proceso de xogo:
#     - Primeiro un xogador, comproba se hai gañador, logo outro.
#     - Paras cando un gaña ou xa non hai máis movementos.

player_one_turn : str = "Where will you place your X, player 1"
player_two_turn : str = "Where will you place your O, player 2"
def three_of_a_kind():
    playing_field = [[], [], [],
                     [], [], [],
                     [], [], []]
    print(playing_field)
    print(player_one_turn)
    print(player_two_turn)


three_of_a_kind()