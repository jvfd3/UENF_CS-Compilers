'''Creating and running a DFA'''


def creating_automata():
    '''returning a tuple'''
    states = ['q0', 'q1']
    Q = states

    alphabet = ['0', '1']
    Σ = alphabet

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
    δ = transition_table

    initial_state = 'q0'
    q0 = initial_state

    final_states = ['q0']
    F = final_states

    # automata = (Q, Σ, δ, q0, F)
    automata = {'Q': Q, 'Σ': Σ, 'δ': δ, 'q0': q0, 'F': F}
    return automata


def automata_validation(automata):
    '''validating'''

    def check_transition_table(automata):
        '''checking transition table'''

        def check_transitions_size(automata):
            '''aaa'''
            transition_table = automata['δ']
            states = automata['Q']
            errors = ''
            if len(transition_table) != len(states):
                errors += 'Not all states have transitions.\n'
            return errors

        def check_origin_states(automata):
            '''aaa'''
            def get_origin_states(automata):
                '''bbb'''
                transition_table = automata['δ']
                origin_transition_states = []
                for key in transition_table:
                    origin_transition_states.append(key)
                return origin_transition_states

            origin_transition_states = get_origin_states(automata)
            states = automata['Q']
            errors = ''
            if len(origin_transition_states) != len(states):
                errors += 'Not same number of states and origin state transitions. '
                errors += 'Your transition origin states are:\t"' + origin_transition_states
                errors += '"\nand all your automata states are:\t"' + states
                errors += '"\n'
            for elem in origin_transition_states:
                if elem not in states:
                    errors += f'The origin transition state "{elem}" is not'
                    errors += f'in your states list "{states}"\n'
            for elem in states:
                if elem not in origin_transition_states:
                    errors += f'The state "{elem}" is not'
                    errors += 'in your origin states transition list "'
                    errors += f'{origin_transition_states}"\n'
            return errors

        def check_origin_tokens(automata):
            '''aaa'''
            def check_lists_equality(used_alphabet, alphabet):
                '''
                https://thispointer.com/python-check-if-two-lists-are-equal-or-not-covers-both-ordered-unordered-lists/
                '''
                errors = ''
                inequality_message = str(used_alphabet) + str(alphabet) + '\n'
                same_message = ' used in the alphabet and in the transition table are different: '
                if len(used_alphabet) != len(alphabet):
                    errors += 'The size of the lists' + same_message + inequality_message
                if sorted(used_alphabet) != sorted(alphabet):
                    errors += 'elements' + same_message + inequality_message
                return errors

            errors = ''
            alphabet = automata['Σ']
            # alphabet = ['0', '1']
            transition_table = automata['δ']
            # transition_table = {
            #     'q0': {
            #         '0': 'q1',
            #         '1': 'q1',
            #     },
            #     'q1': {
            #         '0': 'q1',
            #         '1': 'q0',
            #     },
            # }
            for elem in transition_table:
                used_alphabet = list(transition_table[elem].keys())
                errors += check_lists_equality(used_alphabet, alphabet)
            return errors

        def check_arrive_states(automata):
            '''aaa'''
            def check_lists_compatibility(arrive_states, states):
                '''aaa'''
                errors = ''
                for elem in arrive_states:
                    if elem not in states:
                        errors += f'arrive state "{elem}" does not exists in the possible states\n'
                return errors
            errors = ''
            transition_table = automata['δ']
            states = automata['Q']
            for elem in transition_table:
                arrive_states = list(transition_table[elem].values())
                errors += check_lists_compatibility(arrive_states, states)
            return errors

        errors = ''
        errors += check_transitions_size(automata)
        errors += check_origin_states(automata)
        errors += check_origin_tokens(automata)
        errors += check_arrive_states(automata)

        return errors

    def check_initial_states(automata):
        '''checking initial states'''
        errors = ''
        q0 = automata['q0']
        states = automata['Q']
        if q0 not in states:
            errors += 'the initial state' + q0 + 'is not in your state list ' + states + '.\n'
        return errors

    def check_final_states(automata):
        '''checking final states'''
        errors = ''
        final_states = automata['F']
        states = automata['Q']
        for elem in final_states:
            if elem not in states:
                errors += 'the final state' + elem + 'is not in your state list ' + states + '.\n'
        return errors

    errors = ''
    errors += check_transition_table(automata)
    errors += check_initial_states(automata)
    errors += check_final_states(automata)

    return errors


def run_automata(automata):
    '''aaa'''
    def print_starting_message():
        '''aaa'''
        line = 2*'\n' + 12*'=' + 2*'\n'
        message = 'automata is valid. Now, running automata: \t'
        message = line + message + str(automata) + line
        print(message)

    def run_automata_on_word(word):
        '''aaa'''
        def print_transition_message(current_state, transitions, token):
            '''aaa'''
            new_state = transitions[current_state][token]
            message = f'{current_state} -({token})-> {new_state}'
            print(message)

        print(f'\n\ntesting word: {word}')
        current_state = automata['q0']
        transitions = automata['δ']
        final_states = automata['F']
        alphabet = automata['Σ']
        final_message = f'The string "{word}" is '
        for token in word:
            if token not in alphabet:
                print(f'invalid Token "{token}"')
                return
            print_transition_message(current_state, transitions, token)
            current_state = transitions[current_state][token]
        if current_state not in final_states:
            final_message += 'in'
        final_message += 'valid'
        print(final_message)
    print_starting_message()

    def batch_testing():
        '''aaa'''
        word_to_validate = [
            '0',
            '00',
            '10',
            '00100',
            '00122002',
            '00101010',
            '001',
            '001001',
        ]
        for elem in word_to_validate:
            run_automata_on_word(elem)

    batch_testing()


def main():
    '''aaa'''
    automata = creating_automata()
    encounted_errors = automata_validation(automata)
    if encounted_errors == '':
        run_automata(automata)
    else:
        line = '\n' + 12*'=' + '\n'
        message = line + 'Something went wrong. Printing the error log:' + line
        message += line + '\n' + encounted_errors + line
        print(message)


main()
