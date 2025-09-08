import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from io import StringIO

# -----------------------
# Load CSV
# -----------------------
df = pd.read_csv("stacked_counts.csv")

# -----------------------
# Sort by total repos
# -----------------------
df["total"] = df[["Multiple models", "Single model"]].sum(axis=1)
df = df.sort_values("total", ascending=False)

stacked_counts = df.set_index("type_label")[["Single model", "Multiple models"]]

# -----------------------
# Plotting side-by-side bars
# -----------------------
fig, ax = plt.subplots(figsize=(16,12))

colors = {
    "Single model": "#969696",
    "Multiple models": "#525252"
}

n = len(stacked_counts)
bar_width = 0.45
x = np.arange(n)

# Minimum height to make very small bars visible
min_display_val = 7

# Plot bars side-by-side
for i, col in enumerate(stacked_counts.columns):
    for j in range(n):
        val = stacked_counts.iloc[j, i]
        if val == 0:
            continue  # skip zero bars

        display_val = val if val >= min_display_val else min_display_val

        ax.bar(
            x[j] + i*bar_width,
            display_val,
            width=bar_width,
            color=colors[col],
            label=col if j==0 else ""  # only add label once for legend
        )

        # Text: show original value
        ax.text(
            x[j] + i*bar_width,
            display_val / 2,
            str(val),
            ha="center",
            va="center",
            fontsize=18,
            color="white" if col=="Multiple models" else "black"
        )

ax.set_xticks(x + bar_width/2)
ax.set_xticklabels(stacked_counts.index, rotation=45, ha="right", fontsize=24)
ax.set_ylabel("Number of Projects", fontsize=24)
ax.tick_params(axis="y", labelsize=18)

# Legend
ax.legend(fontsize=24, loc="upper right", frameon=False)

plt.tight_layout()
# plt.show()
plt.savefig("figures/emse_repo_type_stacked_linear.pdf", format="pdf")
