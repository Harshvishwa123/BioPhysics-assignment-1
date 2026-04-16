
import matplotlib.pyplot as plt

def read_profile(filename):
    x = []
    y = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = line.split()

            try:
                residue_index = int(float(parts[0]))
                dope_value = float(parts[-1])
                x.append(residue_index)
                y.append(dope_value)
            except (ValueError, IndexError):
                continue

    print(f"{filename}: read {len(x)} points")
    return x, y

def plot_profiles(profile_map, title, output_file, main_label):
    plt.figure(figsize=(10, 5.5))

    for label, file in profile_map.items():
        x, y = read_profile(file)

        if len(x) == 0 or len(y) == 0:
            print(f"Skipping {file} because no valid data was read.")
            continue

        if label == main_label:
            plt.plot(x, y, linewidth=2.0, label=label)
        else:
            plt.plot(x, y, linestyle="--", linewidth=1.2, label=label)

    plt.title(title)
    plt.xlabel("Residue Number")
    plt.ylabel("DOPE Score")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()
    print(f"Saved: {output_file}")

profiles_wt = {
    "Template 1": "7S37.profile",
    "Template 2": "6IFO.profile",
    "Template 3": "5F9R.profile",
    "Best WT Model": "wt_best.profile"
}

profiles_mut = {
    "Template 1": "7S37.profile",
    "Template 2": "6IFO.profile",
    "Template 3": "5F9R.profile",
    "Best MT Model": "mut_best.profile"
}

plot_profiles(
    profiles_wt,
    "DOPE Score Profile: Templates vs Best WT Model",
    "Templates_vs_Best_WT_Model.png",
    "Best WT Model"
)

plot_profiles(
    profiles_mut,
    "DOPE Score Profile: Templates vs Best Mutant Model",
    "Templates_vs_Best_Mutant_Model.png",
    "Best MT Model"
)