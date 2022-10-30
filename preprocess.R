library(tidyverse)
data <- read_csv("Mental-Health-Twitter.csv")
text <- data$post_text
clean_tweet <- function(text){
  text <- gsub("?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)", "", text)
  text <- gsub("@\\S*", "", text) 
  text <- gsub("[\r\n]", "", text)
  text <- gsub("[[:punct:]]", "", text)
  text <- gsub("[^\x01-\x7F]", "", text)
  text <- gsub("amp ", "", text)
  text <- gsub("rt ", "", text)
  text <- gsub("\\d+\\w*\\d*", "", text)
  text <- gsub("\n", " ", text)
  text <- gsub("^\\s+", "", text)
  text <- gsub("\\s+$", "", text)
  text <- gsub("[ |\t]+", " ", text)
  return(text)
}

text <- tolower(text)
text <- clean_tweet(text)
data$post_text <- as.vector(text)
write.csv(data, file="data/processed_tweets.csv")