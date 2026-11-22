from game_logic_2_0 import Game_logic

game = Game_logic('q.pkl')



print(len(game.q_tab))

for i in range(10):
    win,los,nech = 0,0,0
    print(f'Training AI {i+1}/10')
    for _ in range(100000):
        game.training_ai()
    for _ in range(10):
        a = game.test_ai()
        if a == 0:
            nech +=1
        elif a == 1:
            los += 1
        else:
            win += 1
    print(f'побед: {win}, поражений: {los}, нечей: {nech}')

print(len(game.q_tab))
game.save_q()

print(f'побед: {win}, поражений: {los}, нечей: {nech}')
