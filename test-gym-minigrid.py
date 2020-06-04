import gym
# Test specifically importing a specific environment
from gym_minigrid.envs import FourRoomsEnv

# Test importing wrappers
from gym_minigrid.wrappers import *

#python3 -m scripts.train --algo ppo --env MiniGrid-DoorKey-5x5-v0 --model DoorKey --save-interval 10 --frames 80000
#python3 -m scripts.visualize --env MiniGrid-DoorKey-5x5-v0 --model DoorKey
#python3 -m scripts.evaluate --env MiniGrid-DoorKey-5x5-v0 --model DoorKey


env = TargetGeneration(gym.make("MiniGrid-FourRooms-v0"))
env.reset()
env.render('rgb_array')

print(env.height)
print(env.agent_pos)
