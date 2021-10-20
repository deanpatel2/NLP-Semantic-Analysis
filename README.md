# Venture-Semantic-Analysis

This is a semantic analysis project which is aimed at generating value from the past 12 years of feedback on ventures for [IDEA](https://www.northeastern.edu/idea/), one of the largest student-led venture accelerators in the nation.

The venture team has asked us (the data team) to characterize the commonalities in the feedback of those ventures which make it into further stages in the launch process and eventually receive funding.

### Tools Used: VADER

VADER is a sentiment analysis library which allows you to describe the polarity of natural language. It is particularly well-tuned to feedback data (short, few sentences entries). You can find more about it [here](https://github.com/cjhutto/vaderSentiment). 

In this project, I am using VADER to interrogate the feedback on a more quantitative level and help characterize successful ventures as the venture team has requested. In the future, using sentiment scores may be one of several features in a more comlpex model to potentially identify which data we track has the most predictive power in venture success.
