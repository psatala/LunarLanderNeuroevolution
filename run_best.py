import gym
import time

import torch
import network
import config

def main():
    games = 0
    env = gym.make("LunarLander-v2")
    net = network.Network()

    while True:
        net.load_state_dict(torch.load(config.PATH))
        env.seed(round(time.time()))
        
        total_reward = 0
        steps = 0
        s = env.reset()
        while True:
            a = net(torch.from_numpy(s)).argmax().detach().numpy()
            s, r, done, info = env.step(a)
            total_reward += r

            still_open = env.render()
            if still_open == False:
                return

            if done:
                print("game {} step {} total_reward {:+0.2f}".format(games, 
                    steps, total_reward))
                break

            steps += 1
        games += 1


if __name__ == '__main__':
    main()