# Audio Slicer

This repository provides a command-line tool for slicing audio files based on voice activity detection (VAD). Built with NumPy for efficient audio processing, this tool supports multithreading to accelerate processing speed, making it ideal for handling large audio datasets.

## Features

- **Voice Activity Detection (VAD)**: Automatically detects and segments regions with active voice in audio files.
- **Multi-Threaded Processing**: Leverages multithreading to process multiple audio files simultaneously, significantly boosting performance.
- **Efficient Implementation**: Built on NumPy for fast and reliable data handling.

## Setup

### Prerequisites

- Python 3.11 or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/audio-slicer-vad.git
cd audio-slicer-vad
```

2. Create a virtual environment:

```bash
python3.11 -m venv .venv
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Upgrade pip, wheel, and setuptools:

```bash
pip install -U pip wheel setuptools
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the tool, run the following command:

```bash
python main.py --audio_sampling_rate <audio_sampling_rate> --input_dir <input_directory> --output_dir <output_directory>
```

### Command-Line Arguments

- --`audio_sampling_rate`: The sampling rate of the audio files
- --`input_dir`: Path to the directory containing input audio files.
- --`output_dir`: Directory where the sliced audio files will be saved.

## Workflow

1. **Voice Detection**: Analyze each audio file using VAD to identify segments with active voice.
2. **Audio Slicing**: Slice the audio based on detected voice regions and save the results.
3. **Parallel Processing**: Utilize multithreading to handle multiple files concurrently, ensuring efficient utilization of system resources.

## Notes

This tool is designed for command-line use and does not include a graphical interface.
Performance may vary depending on the number of threads and system resources available.

## License

Ensure compliance with all relevant copyright and licensing laws when using this tool. Refer to the LICENSE file for more details.
