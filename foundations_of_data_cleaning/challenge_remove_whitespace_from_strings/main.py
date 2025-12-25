import pandas as pd

def strip_whitespace(df):
    cleaned_df=df.copy()
    for col in cleaned_df.select_dtypes(include="object"):
        cleaned_df[col] = cleaned_df[col].str.strip()
    return cleaned_df

data = {
    "Fruit": [" apple", "banana ", "  cherry ", "date"],
    "Color": [" red", "yellow ", " red ", "brown"],
    "Count": [10, 5, 7, 3]
}

df = pd.DataFrame(data)
cleaned_df = strip_whitespace(df)
print(cleaned_df)
