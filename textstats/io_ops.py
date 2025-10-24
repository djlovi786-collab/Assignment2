from pathlib import Path
from typing import Iterable, List, Tuple

DEFAULT_INPUT_FILENAME = "input.txt"
DEFAULT_OUTPUT_FILENAME = "output.txt"


def get_input_text(default_filename: str = DEFAULT_INPUT_FILENAME) -> Tuple[str, str]:
    """Read text content from the user-specified file, falling back to a default."""

    prompt = f"Enter input filename [{default_filename}]: "
    while True:
        candidate = input(prompt).strip() or default_filename
        path = Path(candidate).expanduser()
        try:
            return str(path), path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"File not found: {path}. Try again.")
        except OSError as exc:
            print(f"Could not read file {path}: {exc}. Try again.")


def display_results(lines: Iterable[str]) -> None:
    """Print each result line to the console."""

    for line in lines:
        print(line)


def save_output_lines(
    lines: Iterable[str],
    default_filename: str = DEFAULT_OUTPUT_FILENAME,
) -> str:

    cached_lines: List[str] = list(lines)
    prompt = f"Enter output filename [{default_filename}]: "
    while True:
        candidate = input(prompt).strip() or default_filename
        path = Path(candidate).expanduser()
        try:
            path.write_text("\n".join(cached_lines), encoding="utf-8")
            print(f"Wrote {len(cached_lines)} lines to {path}")
            return str(path)
        except OSError as exc:
            print(f"Could not write to {path}: {exc}. Try again.")
