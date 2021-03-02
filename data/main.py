from typing import Text, List, Tuple
import pandas as pd
import spacy
import nltk
import neuralcoref

nlp = spacy.load('en_core_web_lg')
neuralcoref.add_to_pipe(nlp)



def process_tokens(tokens: List[Text]):
    links: List[Tuple[Text, Text, Text]]
    for token in tokens:
        if "punct" in token.dep_:
            continue
        print(token)
        subj, obj, rel = '', '', ''


