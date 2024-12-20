import os

import gymnasium as gym
import imageio

import adversarial_highway_env


def test_adversarial_parking_init():
    animation_save_path: str = "tests/out/test_adversarial_parking_init.gif"
    env = gym.make("AdversarialParking-v0")

    obs, _ = env.reset()
    frames = [env.render()]

    step_count: int = 0
    while True:
        step_count += 1
        obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
        frames.append(env.render())

        if terminated or truncated:
            break
        else:
            pass

    os.makedirs(os.path.dirname(animation_save_path), exist_ok=True)
    imageio.mimsave(animation_save_path, frames, fps=30)

    assert os.path.exists(animation_save_path)
