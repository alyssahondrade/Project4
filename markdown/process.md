# Process

## Table of Contents
1. [Introduction]()
2. [Data Cleaning]()
    1. [Metadata]()
        1. [Skew Function]()
        2. [Encoding]()
    2. [Spectrograms]()


## Introduction
The intent is to build a modularised workflow to minimise repetition and optimise the ML model workflow (build, train, test, optimise).
1. Convert the `wfdb` to `wav` format for use with python libraries to extract features.
2. Extract features and store in a dataframe.
3. Data cleaning for storage in SQL database.
4. Build machine learning models:
    - CNN for visual features (spectrogram)
    - RNN for features with temporal component (MFCCs)

## Data Cleaning

### Metadata
1. Simplify the column names: lowercase and underscores
2. Convert `NU` values to `NaN`
3. Clean categorical columns
4. Clean numerical columns

#### Skew Function
Due to the dataset size, needed to minimise dropping rows, used imputation instead. Skew function used to determine whether to use `mean` or `median` to impute missing values.
- Close to `0` means relatively symmetric, use: `mean`.
- Close to `-1` means skewed to the left (negatively skewed), use: `median`.
- Close to `1` means skewed to the right (positively skewed), use: `median`.

#### Encoding
Following encoding used for categorical columns
- `smoker` column
	- `0` for `no`
	- `1` for `casual`
	- `2` for `yes`
- `alcohol_consumption` column
	- `0` for `nondrinker`
	- `1` for `casual`
	- `2` for `habitual`
- `carbonated_beverages`, `tomatoes`, `coffee`, `chocolate`, `soft_cheese`, `citrus_fruits` columns
	- `0` for `never`
	- `1` for `almost_never`
	- `2` for `sometimes`
	- `3` for `almost_always`
	- `4` for `always`


### Spectrograms