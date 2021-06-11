import gym
import datetime

import torch
import network
import heuristic

def main():
    net = network.Network()
    env = gym.make("LunarLander-v2")
    flat_params = net.get_params()

    # check parsing parameters
    net2 = network.Network()
    net2.set_params(flat_param_array=flat_params)
    print("Equality of both networks: " + str(net == net2))

    while True:
        env.seed(int(datetime.datetime.now().timestamp()))
        total_reward = 0
        steps = 0
        s = env.reset()
        while True:
            a = net(torch.from_numpy(s)).argmax().detach().numpy()
            s, r, done, info = env.step(a)
            total_reward += r

            # rest of this loop has been copied from tutorial
            still_open = env.render()
            if still_open == False: break

            if steps % 20 == 0 or done:
                print("observations:", " ".join(["{:+0.2f}".format(x) for x in s]))
                print("step {} total_reward {:+0.2f}".format(steps, total_reward))
            steps += 1
            if done: break



if __name__ == '__main__':
    main()