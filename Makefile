.PHONY: clean
SHELL: /bin/bash

clean:
	rm -f data/*
	rm -r -f figure/*
	rm -r -f result/*
	

.create-dirs:
	mkdir -p figure
	mkdir -p data
	mkdir -p result

data/processed_tweets.csv: Mental-Health-Twitter.csv preprocess.R
	Rscript preprocess.R
	
figure/density.png: stat.R data/processed_tweets.csv
	Rscript stat.R
	
figure/negative.html figure/positive.html figure/negative.png figure/positive.png: eda.R data/processed_tweets.csv
	Rscript eda.R

figure/follower_month.png figure/follower_year.png figure/freq_month.png figure/freq_year.png: eda.py data/processed_tweets.csv
	python3 eda.py

model/model_lstm.pt figure/loss.png: model.py network/train.py network/train_prepare.py data/processed_tweets.csv
	python3 network/train.py

result/cm_lstm.png: model.py network/eval.py network/train_prepare.py data/processed_tweets.csv model/model_lstm.pt
	python3 network/eval.py

result/cm_bnb.png: data/processed_tweets.csv bernoulli.py
	python3 bernoulli.py

report.pdf: figure/density.png figure/negative.png figure/positive.png report.Rmd
	R -e "rmarkdown::render(\"report.Rmd\", output_format=\"pdf_document\")"
