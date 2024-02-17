# Markov Reward Process State Value Function Calculator

This Python script calculates the state value functions for a Markov Reward Process using iterative methods.

## Usage

To use this script, simply run it in a Python environment. Ensure that you have Python installed on your system.

```bash
python markov_reward_process.py

The script defines the state space, transition probabilities, and rewards for a Markov Reward Process. It then iteratively calculates the state value functions using the Bellman equation until convergence.

State Space
C1: State 1
C2: State 2
C3: State 3
FH: Final Handover State
PASS: Pass State
NF: No Further Handover State
TERMINATE: Terminal State
Transition Probabilities (State Transition Matrix)
The probabilities of transitioning from one state to another.

Rewards
The rewards associated with each state.

Discount Factor
The discount factor (gamma) used in the Bellman equation.

Output
The script prints the state value function of each state after each iteration until convergence. Once convergence is achieved, it prints the final state value functions.
