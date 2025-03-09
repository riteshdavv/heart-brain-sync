from scipy.signal import coherence
import neurokit2 as nk

def extract_hrv(ecg_signal, r_peaks, sampling_rate=1000):
    """Extract Heart Rate Variability (HRV) features from ECG."""
    hrv_features = nk.hrv_time(r_peaks, sampling_rate=sampling_rate)
    return hrv_features

def compute_coherence(ecg_signal, eeg_signal, sampling_rate=1000):
    """Compute EEG-ECG coherence to measure synchronization."""
    f, Cxy = coherence(ecg_signal, eeg_signal, fs=sampling_rate)
    return f, Cxy