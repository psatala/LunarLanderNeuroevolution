import gym
import numpy as np

import network
import torch

SEED = 123
MAX_ENV_SEED = 10**9
N_GAMES = 1000
PATH = "best_model_2021-06-15125804128475.pt"

def main():
    np.random.seed(SEED)
    env = gym.make("LunarLander-v2")
    net = network.Network()
    net.load_state_dict(torch.load(PATH))
    rewards = np.zeros(N_GAMES)

    for i in range(N_GAMES):
        env.seed(np.random.randint(MAX_ENV_SEED))
        
        total_reward = 0
        s = env.reset()
        while True:
            a = net(torch.from_numpy(s)).argmax().detach().numpy()
            s, r, done, info = env.step(a)
            total_reward += r

            if done:
                rewards[i] = total_reward
                break

    print("Mean: " + str(rewards.mean()))
    print("Stdev: " + str(rewards.std()))


if __name__ == '__main__':
    main()