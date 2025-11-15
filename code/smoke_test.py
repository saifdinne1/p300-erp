import sys, importlib

pkgs = [
    "numpy", "scipy", "pandas", "matplotlib",
    "mne", "mne_bids", "sklearn", "autoreject",
    "h5py", "tqdm", "requests"
]

missing = []
for p in pkgs:
    try:
        importlib.import_module(p)
        print(f"[OK] {p}")
    except Exception as e:
        print(f"[ERROR] {p}: {e}")
        missing.append(p)

print(f"Python: {sys.version}")
print("CI smoke test:", "PASS" if not missing else f"FAIL ({len(missing)} missing)")
sys.exit(1 if missing else 0)
