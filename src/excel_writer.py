import os
import pandas as pd
from src.config import EXCEL_FILE, FIELDNAMES

def write_to_excel(rows):
    """Append rows to Excel file."""
    if os.path.exists(EXCEL_FILE):
        df_existing = pd.read_excel(EXCEL_FILE)
    else:
        df_existing = pd.DataFrame(columns=FIELDNAMES)

    df_new = pd.DataFrame(rows, columns=FIELDNAMES)
    df_all = pd.concat([df_existing, df_new], ignore_index=True)
    df_all.to_excel(EXCEL_FILE, index=False)

write_csv = write_to_excel  # alias for consistency
