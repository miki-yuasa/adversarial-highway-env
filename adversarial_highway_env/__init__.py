import gymnasium as gym

# Register the environment with Gymnasium

gym.register(
    id="AdversarialParking-v0",
    entry_point="adversarial_highway_env.envs.parking:AdversarialParkingEnv",
)
