import pandas as pd
import os
import re
from pathlib import Path

module_path = Path(__file__).parent.parent.absolute()

cdf = pd.read_csv(os.path.join(module_path, "data/georgian_contractions.csv"))
cmap = cdf.set_index('CONTRACTION')[['EXPANSION']].to_dict('dict')['EXPANSION']
emap = cdf.set_index('EXPANSION')[['CONTRACTION']].to_dict('dict')['CONTRACTION']

def expand(word):
    # Just a wrapper around contractions map
    if word in cmap:
        return cmap[word]

    return word


def expand_text(text):
    # Look up contractions sequentially and replace them with expansions
    while True:
        match = re.search(r'([ა-ჿ]+\.(?:[ა-ჿ]+\.)*)', text)
        if not bool(match):
            break

        expansion = expand(text[match.start():match.end()])
        text = text[:match.start()] + expansion + text[match.end():]

    return text


def contract_text(text):
    for key in emap.keys():
        text = re.sub(key, emap[key], text)
    return text