import mne
import comet

# Suppress warnings
mne.set_log_level('ERROR')
import warnings
warnings.filterwarnings("ignore",module="pymatreader.utils")

lpp_results = []
subjects = ["21013", "21014", "21015", "21017", "21022"]

for subject in subjects:
    # Load data
    raw = mne.io.read_raw_eeglab(f"data/eeg/{subject}_E4/{subject}_E4_postICA_interpolated_fixed.set", preload=True)

    # Epoch data
    event_map = {f"S {i:2d}": i for i in [18,19,28,29,38,39,48,49,56,58,68,69,78,79]}
    events, _ = mne.events_from_annotations(raw, event_id=event_map)
    epochs = mne.Epochs(raw, events, event_id=None, tmin=-0.2, tmax=0.8, baseline=None, preload=True, reject=dict(eeg=150e-6))

    # Baseline correction
    epochs.apply_baseline((-0.1, 0))

    # Re-reference
    epochs.set_eeg_reference('average')

    # Crop (subject average peak or specified window)
    window = (0.4, 0.6)
    if (0.4, 0.6) == 'SAV':
        channel, time = epochs.average().get_peak(ch_type='eeg', tmin=0.3, mode='abs')
        epochs.crop(time-0.1, time+0.1)
    else:
        epochs.crop(window[0], window[1])

    # Pick electrodes for LPP estimation
    picks = mne.pick_channels(epochs.ch_names, include=['P3', 'Pz', 'P4'], exclude=[])

    # Get LPP as mean amplitude over epochs, channels & timepoints
    data = epochs.get_data() # (n_epochs, n_ch, n_times)
    lpp = data[:, picks, :].mean()
    lpp_results.append(lpp)

# Save results
comet.utils.save_universe_results({"LPP": lpp_results})