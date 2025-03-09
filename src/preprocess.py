import numpy as np
import pandas as pd
import neurokit2 as nk
import mne

def preprocess_ecg(ecg_signal, sampling_rate=1000):
    """Cleans ECG, detects R-peaks, and computes HRV features."""
    ecg_cleaned = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)
    r_peaks, _ = nk.ecg_peaks(ecg_cleaned, sampling_rate=sampling_rate)
    hrv_features = nk.hrv_time(r_peaks["ECG_R_Peaks"], sampling_rate=sampling_rate)
    
    return ecg_cleaned, hrv_features

def preprocess_eeg(eeg_signal, sampling_rate=1000):
    """Cleans EEG and computes power bands."""
    info = mne.create_info(ch_names=["EEG"], sfreq=sampling_rate, ch_types=["eeg"])
    raw_eeg = mne.io.RawArray(eeg_signal.reshape(1, -1), info)
    raw_eeg.filter(1, 50, fir_design="firwin")
    
    psd, freqs = mne.time_frequency.psd_array_welch(raw_eeg, fmin=1, fmax=50)
    theta_power = np.mean(psd[(freqs >= 4) & (freqs <= 8)])
    alpha_power = np.mean(psd[(freqs >= 8) & (freqs <= 13)])
    
    return raw_eeg, theta_power, alpha_power