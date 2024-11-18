from slicer import utils
from slicer.engine import AudioSlicerEngine

if __name__ == "__main__":
    args = utils.parse_args()
    AudioSlicerEngine(
        audio_sampling_rate=args.audio_sampling_rate,
        input_dir=args.input_dir,
        output_dir=args.output_dir,
    ).run()
