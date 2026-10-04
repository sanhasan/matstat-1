from pathlib import Path

from matplotlib.figure import Figure


IMAGES_DIR = Path(__file__).resolve().parent.parent / "images"


def save_figure(figure: Figure, filename: str) -> Path:
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    path = IMAGES_DIR / filename
    figure.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    return path
