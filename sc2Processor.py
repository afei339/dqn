from rl.core import Processor
import numpy as np


class Sc2Processor(Processor):

    def __init__(self, screen=16):
        super(Processor, self).__init__()
        self._SCREEN = screen

    def process_state_batch(self, batch):
        # reshape cause batch is (bs, 1, 2, screen, screen)
        size_first_dim = len(batch)
        return np.reshape(batch, (size_first_dim, 2, self._SCREEN, self._SCREEN))

    # observation, reward, done, info = env.step(action)
    def process_observation(self, observation):

        # small_observation = observation[0].observation["feature_screen"][5]

        # print(smallObservation, observation[0].reward, observation[0].last(), "lol")

        # small_observation = small_observation.reshape(1, small_observation.shape[0], small_observation.shape[0], 1)

        # print(smallObservation.shape)

        # print(smallObservation, observation[0].reward, observation[0].last(), "lol")

        # fix dim from 1 1 2 16 16 to 1 2 16 16
        # observation = observation[0]

        return observation

        # assert observation.ndim == 3  # (height, width, channel)
        # img = Image.fromarray(observation)
        # img = img.resize(INPUT_SHAPE).convert('L')  # resize and convert to grayscale
        # processed_observation = np.array(img)
        # assert processed_observation.shape == INPUT_SHAPE
        # return processed_observation.astype('uint8')  # saves storage in experience memory


class Sc2ProcessorFull(Processor):

    def __init__(self, screen=16):
        super(Processor, self).__init__()
        self._SCREEN = screen

    def process_state_batch(self, batch):
        # reshape cause batch is (bs, 1, 2, screen, screen)
        size_first_dim = len(batch)
        return np.reshape(batch, (size_first_dim, 17, self._SCREEN, self._SCREEN))

    # observation, reward, done, info = env.step(action)
    def process_observation(self, observation):

        # small_observation = observation[0].observation["feature_screen"][5]

        # print(smallObservation, observation[0].reward, observation[0].last(), "lol")

        # small_observation = small_observation.reshape(1, small_observation.shape[0], small_observation.shape[0], 1)

        # print(smallObservation.shape)

        # print(smallObservation, observation[0].reward, observation[0].last(), "lol")

        # fix dim from 1 1 2 16 16 to 1 2 16 16
        # observation = observation[0]

        return observation

        # assert observation.ndim == 3  # (height, width, channel)
        # img = Image.fromarray(observation)
        # img = img.resize(INPUT_SHAPE).convert('L')  # resize and convert to grayscale
        # processed_observation = np.array(img)
        # assert processed_observation.shape == INPUT_SHAPE
        # return processed_observation.astype('uint8')  # saves storage in experience memory
