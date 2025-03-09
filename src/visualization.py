import matplotlib.pyplot as plt
import seaborn as sns

def plot_signals(ecg, eeg, sampling_rate=1000):
    """Plot the ECG and EEG signals together"""
    plt.figure(figsize=(12, 5))
    plt.plot(ecg, label="ECG Signal", color="red", alpha=0.7)
    plt.plot(eeg, label="EEG Signal", color="blue", alpha=0.7)
    plt.legend()
    plt.title("ECG & EEG Signals")
    plt.show(block=True)

def plot_coherence(frequencies, coherence_values):
    """Plot Convergence Spectrum"""
    plt.figure(figsize=(10, 4))
    plt.semilogy(frequencies, coherence_values)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Coherence")
    plt.title("Brain-Heart Synchronization")
    plt.show(block=True)