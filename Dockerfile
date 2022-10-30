FROM rocker/verse 
RUN Rscript --no-restore --no-save -e "update.packages(ask = FALSE)"

RUN R -e "install.packages(\"tidyverse\")"
RUN R -e "install.packages(\"tidytext\")"
RUN R -e "install.packages(\"RColorBrewer\")"
RUN R -e "install.packages(\"wordcloud2\")"
RUN R -e "install.packages(\"stopwords\")"
RUN R -e "install.packages(\"webshot\")"
RUN R -e "install.packages(\"htmlwidgets\")"
RUN R -e "webshot::install_phantomjs()"