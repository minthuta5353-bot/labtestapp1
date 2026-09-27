import pandas as pd

def process_csv():
    # CSV ဖိုင်ကို Read လုပ်ခြင်း (Load)
    file_path = 'data.csv'
    print(f"Reading CSV file from {file_path}...")
    
    df = pd.read_csv(file_path)
    
    # ဖတ်ရလာတဲ့ Data များကို Display လုပ်ပြခြင်း
    print("\n--- CSV Data Content ---")
    print(df)
    
    # ဥပမာ - ဒေတာအသစ်တစ်ခုကို ပြန်လည် Save / Load လုပ်ခြင်း
    output_path = 'output_data.csv'
    df.to_csv(output_path, index=False)
    print(f"\nSuccessfully processed and loaded data to {output_path}")

if __name__ == "__main__":
    process_csv()
