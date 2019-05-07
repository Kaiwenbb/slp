#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Kami
# @Date:   2019-05-07 09:29:50
# @Last Modified by:   Kami
# @Last Modified time: 2019-05-07 15:15:12

from __future__ import print_function



def nd_recognize(tape, transition_table, accept_states):
    '''
    Non-Deterministic Automaton
    (If the tape completly accord with the automaton, then return accept; otherwise, return reject.
    The automaton has to choose where to go, and store the previous choices for not reaching the accpet states)

    @param tape: input tape of string 
    @param transition_table: transisiton table of the automaton (-1 means empty)
    @param accept_states: accept states of the automaton
    @return boolean: accept(True) or reject(False)
    '''

    def generate_new_state(current_state, index):
        epilson_list = transition_table[current_state]['ephilson']
        try:
            next_list = transition_table[current_state][tape[index]]
        except KeyError:
            next_list = []

        result = []
        for e in epilson_list:
            if e > 0 :
                result.append((e, index))
        for n in next_list:
            if n > 0 :
                result.append((n, index+1))

        return result


    result = False
    current_state = 0
    index = 0
    agenda = []

    while index < len(tape):
        agenda += generate_new_state(current_state, index)
        if len(agenda)==0:
            break
        
        # stack, LIFO
        current_state, index = agenda.pop()

    # ACCEPT-STATE?: end of the input has been reached
    if current_state in accept_states:
        result = True
    return result

def test_nd_recognize():
    '''
    TEST: nd_recognize(tape, transition_table, accept_state)
    '''
    tape = "baaaaa!"
    alphabet = ['b','a','!','ephilson']
    transition_matrix = [
                        [[1], [-1], [-1],[-1]],
                        [[-1], [2], [-1],[-1]],
                        [[-1], [2,3], [-1],[-1]],
                        [[-1], [-1], [4],[-1]],
                        [[-1], [-1], [-1],[-1]]]
    accept_states = [4]
    transition_table = []
    for i in range(len(transition_matrix)):
        assert len(transition_matrix[i]) == len(alphabet)
        d = {}
        for j in range(len(alphabet)):    
            d[alphabet[j]] = transition_matrix[i][j]
        transition_table.append(d)

    print("Result of d_recognize: ", end='\t')
    print(nd_recognize(tape, transition_table, accept_states))


if __name__ == "__main__":

    test_nd_recognize()
