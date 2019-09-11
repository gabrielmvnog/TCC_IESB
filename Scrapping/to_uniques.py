import pandas as pd
import os
import shutil
from os.path import join

PATH_FROM = 'dataset_from_twitter'
PATH_TO = 'dataset_uniques'

def clean_dataset(df):

    # Remoção de RT
    df = df.str.replace(r"^RT", '')

    # Remoção de referências
    df = df.str.replace(r"(@[\w]*:?)", '')

    # Remoção de hashtags
    df = df.str.replace(r"(#[\w]*)", '')

    # Remoção de links
    df = df.str.replace(r"https:\/\/t.co\/[\w]*", '')

    # Strip
    df = df.str.strip()

    # Remove /n
    df = df.str.replace(r"\n", ' ')

    return df


if __name__ == '__main__':

    if os.path.exists(PATH_TO):
        shutil.rmtree(PATH_TO)

    os.makedirs(PATH_TO)

    for csv  in os.listdir(PATH_FROM):
        print(f'Reading... {csv}')

        CSV_PATH_FROM = join(PATH_FROM, csv)
        CSV_PATH_TO = join(PATH_TO, csv)

        df = pd.read_csv(CSV_PATH_FROM, header=None)
        df = df.apply(clean_dataset)
        df_unique = df.apply(pd.unique)

        df_unique.to_csv(CSV_PATH_TO, header=None)        
