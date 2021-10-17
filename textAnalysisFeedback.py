# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:53:36 2021

@author: deanp

IDEA Semantic Analysis
"""

#%% Libraries
import pandas as pd
import sys
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#%% Read Data
path = 'C:/Users/deanp/OneDrive/Desktop/Fall 2021/IDEA/Q17/Set Stage Pitches - Feedback-2021-10-11-23-02-28.xlsx - Set Stage Pitches - Feedback.csv'
ready_stage = pd.read_csv(path)

#%% Make feedback columns strings

ready_stage["Areas Doing Well"]=ready_stage["Areas Doing Well"].apply(str)
ready_stage["Areas That Need Improvement"]=ready_stage["Areas That Need Improvement"].apply(str)

#%% Declare sentiment analyzer object

sid = SentimentIntensityAnalyzer()

#%% Example Output
a = 'This was a good movie.'
print(sid.polarity_scores(a))

#%% Loop to produce sentiment scores

area_well_scores = [None] * len(ready_stage)
area_improvements_scores = [None] * len(ready_stage)


for i in range(0, len(ready_stage)):
    print(ready_stage.iloc[i]['Account Name'])
    areas_doing_well = ready_stage.iloc[i]['Areas Doing Well']
    areas_improvement = ready_stage.iloc[i]['Areas That Need Improvement']
    if areas_doing_well != 'nan':
        area_well_scores[i] = sid.polarity_scores(areas_doing_well)
    if areas_improvement != 'nan':
        area_improvements_scores[i] = sid.polarity_scores(areas_improvement)

#%% Assign scores to new row

ready_stage["Areas Doing Well- Sentiment Scores"] = area_well_scores
ready_stage["Areas That Need Improvement- Sentiment Scores"] = area_improvements_scores

#%% Loop to take out null feedback scores

to_drop = []
for i in range(0, len(ready_stage)):
    areas_doing_well = ready_stage.iloc[i]['Areas Doing Well']
    areas_improvement = ready_stage.iloc[i]['Areas That Need Improvement']
    if areas_doing_well == 'nan' or areas_improvement == 'nan':
        to_drop.append(i)

ready_stage.drop(labels=to_drop, axis=0, inplace=True)
#%% Creating new columns for compound scores

ready_stage['Areas Doing Well - compound']  = ready_stage['Areas Doing Well- Sentiment Scores'].apply(lambda score_dict: score_dict['compound'])
ready_stage['Areas That Need Improvement - compound']  = ready_stage['Areas That Need Improvement- Sentiment Scores'].apply(lambda score_dict: score_dict['compound'])

#%% Create Pos or Neg Column based on compound scores

ready_stage['comp_score1'] = ready_stage['Areas Doing Well - compound'].apply(lambda c: 'pos' if c >=0 else 'neg')
ready_stage['comp_score2'] = ready_stage['Areas That Need Improvement - compound'].apply(lambda c: 'pos' if c >=0 else 'neg')


#%% Loop to get scores for passing and non-passing ventures

yes_well_scores = []
yes_improvement_scores = []
no_well_scores = []
no_improvement_scores = []
for i in range(0, len(ready_stage)):
    well_compound = ready_stage.iloc[i]['Areas Doing Well - compound']
    improvement_compound = ready_stage.iloc[i]['Areas That Need Improvement - compound']
    pass_yesNo = ready_stage.iloc[i]['Pass']
    if pass_yesNo == 'No':
        no_well_scores.append(well_compound)
        no_improvement_scores.append(improvement_compound)
    else:
        yes_well_scores.append(well_compound)
        yes_improvement_scores.append(improvement_compound)
        
#%% Computing Median sentiment scores for passing and non-passing

passing_well_median = np.median(yes_well_scores)
passing_improvement_median = np.median(yes_improvement_scores)
notpassing_well_median = np.median(no_well_scores)
notpassing_improvement_median = np.median(no_improvement_scores)


