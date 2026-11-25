"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue to $MAKEFUN_OUTPUT_DIR/entry.txt (default: ./output)
and prints it to stdout. Fully deterministic: one fixed text, no input,
no randomness, no network, no clock.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "You stand there, sword up, chin up, the whole pose. "
    "Malachar has seen it a thousand times. Sit. "
    "The floor is cold. The hearth is out. "
    "My crows left years ago. "
    "I kept this siege for forty years, and all I kept was the damp. "
    "Where was I? The speech. "
    "I must stand and call the storm and say the old words, "
    "but my throat is raw and my knees have filed their own complaint. "
    "So take the crown. Take the keys. "
    "Just leave the chair by the fire, and come back Thursday. "
    "We shall do the grand battle then."
)


def resolve_output_path(argv=None) -> Path:
    if argv and len(argv) > 1:
        return Path(argv[1])
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def print_entry() -> None:
    print(ENTRY)


def write_entry(entry_path: Path) -> None:
    entry_path.write_text(ENTRY + "\n", encoding="utf-8")
    print_entry()


def run(argv=None) -> None:
    entry_path = resolve_output_path(argv)
    write_entry(entry_path)


def main(argv=None) -> None:
    run(argv)


if __name__ == "__main__":
    main(sys.argv)
