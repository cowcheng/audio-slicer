import glob
import os
from pathlib import Path

import librosa
import soundfile

from slicer.vad import VoiceActivityDetector


class AudioSlicer:
    def __init__(
        self,
        audio_sampling_rate: int,
        output_dir: str,
    ) -> None:
        """
        Initializes the Slicer object.

        Parameters:
            audio_sampling_rate (int): The sampling rate for audio processing.
            output_dir (str): The directory where output files will be saved.

        Attributes:
            audio_sampling_rate (int): The sampling rate for audio processing.
            output_dir (str): The directory where output files are saved.
            vad (VoiceActivityDetector): The voice activity detector instance.
        """
        
        self.audio_sampling_rate = audio_sampling_rate
        self.output_dir = output_dir
        os.makedirs(name=self.output_dir)
        self.vad = VoiceActivityDetector(
            sr=self.audio_sampling_rate,
            threshold=-40,
            min_length=5000,
            min_interval=300,
            hop_size=10,
            max_sil_kept=500,
        )

    def slice(
        self,
        file_path: str,
    ) -> None:
        """
        Slices the audio file at the given file path and saves the resulting audio segments.

        Args:
            file_path (str): The path to the source audio file to be sliced.

        Returns:
            None
        """

        file_name = file_path.split("/")[-1].split(".")[0]
        source_audio, _ = librosa.load(
            path=file_path,
            sr=None,
            mono=False,
        )
        result_audio_list = self.vad.slice(waveform=source_audio)
        for i, audio in enumerate(result_audio_list):
            if len(audio.shape) > 1:
                audio = audio.T
            soundfile.write(
                file=f"{self.output_dir}/{file_name}_{i}.wav",
                data=audio,
                samplerate=self.audio_sampling_rate,
            )
