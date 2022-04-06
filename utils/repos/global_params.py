import re
import os
import datetime as dt


common_patterns = {
    'pattern_1': '.',
    'pattern_2': ' ',
    'pattern_3': '',
    'pattern_4': '\'',
    'pattern_5': 'and'
}

html_patterns = {
    'pattern_1': r'<.*?>',
    'pattern_2': r'(&nbsp;|&ensp;|&emsp;|&gt;)',
    'pattern_3': r'&amp;'
}

# spacy_model = "en_core_web_lg"
# spacy_NER_tags = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'ORDINAL']

postal_code_pattern = r'(?<=[\w\s])\d{6}(?=\.?\n)'

encode_decode_vars = {
    "encode_type": 'ascii',
    "error_type": 'replace',
    "decode_type": 'ascii',
    "pattern_1": r'\?+',
    "pattern_2": r'\s+',
}

bullet_pattern = r'^\*|^-'

url_pattern = r'((http|https):/+\S+)|(www\.\S+\.\S{2,9})'

hexcode_pattern = r'[^\x00-\x7f]'

escape_seq_pattern = r'\\[a-z]'

contact_numb_pattern = r'\+?\d?[\s-]?\(?\d{3}\)?[\.\s-]?\d{3}[\.\s-]?\d{4}'

email_data_pattern = r'\S*@\S*\s?'

socialmedia_pattern = r'\s?(@|#)\S+'

contraction_patterns = {
    'pattern_1': r'n\'t',
    'pattern_2': r'\'re',
    'pattern_3': r'\'s',
    'pattern_4': r'\'d',
    'pattern_5': r'\'ll',
    'pattern_6': r'\'t',
    'pattern_7': r'\'ve',
    'pattern_8': r'\'m'
}

expanded_contractions = [' not', ' are', ' is',
                         ' would', ' will', ' not', ' have', ' am']

emojis = "["\
    u"\U0001F600-\U0001F64F"\
    u"\U0001F300-\U0001F5FF"\
    u"\U0001F680-\U0001F6FF"\
    u"\U0001F1E0-\U0001F1FF"\
    u"\U00002500-\U00002BEF"\
    u"\U00002702-\U000027B0"\
    u"\U00002702-\U000027B0"\
    u"\U000024C2-\U0001F251"\
    u"\U0001f926-\U0001f937"\
    u"\U00010000-\U0010ffff"\
    u"\u2640-\u2642"\
    u"\u2600-\u2B55"\
    u"\u200d"\
    u"\u23cf"\
    u"\u23e9"\
    u"\u231a"\
    u"\ufe0f"\
    u"\u3030"\
    "]+"

emoji_flag = re.UNICODE

emoji_rstring = r''

punct_patterns = {
    'pattern_1': r'(?<![\d\w])-(?![\d\w])',
    'pattern_2': r'-(?=\w)',
    'pattern_3': r'((?<!\d)/)',
    'pattern_4': r'(?<![\d\.,])\%',
    'pattern_5': r'\$(?!\d+)',
    'pattern_6': r'(?<![\w])\.|(?<![\w])\:',
    'pattern_7': r'\((?![\w])|(?<![\w])\)'
}

punct_list = [
    '!', '"', '#', '&', "'", '*', '+', ',',
    ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
]

extra_spaces = r'\s{2,}'

make_directory = {
    "dir_structure": None,
    "basefolder": "samples\\Logfiles",
    "file_start": "text_cleaner"
}

datetime_vars = {
    'now': dt.datetime.now(),
    'curr_year': dt.datetime.now().year,
    'curr_month': dt.datetime.now().strftime("%B"),
    'curr_day': dt.datetime.now().day,
    'curr_date': dt.datetime.now().date(),
    'curr_time': dt.datetime.now().strftime("%H-%M-%S")
}

curr_directory = os.getcwd()
