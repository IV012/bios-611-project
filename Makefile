.PHONY: clean
SHELL: /bin/bash

clean:
	rm -f data/*
	rm -f figure/*
	rm -f result/*
	

.created-dirs:
	mkdir -p figure
	mkdir -p data
	mkdir -p result

data/processed_tweets.csv: Mental-Health-Twitter.csv preprocess.R
	Rscript preprocess.R
	
figure/density.png: stat.R data/processed_tweets.csv
	Rscript stat.R
	
figure/negative.html figure/positive.html figure/negative.png figure/positive.png: eda.R data/processed_tweets.csv
	Rscript eda.R

report.pdf: figure/negative.png figure/positive.png report.Rmd
	R -e "rmarkdown::render(\"report.Rmd\", output_format=\"pdf_document\")"
