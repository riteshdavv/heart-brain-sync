import numpy as np
import neurokit2 as nk
from preprocess import preprocess_ecg, preprocess_eeg
from feature_extraction import extract_hrv, compute_coherence
from visualization import plot_signals, plot_coherence

import sys
import os

# Get the project root directory (parent of src)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.ecg_signals import importECG  # Now it should work!
from data.eeg_signals import importEEG

# Simulate Signals
sampling_rate = 1000

importECG()

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