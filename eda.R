library(tidyverse)
library(tidytext)
library(RColorBrewer)
library(wordcloud2)
library(stopwords)
library(webshot)
library(htmlwidgets)

data <- read_csv("data/processed_tweets.csv")
data("stop_words")
stop_words$word <- gsub("[[:punct:]]", "", stop_words$word)
set.seed(100)
words <- data %>% filter(label==1) %>% 
  select(post_text) %>% 
  unnest_tokens(word, post_text)
words <- words %>% anti_join(stop_words, by = "word")
words <- words %>% count(word, sort = TRUE)
negative <- wordcloud2(data=words, size=0.8, color='random-dark')
saveWidget(negative,"figure/negative.html",selfcontained = F)
webshot("figure/negative.html","figure/negative.png",
        vwidth = 1080, vheight = 720, delay = 5)

words <- data %>% filter(label==0) %>% 
  select(post_text) %>% 
  unnest_tokens(word, post_text)
words <- words %>% anti_join(stop_words, by = "word")
words <- words %>% count(word, sort = TRUE)
positive <- wordcloud2(data=words, size=0.8, color='random-dark')
saveWidget(positive,"figure/positive.html",selfcontained = F)
webshot("figure/positive.html","figure/positive.png",
        vwidth = 1080, vheight = 720, delay = 5)