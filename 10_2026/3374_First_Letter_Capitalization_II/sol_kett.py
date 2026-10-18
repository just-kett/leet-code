import pandas as pd
import re

def convert_text(text):
    def convert_word(match):
        word = match.group()

        if not word[0].isalpha():
            return word

        if '-' in word and '--' not in word and word.replace('-', '').isalnum():
            parts = word.split('-')
            return '-'.join(
                part.capitalize() if part else part
                for part in parts
            )

        return word.capitalize()

    return re.sub(r'\S+', convert_word, text)

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    result = user_content.copy()

    result['original_text'] = result['content_text']
    result['converted_text'] = result['content_text'].apply(convert_text)

    return result[['content_id', 'original_text', 'converted_text']]