#!/usr/bin/env python

# Other imports.
import srl_example_setup
from simple_rl.agents import LinearApproxQLearnerAgent, RandomAgent
from simple_rl.tasks import GymMDP
from simple_rl.run_experiments import run_agents_on_mdp

# Gym MDP
gym_mdp = GymMDP(env_name='MountainCar-v0', render=True)

# Setup agents and run.
lin_agent = LinearApproxQLearnerAgent(gym_mdp.actions)
rand_agent = RandomAgent(gym_mdp.actions)

run_agents_on_mdp([lin_agent, rand_agent], gym_mdp, instances=25, episodes=100, steps=200)