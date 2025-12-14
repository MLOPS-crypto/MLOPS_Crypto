import io
import pandas as pd
from google.cloud import storage

BUCKET_NAME = "bucket-crypto-data"
PAIR_SLUG = "BTC_USDT"

PRICES_PATH = f"monitoring/{PAIR_SLUG}_prices.parquet"
EVAL_PATH = f"monitoring/{PAIR_SLUG}_eval.parquet"

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

def load_parquet(path):
    blob = bucket.blob(path)
    buf = io.BytesIO()
    blob.download_to_file(buf)
    buf.seek(0)
    return pd.read_parquet(buf)

# --- Load data ---
df_prices = load_parquet(PRICES_PATH)
df_eval = load_parquet(EVAL_PATH)

# --- Display ---
print("\n=== PRICES (OHLCV) ===")
print(df_prices.head())
print("\nColumns:", df_prices.columns.tolist())

print("\n=== EVAL (predictions vs reality) ===")
print(df_eval.head())
print("\nColumns:", df_eval.columns.tolist())

print("\n=== Last 5 eval rows ===")
print(df_eval.tail())
