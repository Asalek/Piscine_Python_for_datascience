import pandas as pd


def load(path: str) -> list:
    '''
        Load a CSV file, print it's shape and return it transposed
        path: str Path to CSV File
        return : File DataFrame
    '''
    df = None
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
    except Exception as e:
        print("Exception caught : \n", e)
        return None
    return df.transpose() if df is not None else None
