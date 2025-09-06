import matplotlib.pyplot as plt
import numpy as np

total_projects = 401

partial_sub = {"README only": 48, "Config only": 14, "Both README & Config": 18}
explicit_sub = {"README only": 62, "Config only": 6, "Both README & Config": 17}

categories = ["README only", "Config only", "Both README & Config"]
partial_counts = [partial_sub[cat] for cat in categories]
explicit_counts = [explicit_sub[cat] for cat in categories]

y_pos = np.arange(len(categories))
bar_height = 0.4

fig, ax = plt.subplots(figsize=(14, 5))


ax.barh(y_pos, partial_counts, height=bar_height, color="#969696", label="Partial")
ax.barh(y_pos, explicit_counts, left=partial_counts, height=bar_height, color="#525252", label="Explicit")


for i, (p, e) in enumerate(zip(partial_counts, explicit_counts)):
    ax.text(p/2, y_pos[i], f"{p/total_projects*100:.1f}%",
            va='center', ha='center', color='white', fontsize=18)
    ax.text(p + e/2, y_pos[i], f"{e/total_projects*100:.1f}%",
            va='center', ha='center', color='white', fontsize=18)

ax.set_xlabel("Number of Projects", fontsize=18)
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=18)
ax.tick_params(axis="x", labelsize=18)

ax.legend(title="", fontsize=18)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("fig_breakdown.pdf")
plt.show()
