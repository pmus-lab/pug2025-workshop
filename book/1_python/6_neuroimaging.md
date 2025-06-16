---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# <i class="fa-brands fa-python"></i> Neuroimaging

Neuroimaging libraries depend on the specific modality you are dealing with. While there are *many* packages out there, this section will introduce the most widely used ones, which you will also need for the practical part of the workshop tomorrow.

## fMRI

**NiBabel**

Core I/O support for neuroimaging file formats (NIfTI, Analyze, MGH, MINC, etc.). Provides utilities to load, save, and manipulate image headers and data arrays.

- PyPI: https://pypi.org/project/nibabel/
- Docs: https://nipy.org/nibabel/

**Nilearn**

High-level statistical learning and visualization on neuroimaging data. Built on scikit-learn, it offers functions for decoding, predictive modeling, functional connectivity, and easy plotting of brain maps.

- PyPI: https://pypi.org/project/nilearn/
- Docs: https://nilearn.github.io/


### Usage Examples

Let's look at some real data to get a better sense of why arrays are a useful thing to use. We use the `nilearn` package to load fMRI data of a single subject from the ADHD dataset and then convert the data into a numpy array with the `nibabel` package:

```{code-cell} ipython3
from nilearn import datasets
import nibabel as nib

haxby_dataset = datasets.fetch_adhd(n_subjects=1); # Download the Haxby dataset
fmri_img = nib.load(haxby_dataset.func[0])         # Load the fMRI data using nibabel
fmri_data = fmri_img.get_fdata()                   # Convert to a 4D numpy array
print(f"Shape of the fMRI data: {fmri_data.shape}")
```

You can see that the data has shape `(61, 73, 61, 176)`, meaning that it has four dimensions. fMRI data is similar to a picture which is composed of individual pixels, with the addition that the brain is a three-dimensional object and is thus separated in little cubes called *voxels*. As such three-dimensional scans are aquired in slices, the first two dimensions are the in-plane dimensions of the scan ($61 * 73$ voxels), the third dimension are the $61$ slices, and the third dimension is the time, telling us that $176$ scans of the brain were obtained over time.




## EEG

**MNE-Python**

The go-to package for EEG/MEG data: supports raw‐data I/O (EDF, BDF, BrainVision, etc.), preprocessing (filtering, ICA, SSP), epoching, time-frequency analysis, source localization (via FreeSurfer), connectivity, and powerful visualization routines.

- Docs: https://mne.tools/stable/index.html
- PyPI: https://pypi.org/project/mne/



