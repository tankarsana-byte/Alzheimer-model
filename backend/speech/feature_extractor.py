"""
Speech Feature Extractor for NeuroSense AI.
Extracts MFCC, Chroma, and Mel features from audio files.
"""
import numpy as np
import librosa
from typing import Dict


def extract_features(audio_path: str) -> np.ndarray:
    """
    Extract 65 acoustic features from an audio file.

    Args:
        audio_path: Path to the .wav audio file.

    Returns:
        numpy array of shape (65,) containing extracted features.
    """
    y, sr = librosa.load(audio_path, sr=None)
    features = []

    # MFCC features (13)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    features.extend(np.mean(mfccs.T, axis=0))

    # Chroma features (12)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    features.extend(np.mean(chroma.T, axis=0))

    # Mel spectrogram features (40)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    features.extend(np.mean(mel.T, axis=0)[:40])

    return np.array(features)


def get_feature_breakdown(audio_path: str) -> Dict:
    """Extract features broken down by type."""
    y, sr = librosa.load(audio_path, sr=None)

    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)

    return {
        "mfcc": np.mean(mfccs.T, axis=0),
        "chroma": np.mean(chroma.T, axis=0),
        "mel": np.mean(mel.T, axis=0)[:40],
        "duration_sec": librosa.get_duration(y=y, sr=sr),
        "sample_rate": sr,
    }


def get_audio_metadata(audio_path: str) -> Dict:
    """Return basic audio metadata."""
    y, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)
    return {
        "duration_sec": round(duration, 2),
        "sample_rate": sr,
        "num_samples": len(y),
    }
