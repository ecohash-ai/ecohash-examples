"""Draw the Retell custom-LLM flow diagram (flow.png)."""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PURPLE = "#6D28D9"
SLATE = "#334155"

fig, ax = plt.subplots(figsize=(9.5, 3.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3.9)
ax.axis("off")

boxes = [
    ("Retell agent\n(custom LLM)", 1.6, SLATE),
    ("bridge\nserver.py", 5.0, PURPLE),
    ("EcoHash LLM\nllama-3.1-8b", 8.4, PURPLE),
]
for label, x, color in boxes:
    ax.add_patch(FancyBboxPatch((x - 1.15, 1.55), 2.3, 0.95, boxstyle="round,pad=0.08", fc=color, ec="none"))
    ax.text(x, 2.03, label, ha="center", va="center", color="white", fontsize=9.5, fontweight="bold")


def arrow(x0, x1, y):
    ax.annotate("", (x1, y), (x0, y), arrowprops=dict(arrowstyle="-|>", lw=2, color="#444"))


# request path: arrows in the gaps, labels above the boxes
arrow(2.85, 3.75, 2.25)
ax.text(3.3, 2.72, "WebSocket events\n(transcript, response_id)", ha="center", va="bottom", fontsize=8.5, color="#555")
arrow(6.25, 7.15, 2.25)
ax.text(6.7, 2.72, "/v1/chat/completions\n(stream: true)", ha="center", va="bottom", fontsize=8.5, color="#555")

# response path: arrows lower in the gaps, labels below the boxes
arrow(7.15, 6.25, 1.75)
ax.text(6.7, 1.32, "token deltas", ha="center", va="top", fontsize=8.5, color="#555")
arrow(3.75, 2.85, 1.75)
ax.text(3.3, 1.32, "streamed response events\n(content_complete on finish)", ha="center", va="top", fontsize=8.5, color="#555")

ax.text(5.0, 0.22, "one bridge server  ·  api.ecohash.com/v1", ha="center", fontsize=9.5, color=PURPLE, fontweight="bold")

fig.tight_layout()
fig.savefig(os.path.join(HERE, "flow.png"), dpi=140, bbox_inches="tight")
print("wrote flow.png")
