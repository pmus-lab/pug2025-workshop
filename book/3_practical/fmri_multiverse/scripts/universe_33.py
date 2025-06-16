import comet
import numpy as np
from nilearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Get data (if it is preloaded this will skip the download)
data = datasets.fetch_abide_pcp(data_dir="./data", n_subjects=100, quality_checked=True, verbose=0,
                                pipeline='ccs',
                                derivatives='rois_cc200',
                                band_pass_filtering=True,
                                global_signal_regression=True)

time_series = data['rois_cc200']
diagnosis = data["phenotypic"]["DX_GROUP"]

# Calculate FC
tri_ix = None
features = []

for ts in time_series:
    FC = comet.connectivity.Static_Pearson(ts, **{}).estimate()

    if tri_ix == None:
        tri_ix = np.triu_indices_from(FC, k=1)

    feat_vec = FC[tri_ix]
    features.append(feat_vec)

# Prepare features (FC estimates) and target (autism/control)
X = np.vstack(features)
X[np.isnan(X)] = 0.0
y = np.array(diagnosis)

# Classification model
model = Pipeline([('scaler', StandardScaler()), ('reg', LogisticRegression(penalty='l2'))])
cv = StratifiedKFold(n_splits=10)
accuracies = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

# Save the results
comet.utils.save_universe_results({"accuracy": accuracies})