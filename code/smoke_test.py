# Minimal smoke test: verify libs, write tiny artifacts
import os, sys, json, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

VERS = {
    "python": sys.version.split()[0],
}

# optional imports; okay if they exist already
try:
    import mne; VERS["mne"] = mne.__version__
except Exception as e:
    VERS["mne"] = f"import-failed: {e}"

try:
    import pandas as pd; VERS["pandas"] = pd.__version__
except Exception as e:
    VERS["pandas"] = f"import-failed: {e}"

outdir = "outputs_smoke"
os.makedirs(outdir, exist_ok=True)

# write versions
with open(os.path.join(outdir, "versions.json"), "w", encoding="utf-8") as f:
    json.dump(VERS, f, indent=2)

# make a tiny PNG so CI uploads something
x = np.linspace(-1, 1, 200)
y = np.exp(-(x*4)**2)  # a little “P300-like” bump-ish curve
plt.figure()
plt.plot(x, y)
plt.title("Smoke curve")
plt.xlabel("time (a.u.)"); plt.ylabel("amplitude (a.u.)")
plt.savefig(os.path.join(outdir, "smoke.png"), dpi=120)

print("SMOKE OK")
