
import random
pair = []
boys = ['ali', 'reza', 'akbar', 'naser', 'mahdiar', 'saber', 'hasan', 'amir']
girls = ['zahra', 'hasti', 'hamide', 'nazanin', 'nilo', 'mina', 'tayeb', 'setare', 'sima']

print('pairs =',end="")
for i in range(min(len(boys),len(girls))):
    boy = random.choice(boys)
    girl = random.choice(girls)
    pair.append([boy,girl])
    boys.remove(boy)
    girls.remove(girl)
    print("pairs="f'({boy},{girl})')

    
if len(girls):
    print(girls,'are single')
elif len(boys):
    print(boys,'are single')