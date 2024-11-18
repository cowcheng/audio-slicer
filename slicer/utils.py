import logging
from argparse import ArgumentParser, Namespace

import numpy as np

from slicer.configs import LOG_DATEFMT, LOG_FORMAT, LOG_LEVEL

logging.basicConfig(
    format=LOG_FORMAT,
    datefmt=LOG_DATEFMT,
    level=LOG_LEVEL,
)

logger = logging.getLogger(name="AudioSlicer")


def parse_args() -> Namespace:
    """
    Parses command-line arguments for the audio slicer application.

    Returns:
        Namespace: The parsed arguments containing audio_sampling_rate, input_dir, and output_dir.
    """

    parser = ArgumentParser()
    parser.add_argument(
        "--audio_sampling_rate",
        default=44100,
        type=int,
        help="The sampling rate of the audio files",
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        required=True,
        help="The directory containing the input audio files",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="The directory where the sliced audio files will be saved",
    )

    args = parser.parse_args()
    return args


"""
Source from the librosa library.
"""


def get_rms(
    y,
    *,
    frame_length=2048,
    hop_length=512,
    pad_mode="constant",
) -> np.ndarray:
    """
    Compute the Root Mean Square (RMS) of the input signal.

    Parameters:
        y (np.ndarray): Input audio signal.
        frame_length (int, optional): Length of each frame. Defaults to 2048.
        hop_length (int, optional): Number of samples between successive frames. Defaults to 512.
        pad_mode (str, optional): Mode to use for padding the signal. Defaults to "constant".

    Returns:
        np.ndarray: Array of RMS values for each frame.
    """

    padding = (int(frame_length // 2), int(frame_length // 2))
    y = np.pad(y, padding, mode=pad_mode)

    axis = -1
    out_strides = y.strides + tuple([y.strides[axis]])
    x_shape_trimmed = list(y.shape)
    x_shape_trimmed[axis] -= frame_length - 1
    out_shape = tuple(x_shape_trimmed) + tuple([frame_length])
    xw = np.lib.stride_tricks.as_strided(y, shape=out_shape, strides=out_strides)
    if axis < 0:
        target_axis = axis - 1
    else:
        target_axis = axis + 1
    xw = np.moveaxis(xw, -1, target_axis)
    slices = [slice(None)] * xw.ndim
    slices[axis] = slice(0, None, hop_length)
    x = xw[tuple(slices)]

    power = np.mean(np.abs(x) ** 2, axis=-2, keepdims=True)

    return np.sqrt(power)
