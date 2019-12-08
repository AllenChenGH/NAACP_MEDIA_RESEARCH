# NAACP_MEDIA_RESEARCH

CS506 Spark! project

Yufeng Chen, yufeng72@bu.edu

Jiaqi Sun, sjq@bu.edu

Ruotian Liu, rtliu@bu.edu

## SOME INSTRUCTIONS ON HOW TO RUN OUR CODE:

Collect data: run [get_links.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/get_links.py) first to get 3 txt files ([bostonglobe.txt](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/bostonglobe.txt), [wbur.txt](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/wbur.txt) and [wgbh.txt](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/wgbh.txt)) of 3 websites, then run Scrapy..................... This process will take a long time and we splitted these 3 txts into more small sub files when we did this step. We stored our data in [raw data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/raw%20data), and suggest you simply download it to see what we've collected.

Filter news about black people: make sure you've already generated (by run [combine.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/combine.py) on [raw data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/raw%20data) or downloaded [classified data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/classified%20data), then run [keywords_filter_black.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/keywords_filter_black.py). The results should be generated in [relevent data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/relevant%20data) folder.

Calculate coverage: make sure you've already generated (by run [combine.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/combine.py) on [raw data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/raw%20data)) or downloaded [classified data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/classified%20data), then run [coverage.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/coverage.py). The result should be printed on your screen. It's also recorded in [statistics_final.xlsx](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/statistics_final.xlsx) sheet one.

Sentiment analysis: make sure you've already generated (by run [combine.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/combine.py) on [raw data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/raw%20data) and [keywords_filter_black.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/keywords_filter_black.py) on [classified data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/classified%20data) or downloaded [classified data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/classified%20data) and [relevent data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/relevant%20data), then run [sentiment_analysis_black.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/sentiment_analysis_black.py) and [sentiment_analysis_all.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/sentiment_analysis_all.py). The results should be stored in [sentiment_analysis_black.csv](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/sentiment_analysis_black.csv) and [sentiment_analysis_all.csv](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/sentiment_analysis_all.csv). The results are also recorded in [statistics_final.xlsx](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/statistics_final.xlsx) sheet one.

Look for popular topics: make sure you've already generated (by run [combine.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/combine.py) on [raw data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/raw%20data)) or downloaded [classified data](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/classified%20data), then run [get_topics.py](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/get_topics.py) to get popular topics and see visulization results like [topic_crime_black.png](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/topic_crime_black.png) and [topic_crime_all.png](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/topic_crime_all.png). you can change code to get all popular topics for the past five years. The results are stored in [5topics_black.txt
](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/5topics_black.txt) and [5topics_all.txt
](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/5topics_all.txt), The results are also stored in [statistics_final.xlsx](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/blob/master/statistics_final.xlsx) sheet two.

To run all codes, please make sure to follow our project structure, or yhou can change the target directory in our codes into your own valid path.

## FOR NON-TECHNICAL AUDIANCE

If you are non-technical audiance who just want to see what we've achieved, please have a look [here](https://github.com/AllenChenGH/NAACP_MEDIA_RESEARCH/tree/master/Report%26Poster) at our project report and poster. This should give you an basic idea of what we've done.
