import glob
import os
import warnings
from concurrent.futures import ThreadPoolExecutor

from tqdm import tqdm

from slicer.slicer import AudioSlicer
from slicer.utils import logger

warnings.filterwarnings(action="ignore")


class AudioSlicerEngine:
    def __init__(
        self,
        audio_sampling_rate: int,
        input_dir: str,
        output_dir: str,
    ) -> None:
        """
        Initialize the Audio Slicer Engine.

        Args:
            audio_sampling_rate (int): The sampling rate for audio processing.
            input_dir (str): The directory path where input audio files are located.
            output_dir (str): The directory path where sliced audio files will be saved.

        Attributes:
            output_dir (str): The output directory path.
            num_workers (int): The number of worker threads based on CPU count.
            batch_id (str): A unique identifier for the current batch.
            slicer (AudioSlicer): An instance of the AudioSlicer class.
            files_list (List[str]): A list of input audio file paths.
        """

        self.output_dir = output_dir

        logger.info(msg="Initializing Audio Slicer Engine")
        logger.info(msg=f"Audio sampling rate: {audio_sampling_rate}")
        logger.info(msg=f"Input directory: {input_dir}")
        logger.info(msg=f"Output directory: {self.output_dir}")

        self.num_workers = int(os.cpu_count() // 1.5)
        logger.info(msg=f"Number of workers: {os.cpu_count()}")

        self.slicer = AudioSlicer(
            audio_sampling_rate=audio_sampling_rate,
            output_dir=output_dir,
        )

        self.files_list = glob.glob(pathname=f"{input_dir}/*.*")

    def run(
        self,
    ) -> None:
        """
        Executes the audio slicing process concurrently across multiple workers.

        This method initializes a ThreadPoolExecutor with a specified number of workers
        and maps the `slicer.slice` function to each file in `files_list`. The progress
        of the slicing operation is displayed using a tqdm progress bar.

        Returns:
            None
        """

        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            list(
                tqdm(
                    executor.map(self.slicer.slice, self.files_list),
                    total=len(self.files_list),
                    desc="Slicing audio files",
                )
            )
