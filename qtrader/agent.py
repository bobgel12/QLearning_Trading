#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement and run an agent to learn in reinforcement learning framework

@author: ucaiado

Created on 08/18/2016
"""
import random
from environment import Agent, Environment
from simulator import Simulator
import logging
import sys
import time
from collections import defaultdict
import pandas as pd

# Log finle enabled. global variable
DEBUG = False


# setup logging messages
if DEBUG:
    s_format = '%(asctime)s;%(message)s'
    s_now = time.strftime('%c')
    s_now = s_now.replace('/', '').replace(' ', '_').replace(':', '')
    s_file = 'log/sim_{}.log'.format(s_now)
    logging.basicConfig(filename=s_file, format=s_format)
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(s_format)
    ch.setFormatter(formatter)
    root.addHandler(ch)


'''
Begin help functions
'''


def save_q_table(e):
    '''
    Log the final Q-table of the algorithm
    :param e: Environment object. The grid-like world
    '''
    agent = e.primary_agent
    try:
        q_table = agent.q_table
        pd.DataFrame(q_table).T.to_csv('log/qtable.log', sep='\t')
    except:
        print 'No Q-table to be printed'

'''
End help functions
'''


class BasicAgent(Agent):
    '''
    A Basic agent representation that learns to drive in the smartcab world.
    '''
    def __init__(self, env):
        '''
        Initialize a BasicLearningAgent. Save all parameters as attributes
        :param env: Environment object. The Market
        '''
        # sets self.env = env, state = None, next_waypoint = None, and a
        # default color
        super(BasicAgent, self).__init__(env)


def run():
    """
    Run the agent for a finite number of trials.
    """
    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(BasicAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track

    # Now simulate it
    # create simulator (uses pygame when display=True, if available)
    sim = Simulator(e, update_delay=0.01, display=False)
    sim.run(n_trials=100)  # run for a specified number of trials

    # save the Q table of the primary agent
    save_q_table(e)


if __name__ == '__main__':
    # run the code
    run()