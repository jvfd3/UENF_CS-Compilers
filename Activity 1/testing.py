'''as'''

transition_table = {
    'q0': {
        '0': 'q1',
        '1': 'q1',
    },
    'q1': {
        '0': 'q1',
        '1': 'q0',
    },
}

# for elem in transition_table:
#     print(elem)
# for elem in list(transition_table.keys()):
#     print(elem)
# for elem in transition_table.keys():
#     print(elem)
# for elem in transition_table.items():
#     print(elem)
#     print(elem[0])
#     print(elem[1])
#     print(elem[1].keys())
#     print(elem[1].values())

# for elem in transition_table:
#     test = list(transition_table[elem].values())
#     print(test)
#     print(str(test))
# for elem in transition_table.items():
#     print(elem)
# for elem in transition_table:
#     print(elem)
b = '0'
c = 'q0'
a = transition_table[c][b]
print(a)
