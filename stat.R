library(tidyverse)
set.seed(99)
data <- read_csv("data/processed_tweets.csv")
wordcount <- str_count(data$post_text, "\\w+")
label <- data$label[!is.na(wordcount)]
wordcount <- wordcount[!is.na(wordcount)]
mu <- data.frame(wc.mean = c(mean(wordcount[label==0]), 
                             mean(wordcount[label==1])), 
                 label = c(0, 1))
df <- data.frame(wordcount=wordcount, label=as.factor(label))
mu <- df %>% 
  group_by(label) %>%
  summarise(wc.mean = mean(wordcount))
dens <- ggplot(df, aes(wordcount)) + 
  geom_density(aes(fill = label), alpha = 0.4) +
  geom_vline(aes(xintercept = wc.mean, color = label),
             data = mu, linetype = "dashed") +
  scale_color_manual(values = c("#3D85C6", "#EFC000FF")) +
  scale_fill_manual(values = c("#3D85C6", "#EFC000FF"))
ggsave("figure/density.png", dens, width = 8, height = 5)