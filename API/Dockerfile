FROM python:3.8-buster

# copy directories
ADD alternative /alternative/
ADD common /common/
ADD endpoints /endpoints/
ADD mistakes /mistakes/
ADD models /models/
ADD parser /parser/
ADD scrapers /scrapers/
ADD similarity /similarity/


# copy files
ADD config.py /
ADD run_gen.py /
ADD run_summ.py /
ADD run_test.py /
ADD runner.py /
ADD main.py /

# ADD data/open-subtitles-en.txt /data/open-subtitles-en.txt
# ADD data/oxford3000.txt /data/oxford3000.txt
# ADD data/profanity.txt /data/profanity.txt
# ADD data/vocabulary.csv /data/vocabulary.csv

ADD requirements.txt /

# install packages
RUN pip install -r /requirements.txt
RUN pip freeze
RUN python -m spacy download en_core_web_lg
RUN python -m nltk.downloader punkt


CMD python main.py
