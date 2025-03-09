import os
import torch
import numpy as np

# Directory containing the files
data_directory = "E:/Cap Sleep Database - Disorder Classification/ecg"

ecg_signals = []

def importECG():
    for filename in os.listdir(data_directory):
        if filename.endswith(".pt"):
            file_path = os.path.join(data_directory, filename)
            print(f"Processing (ECG): {filename}")
            global ecg_signals
            try:
                tensor_data = torch.load(file_path)
                print(f"Loaded {filename}, Shape: {tensor_data.shape}")
                ecg_signals.append(tensor_data)
                print(ecg_signals)
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    return ecg_signals