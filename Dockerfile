FROM rocker/verse 
RUN wget https://deb.nodesource.com/setup_16.x 
RUN bash setup_16.x
RUN apt update && apt-get install -y nodejs
RUN apt update && apt-get install -y emacs openssh-server python3-pip
RUN pip3 install --pre --user hy
RUN pip3 install beautifulsoup4 theano tensorflow keras sklearn pandas numpy pandasql 
RUN ssh-keygen -A
RUN mkdir -p /run/sshd
RUN sudo usermod -aG sudo rstudio
RUN R -e "devtools::install_github('gastonstat/arcdiagram')"
RUN R -e "install.packages(c('matlab','Rtsne'));"
RUN apt update && DEBIAN_FRONTEND=noninteractive apt-get install -y xfce4-terminal gnome-terminal dh-autoreconf libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev asciidoc xmlto docbook2x
RUN git clone git://git.kernel.org/pub/scm/git/git.git
WORKDIR /git
RUN make configure &&\
 ./configure --prefix=/usr &&\
 make all doc info &&\
 make install install-doc install-html install-info
WORKDIR /
RUN Rscript --no-restore --no-save -e "update.packages(ask = FALSE)"
RUN apt update -y && apt install -y python3-pip
RUN R -e "install.packages(\"tidyverse\")"
RUN R -e "install.packages(\"tidytext\")"
RUN R -e "install.packages(\"RColorBrewer\")"
RUN R -e "install.packages(\"wordcloud2\")"
RUN R -e "install.packages(\"stopwords\")"
RUN R -e "install.packages(\"webshot\")"
RUN R -e "install.packages(\"htmlwidgets\")"
RUN R -e "webshot::install_phantomjs()"
RUN pip3 install numpy pandas sklearn
RUN pip3 install torch torchtext nltk matplotlib
RUN apt update -y && apt install -y python3-pip
RUN pip3 install jupyter jupyterlab
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
