pipenv install nltk --skip-lock 
python -m spacy download en_core_web_lg

if you face issue with python certificate on MAC, e.g.
[nltk_data] Error loading Punkt: <urlopen error [SSL:
[nltk_data] CERTIFICATE_VERIFY_FAILED] certificate verify failed
then run /Applications/Python\ 3.8/Install\ Certificates.command 


For preparing sentence generation endpoint, 
download the following files from gdrive foxino-app/data
- open-subtitles-en.txt
- sentence_index.json
- sentence_grammar_index.json
- word_index.faiss
- vocabulary.csv
- oxford3000.txt

and store them into data folder

To produce `sentence_grammar_index.json` run:
`python runner.py --index_grammar`

To produce `sentence_index.json` run:
`python runner.py --index_sents`

Macbook M1 sillicon - to avoid problem with installation of sentencepiece:
brew install cmake
brew install pkg-config
pip3 install sentencepiece

issue with installing tokenizers
ERROR: Could not build wheels for tokenizers, which is required to install pyproject.toml-based projects
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

