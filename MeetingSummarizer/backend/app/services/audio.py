import subprocess
from pathlib import Path

from imageio_ffmpeg import get_ffmpeg_exe


def prepare_for_transcription(source: Path) -> tuple[Path, bool]:
    if source.suffix.lower() != ".aac":
        return source, False

    destination = source.with_name(f"{source.stem}-transcription.flac")
    command = [
        get_ffmpeg_exe(),
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(source),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        "-c:a",
        "flac",
        str(destination),
    ]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as error:
        destination.unlink(missing_ok=True)
        message = error.stderr.strip() or "AAC conversion failed"
        raise RuntimeError(message) from error
    return destination, True
