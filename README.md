# FMCW Signal Process Toolkit

A Python implementation of signal processing algorithms 
for FMCW radar, covering the complete pipeline from raw beat 
signal to target detection.

## Algorithms Implemented

- **DFS** — Discrete Fourier Series for periodic signals
- **DFT** — Discrete Fourier Transform (matrix method, O(N²))
- **FFT** — Cooley-Tukey radix-2 recursive FFT (O(N log N))
- **CA-CFAR** — Cell-Averaging Constant False Alarm Rate detection

## Pipeline
Beat Signal → 1D FFT (Range) → 2D FFT (Range-Doppler) → CA-CFAR → Target Detection

## Quick Start

```bash
git clone https://github.com/LukeJia47/fmcw-signal-process-toolkit
cd fmcw-signal-process-toolkit
pip install -r requirements.txt
python pipeline/radar_pipeline.py
```

## Requirements

Python 3.8+, NumPy, Matplotlib
