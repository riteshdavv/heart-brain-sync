import numpy as np
import pandas as pd
import neurokit2 as nk
import scipy.signal as signal

def preprocess_ecg(ecg_signal, sampling_rate=1000):
    """Preprocess ECG: Denoise, filter, detect R-peaks."""
    ecg_cleaned = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)
    r_peaks, _ = nk.ecg_peaks(ecg_cleaned, sampling_rate=sampling_rate) # ["ECG_R_Peaks"]
    return ecg_cleaned, r_peaks["ECG_R_Peaks"]

def preprocess_eeg(eeg_signal, sampling_rate=1000):
    """Preprocess EEG: Bandpass filter."""
    b, a = signal.butter(4, [0.5, 30], btype='band', fs=sampling_rate)
    eeg_filtered = signal.filtfilt(b, a, eeg_signal)
    return eeg_filtered