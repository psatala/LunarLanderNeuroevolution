import gym
import numpy as np

from heuristic import heuristic

SEED = 123
MAX_ENV_SEED = 10**9
N_GAMES = 1000

def main():
    np.random.seed(SEED)
    env = gym.make("LunarLander-v2")
    rewards = np.zeros(N_GAMES)

    for i in range(N_GAMES):
        env.seed(np.random.randint(MAX_ENV_SEED))
        
        total_reward = 0
        s = env.reset()
        while True:
            a = heuristic(s)
            s, r, done, info = env.step(a)
            total_reward += r


            if done:
                rewards[i] = total_reward
                break

    print("Mean: " + str(rewards.mean()))
    print("Stdev: " + str(rewards.std()))


if __name__ == '__main__':
    main()