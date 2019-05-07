#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Kami
# @Date:   2019-04-24 14:32:12
# @Last Modified by:   Kami
# @Last Modified time: 2019-05-07 09:29:58

from __future__ import print_function

def d_recognize(tape, transition_table, accept_states):
    '''
    Deterministic Finite-State Automaton 
    (If the tape completly accord with the automaton, then return accept; otherwise, return reject.
    The automaton knows exactly where to go)

    @param tape: input tape of string 
    @param transition_table: transisiton table of the automaton (-1 means empty)
    @param accept_states: accept states of the automaton
    @return boolean: accept(True) or reject(False)
    '''

    result = False  # initial result
    current_state = 0   # initial state of machine
    for index in range(len(tape)):
        try:
            current_state = transition_table[current_state][tape[index]]
        except KeyError:
            # string not in alphabet
            current_state = -1

        if current_state == -1:
            break
        
    # end of the input has been reached
    if current_state in accept_states:
        result = True
    return result


def test_d_recognize():
    '''
    TEST: d_recognize(tape, transition_table, accept_state)
    '''
    tape = "baaa!"
    alphabet = ['b','a','!']
    transition_matrix = [[1, -1, -1],
                        [-1, 2, -1],
                        [-1, 3, -1],
                        [-1, 3, 4],
                        [-1, -1, -1]]
    accept_states = [4]
    transition_table = []
    for i in range(len(transition_matrix)):
        assert len(transition_matrix[i]) == len(alphabet)
        d = {}
        for j in range(len(alphabet)):    
            d[alphabet[j]] = transition_matrix[i][j]
        transition_table.append(d)

    print("Result of d_recognize: ", end='\t')
    print(d_recognize(tape, transition_table, accept_state))



if __name__ == "__main__":

    test_d_recognize()
