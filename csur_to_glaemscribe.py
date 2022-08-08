import json

from pathlib import Path

import re

import argparse 


replace_dict_json = '''
{"\ue000": "tinco", "\ue001": "parma", "\ue002": "calma", "\ue003": "quesse", "\ue004": "ando", "\ue005": "umbar", "\ue006": "anga", "\ue007": "ungwe", "\ue008": "sule", "\ue009": "formen", "\ue00a": "harma", "\ue00b": "hwesta", "\ue00c": "anto", "\ue00d": "ampa", "\ue00e": "anca", "\ue00f": "unque", "\ue010": "numen", "\ue011": "malta", "\ue012": "noldo", "\ue013": "nwalme", "\ue014": "ore", "\ue015": "vala", "\ue016": "anna", "\ue017": "vilya", "\ue020": "romen", "\ue021": "arda", "\ue022": "lambe", "\ue023": "alda", "\ue024": "silme", "\ue026": "esse", "\ue025": "silmen", "\ue027": "essen", "\ue028": "hyarmen", "\ue029": "hwestas", "\ue02a": "yanta", "\ue02b": "ure", "\ue02e": "telco", "\ue02c": "ara", "\ue018": "xtinco", "\ue019": "xparma", "\ue01a": "xcalma", "\ue01b": "xquesse", "\ue01c": "xando", "\ue01d": "xumbar", "\ue01e": "xanga", "\ue01f": "xungwe", "\ue02d": "halla", "\ue03d": "vaia", "\ue032": "osse", "\ue03c": "hwl", "\ue03a": "mh", "\ue03b": "mhb", "\ue039": "hwbom", "\ue031": "wbom", "\ue051": "geminate", "\ue050": "nasal", "\ue052": "labial", "\ue043": "palatal", "\ue059": "sarince", "\ue058": "arrince", "\ue070": "0", "\ue071": "1", "\ue072": "2", "\ue073": "3", "\ue074": "4", "\ue075": "5", "\ue076": "6", "\ue077": "7", "\ue078": "8", "\ue079": "9", "\ue07a": "10", "\ue07b": "11", "\ue07c": "12", "\ue07d": "lsd", "\ue057": "thinnas", "\u2e31": ",", ":": ".", "\u205d": "...", "\u2e2c": "::", "\u2058": "....", "\u2e2d": ".....", "\ue066": "?", "\ue065": "!", "\ue068": "~", "-": "~", "\ue06a": "\u00ab", "\ue06b": "\u00bb", "\ue067": "$", "\ue069": "\u2265", "\ue040": "a", "\ue046": "e", "\ue044": "i", "\ue04a": "o", "\ue04c": "u", "\ue056": "arev", "\ue054": "egrave", "\ue055": "acirc", "\ue053": "breve", "\ue041": "a<", "\ue047": "e<", "\ue045": "i<", "\ue04b": "o<", "\ue04d": "u<", "\ue049": "ee<"}
'''

replace_dict = json.loads(replace_dict_json)


def transcode(input_file, output_file):
    
    if output_file == "":
        output_file = Path(input_file).stem + '_glaemscribe.txt'
    
    with open(input_file, 'r', encoding="utf-8") as file:
        csur_text = file.read()
        
        csur_text = ''.join((filter(lambda x: x in list(replace_dict.keys()) + [' ', '\n'], 
                                                    csur_text)))
        
        csur_text_split = re.split(r'(\s+)', csur_text)
        
        glaem_text = ""

        for csur_words_num, csur_word in enumerate(csur_text_split):
            if csur_words_num %2 == 0:
                
                glaem_word = r"{{"
                
                for csur_letter in csur_word :
                    glaem_word += replace_dict[csur_letter] + r"|"
                
                glaem_word += r"}}"
            
            else:
                glaem_word = csur_word
        
            glaem_text += glaem_word
                
    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(glaem_text)
    
    
parser = argparse.ArgumentParser(description="Convert Tengwar with CSUR encoding to Glǽmscribe's format.")
parser.add_argument("input", help="Input file, with CSUR encoding.")
parser.add_argument("output", nargs = '?', help="Output file, to be used in Glǽmscribe.", default = "")

args = parser.parse_args()

transcode(args.input, args.output)
print("Done!")