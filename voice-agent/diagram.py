"""Draw the voice-agent pipeline diagram (pipeline.png)."""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PURPLE = "#6D28D9"

fig, ax = plt.subplots(figsize=(9.5, 2.4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

boxes = [
    ("Speech-to-text\nwhisper-large-v3", 2.0),
    ("LLM\nllama-3.1-8b-instruct", 5.0),
    ("Text-to-speech\nkokoro-82m", 8.0),
]
for label, x in boxes:
    ax.add_patch(FancyBboxPatch((x - 1.15, 1.2), 2.3, 0.9, boxstyle="round,pad=0.08", fc=PURPLE, ec="none"))
    ax.text(x, 1.65, label, ha="center", va="center", color="white", fontsize=9.5, fontweight="bold")


def arrow(x0, x1, label=None):
    ax.annotate("", (x1, 1.65), (x0, 1.65), arrowprops=dict(arrowstyle="-|>", lw=2, color="#444"))
    if label:
        ax.text((x0 + x1) / 2, 1.98, label, ha="center", fontsize=8.5, color="#555")


ax.text(0.25, 1.65, "audio\nin", ha="right", va="center", fontsize=9)
arrow(0.35, 0.83)
arrow(3.2, 3.85, "text")
arrow(6.15, 6.8, "reply")
arrow(9.17, 9.65)
ax.text(9.75, 1.65, "audio\nout", ha="left", va="center", fontsize=9)
ax.text(5.0, 0.5, "one EcoHash API key  ·  api.ecohash.com/v1", ha="center", fontsize=9.5, color=PURPLE, fontweight="bold")

fig.tight_layout()
fig.savefig(os.path.join(HERE, "pipeline.png"), dpi=140, bbox_inches="tight")
print("wrote pipeline.png")
