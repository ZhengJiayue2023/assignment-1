import pandas as pd

def clean(input1, input2):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    df = df.dropna()
    df = df.drop(df[df['job'].str.contains['insurance', 'Insurance']])
    return df

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='contact_info_file')
    parser.add_argument('input2', help='other_info_file')
    parser.add_argument('output', help='Cleaned data file')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)
