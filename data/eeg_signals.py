import os
import torch
import numpy as np

# Directory containing the files
data_directory = "E:/Cap Sleep Database - Disorder Classification/eeg"

eeg_signals = []

def importEEG():
    for filename in os.listdir(data_directory):
        if filename.endswith(".pt"):
            file_path = os.path.join(data_directory, filename)
            print(f"Processing (EEG): {filename}")
            global eeg_signals
            try:
                tensor_data = torch.load(file_path)
                eeg_signals.append(tensor_data)
                print(eeg_signals)
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    return eeg_signals