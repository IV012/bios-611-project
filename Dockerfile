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


RUN apt-get update -qq && apt-get install -qy \
    ca-certificates \
    bzip2 \
    curl \
    libfontconfig \
    --no-install-recommends \
    && curl -SL https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 > phantom.tar.bz2 \
    && bzip2 -d ./phantom.tar.bz2 \
    && tar -xvf ./phantom.tar -C /usr/local/ --strip-components=1 \
    && rm phantom.tar \
    && apt-get -qy remove bzip2 curl \
    && rm -rf /var/lib/apt/lists/*
