# Game of Thrones Challenge

## Introduction

This repository is for Game of Thrones Challenge

## Data Source:

http://anapioficeandfire.com/api/

## Data Set Information:

This challenge will involve querying an API and extracting information from it. The API in question provides information on Game of Thrones, allowing one to access information on the houses, characters and books.

* API URL: http://anapioficeandfire.com/api/{SECTION}/{INDEX}

Where SECTION can be either ‘books’, ‘characters’, or ‘houses’ and INDEX is an integer to a certain entry in a section.

For example, to access the character Peter Baelish, the full request would be http://anapioficeandfire.com/api/characters/823, where 823 is the index corresponding to that character. 

It's recommended to read the full documentation, which can be found here: https://anapioficeandfire.com/Documentation

## Attribute Information:

## Environment Setup

If your `conda` base environment is old, it is important thet you install the `setuptools` and `wheel` packages that are dependencies for `autugluon`.

```
pip install setuptools wheel
```

Step 1: Create Environment
```
conda create --name apichallengenv python=3.9 -y
```

Step 2: Activate Environment
```
conda activate apichallengenv
```

Step 3: Install required packages
NB: This for Windows

```bash
pip install torch==1.12.1+cpu torchvision==0.13.1+cpu torchtext==0.13.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install autogluon matplotlib seaborn scikit-learn request xgboost geopy geocoder folium cufflinks nltk textblob vaderSentiment wordcloud jupyter
```


## Exploratory Data Analysis (EDA)

## Features Engineering and processing

## Model Building

## Model Evaluation

## Model Deployment

