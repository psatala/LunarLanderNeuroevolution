import gym
import time

import torch
import network
import config

def main():
    net = network.Network()
    net.load_state_dict(torch.load(config.PATH))
    env = gym.make("LunarLander-v2")

    while True:
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
                print("step {} total_reward {:+0.2f}".format(steps, 
                    total_reward))
                break

            steps += 1


if __name__ == '__main__':
    main()