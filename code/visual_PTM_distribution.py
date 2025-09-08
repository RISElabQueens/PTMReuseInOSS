import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("model_types.csv")
df["model_type"] = df["model_type"].replace("multi_modal", "multi-modal")

type_counts = df['model_type'].value_counts()


#
plt.rcParams.update({
    "font.size": 16,        # base font size
    "axes.labelsize": 18,   # axis labels
    "xtick.labelsize": 14,  # x tick labels
    "ytick.labelsize": 14,  # y tick labels
    "legend.fontsize": 14
})

plt.figure(figsize=(7,5))
plt.bar(type_counts.index, type_counts.values, color="grey")

plt.ylabel("Number of PTMs", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

for i, count in enumerate(type_counts.values):
    plt.text(i, count + 2, str(count), ha='center', va='bottom', fontsize=13)

plt.ylim(0, type_counts.max() * 1.15)

plt.tight_layout()
plt.savefig("figures/model_type_distribution.pdf", format="pdf")
plt.close()


