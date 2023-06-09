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

We would like you to answer the following:

a) What index corresponds to the house “House Breakstone”?
 
b) How many males, females and unknown genders are there in the first 40 characters? Note, index 0 does not correspond to a character, so full range is 1 - 40 both ends inclusive. 

c) How many books can be accessed from this API?

d) How many books does the character ‘High Septon’ appear in? (ignoring ‘povcharacters’) 

Hint: index value of Septon needs to be found first; it is smaller than 20.

__File type manipulation and formatting__

Three files are presented, one CSV, one TXT and one JSON file. Each contain 1000 rows of data. There are two challenges, both involving collating these files into one data frame. The fields in all files are:

'author.properties.friends',  'author.properties.status_count',  'author.properties.verified',  'content.body',  'location.country',  'properties.platform',  'properties.sentiment',  'location.latitude',  'location.longitude'

where the ‘.’ Indicates a nested field.
 
a) Begin by collating the CSV and TXT files together into one pandas dataframe. The resulting dataframe should be 2000 rows and have all of the columns present in both files.

b) Next, using the created dataframe, integrate the data from the JSON file into the existing columns. The resulting dataframe should now be 3000 rows long.

__Data exploration__

In this challenge we would like to know something interesting about the data. You are free to explore as you wish, producing plots, tables, statistics, etc. Feel free to use any variables in the dataset or include external data you may consider relevant to complement your analysis.  

__Model creation__

For this task you can use AutoGluon or you preferred algorithm.

This final task involves creating a predictive model for a response variable, given a set of features. The task is to create a predictive model for the variable ‘properties.sentiment’ using the remaining features in the data set. 

The data files attached should be used to create the model.  

What we would like to see from this task is your thoughts and decisions on training and testing a model. This will include, but not limited to, considering aspects such as feature selection & creation, parameter tuning of the model and train / validation / test split. 

This task is a blank canvas to work with. The only caveat is that you must be able to explain the methods and models you are using.

## Environment Setup

If your `conda` base environment is old, it is important thet you install the `setuptools` and `wheel` packages that are dependencies for `autugluon`.

```
pip install setuptools wheel
```

Step 1: Create Github Repository
```
https://github.com/OOlatubosun/datahackerman_final_project
```

Step 2: Clone repository on your local computer
```
https://github.com/OOlatubosun/datahackerman_final_project.git
```


Step 3: Create Environment
```
conda env create --file environment.yml
conda create --name apichallengenv python=3.9 -y
```

Step 4: Activate Environment
```
conda activate apichallengenv
```

Step 5: Install required packages
NB: This for Windows

```bash
pip install torch==1.12.1+cpu torchvision==0.13.1+cpu torchtext==0.13.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install autogluon matplotlib seaborn scikit-learn request xgboost geopy geocoder folium cufflinks nltk textblob vaderSentiment wordcloud jupyter
```

## API Access
```
pip install -q requests
```

## Data Merging
```bash
csv_text_data = pd.concat([csv_data, text_data]).reset_index(drop=True)
final_data = pd.concat([csv_text_data, json_data]).reset_index(drop=True)
final_data.to_csv('final_data.csv', index = False)
```

## Exploratory Data Analysis (EDA)
Import merged data thus:
```bash
file_name = "final_data.csv"
final_data = pd.read_csv(file_name)
``` 
## Model Creation
```
train_data, test_data = train_test_split(final_model_data,test_size = 0.30, random_state =42)
```

### Test your instructions as follows:

```bash
(apichallengenv) C:\Users\User\Documents\workspace_datahackerman\final_project\datahackerman_final_project>python
Python 3.9.16 (main, Mar  8 2023, 10:39:24) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from autogluon.tabular import TabularDataset, TabularPredictor
```

If that works, then you have good installation for `autogluon`.

And then for `Streamlit`,

```bash
(apichallengenv) C:\Users\User\Documents\workspace_datahackerman\final_project\datahackerman_final_project>streamlit hello

  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.255.187:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!

  This will automatically pop up on your default browser on this address - `http://localhost:8501/`
  ```

  
## Project Structure

```
GOT Challenge
|--READ.md
|--datasets
|--HFP01_Game_of_Thrones_API_Access.ipynb
|--HFP02_Dataframe_Merging.ipynb
|--HFP03_Data_Exploration.ipynb
|--HFP04_Model_Creation.ipynb
|--final_data.csv
|--app.py
|--environment.yml
|--requirements.txt
```

Deployment will be done on `Streamlit`.

