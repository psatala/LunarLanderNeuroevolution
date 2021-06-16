from config import N_SIM_STEP_LIMIT
import gym
import datetime
import time
import torch

import network
import heuristic

def eval(flat_params=None, seed=None):
    if seed is None:
        seed = int(round(time.time()))

    net = network.Network(flat_param_array=flat_params)
    env = gym.make("LunarLander-v2")

    env.seed(seed)
    total_reward = 0
    steps = 0
    s = env.reset()
    while True:
        a = net(torch.from_numpy(s)).argmax().detach().numpy()
        s, r, done, info = env.step(a)
        total_reward += r

        steps += 1
        if done: break
        if steps == N_SIM_STEP_LIMIT: break

    return total_reward



if __name__ == '__main__':
    eval()