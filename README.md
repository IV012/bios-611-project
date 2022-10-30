## Dataset  
**Depression: Twitter Dataset + Feature Extraction**  
20000 Labelled English Tweets of Depressed and Non-Depressed Users  
Link: https://www.kaggle.com/datasets/infamouscoder/mental-health-social-media  
  
## Description  
The data is in uncleaned format and is collected using Twitter API. The Tweets has been filtered to keep only the English context. It targets mental health classification of the user at Tweet-level.  
Data structure:  
| Post Date | Time of the tweet being published.                                 |
|-----------|--------------------------------------------------------------------|
| Text      | The content of this tweet.                                         |
| Followers | The number of followers of this account.                           |
| Friends   | The number of friends (followed by and following) of this account. |
| Favorites | The number of "like"s.                                             |
| Statuses  | The number of activities of the account owner.                     |
| Retweet   | The number of retweets.                                            |
| Label   | The mental status, whether depression or not. |                                           

## Goal  
1. EDA: label distribution, word frequency, text length...  
2. Statistical Modelling: prediction, clustering...

## Manual  
#### Build docker image and run the container  
```docker
docker build . -t project
docker run -v $(pwd):/home/rstudio -e PASSWORD=yfd -p 8787:8787 -t project
```

#### Generate files, results and the report  
```makefile
make clean
make .create-dirs
make data/processed_tweets.csv
make figure/density.png
make figure/negative.html figure/positive.html figure/negative.png figure/positive.png
make report.pdf
```
