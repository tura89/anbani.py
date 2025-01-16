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
    matches = re.findall(r'([ა-ჿ]+\.(?:[ა-ჿ]+\.)*)', text)
    for match in matches:
       text = re.sub(match, expand(match), text)
    return text


def contract_text(text):
    for key in emap.keys():
        text = re.sub(key, emap[key], text)
    return text