import numpy as np
import neurokit2 as nk
from preprocess import preprocess_ecg, preprocess_eeg
from visualization import plot_signals, plot_coherence

import sys
import os

# Get the project root directory (parent of src)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.ecg_signals import importECG
from data.eeg_signals import importEEG
from preprocess import preprocess_ecg, preprocess_eeg

# Simulate Signals
sampling_rate = 1000

""" ecg_signals = importECG()
eeg_signals = importEEG() """

def chooseMethod():
    """Function to let the user choose the method."""

    print("\nChoose Processing Method:")
    print("1. Bulk Processing (Large Dataset Analysis)")
    print("2. Pairwise Processing (Individual Subject Correlation)\n")

    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        print("\nRunning Bulk Processing Method...\n")
        """bulk_processing()"""

    elif choice == "2":
        print("\nRunning Pairwise Processing Method...\n")
        """pairwise_processing()"""
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

chooseMethod()

""" 
# Preprocess
ecg_cleaned, r_peaks = preprocess_ecg(ecg_signal)
eeg_filtered = preprocess_eeg(eeg_signal)

# Extract Features
hrv_features = extract_hrv(ecg_cleaned, r_peaks)
frequencies, coherence_values = compute_coherence(ecg_cleaned, eeg_filtered)

# Visualize
plot_signals(ecg_cleaned, eeg_filtered)
plot_coherence(frequencies, coherence_values) """