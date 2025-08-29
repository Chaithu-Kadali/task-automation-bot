import pandas as pd

def clean_excel(input_file, output_file):
    df = pd.read_excel(input_file)

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date columns
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], errors="coerce")

    df.to_excel(output_file, index=False)
    print(f"✅ Cleaned data saved to {output_file}")

if __name__ == "__main__":
    print("=== Task Automation Bot ===")
    input_file = "input.xlsx"
    output_file = "output_cleaned.xlsx"
    clean_excel(input_file, output_file)
