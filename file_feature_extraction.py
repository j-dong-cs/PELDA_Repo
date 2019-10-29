from scipy.io.wavfile import *
from numpy import *

import feature_mfccs_init
import feature_mfccs
import getDFT


# Jingjing Dong
# 02/13/2015
# This script reads signal data from WAV files, segment audio files into
# audio frames, and extract features from each audio frame.
#
# Arguments:
# - signal:   the audio signal
#   - fs:       the sampling frequency
#   - win:      short-term window size (default in 0.032 seconds)
#   - step:     short-term step (default in 0.016 seconds - 50% overlap)
def file_feature_extraction(file, win=0.032, step=0.016):
    # read in digital signal from audio file
    audioInfo = read(file)
    fs = audioInfo[0]
    signal = audioInfo[1]

    # Converting stereo signal to MONO signal
    if (len(signal[0]) > 1):
        signal = float_(sum(signal, axis=1)) / 2

    # short-term feature extraction
    numberOfSamples = len(signal)
    duration = float_(numberOfSamples) / fs  # in seconds

    # convert window length and step from seconds to samples
    windowLength = int(round(win * fs))
    stepInSamples = int(round(step * fs))

    # compute the total number of frames
    numOfFrames = int(floor((numberOfSamples - windowLength) / stepInSamples) + 1)

    # number of features to be computed:
    numbOfFeatures = 13
    Features = zeros((numOfFrames, numbOfFeatures))
    Ham = hamming(windowLength)
    mfccParams = feature_mfccs_init.feature_mfccs_init(windowLength, fs)

    curPos = 1
    for i in range(0, numOfFrames):  # for each frame
        # get current frame:
        frame = signal[curPos - 1: curPos + windowLength - 1]
        frame = frame * Ham
        frameFFT = getDFT.getDFT(frame, fs)

        if sum(abs(frame)) > spacing(1):
            MFCCs = feature_mfccs.feature_mfccs(frameFFT, mfccParams)
            Features[i][0:13] = MFCCs
        else:
            Features[:, i] = zeros(numberOfFeatures, 1)
        curPos = curPos + stepInSamples
        frameFFTPrev = frameFFT
    return Features