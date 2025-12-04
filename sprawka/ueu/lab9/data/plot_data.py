import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure img directory exists
os.makedirs('img', exist_ok=True)

# Read data
# The file has a header line, and uses tabs/spaces. Decimal is comma.
# Freq  (Hz) 	 Gain (Linear)  	 Phase (deg)
try:
    df = pd.read_csv('data/zad1.txt', sep=r'\s+', decimal=',')
except Exception as e:
    print(f"Error reading file: {e}")
    exit(1)

# Rename columns for easier access if needed, but index is safer if names vary
# Assuming 3 columns
freq = df.iloc[:, 0]
gain = df.iloc[:, 1]
phase = df.iloc[:, 2]

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 10))

# Gain
ax1.plot(freq, gain, 'b.-')
ax1.set_ylabel('Gain (Linear)')
ax1.set_title('Bode Plot')
ax1.grid(True, which="both", ls="-")
ax1.set_xscale('log')

# Phase
ax2.plot(freq, phase, 'r.-')
ax2.set_ylabel('Phase (deg)')
ax2.set_xlabel('Frequency (Hz)')
ax2.grid(True, which="both", ls="-")
ax2.set_xscale('log')

plt.tight_layout()
plt.savefig('img/charakterystyka.png')
print("Plot saved to img/charakterystyka.png")
