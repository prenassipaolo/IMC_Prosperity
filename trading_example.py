from state_example import state as state
from trader_example import Trader as Trader


T = Trader()

print(f'iteration: {T.iteration}')
print(f'logs: {T.logs}')

T.run(state)

print(f'iteration: {T.iteration}')
print(f'logs: {T.logs}')
