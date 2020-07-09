import numpy as np


class Frame:
    def __init__(self, frame: np.array, frame_number: int):
        self._frame = frame
        self._frame_number = frame_number

    def get_frame(self) -> np.array:
        return self._frame

    def get_frame_number(self) -> int:
        return self._frame_number

    def set_frame(self, value: np.array):
        self._frame = value

    def __hash__(self):
        return self.get_frame_number()
