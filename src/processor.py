import os
import shutil
import json
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.ai_client import call_gpt
from src.config import SUCCESS_DIR, ERROR_DIR, NOT_PROCESS_DIR
from src.utils import log_error, move_to_error
from src.excel_writer import write_csv

def process_single_image(filepath):
    filename = os.path.basename(filepath)
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🔄 Processing {filename}...")

    output = call_gpt(filepath)
    if isinstance(output, bytes):
        output = output.decode("utf-8", errors="replace")

    row = {
        "Image Filename": filename,
        "Description": "",
        "Full AI Output": output,
        "Created At": created_at
    }

    if output.startswith("ERROR:"):
        log_error(filename, "API Error", output)
        move_to_error(filepath, filename)
        print(f"❌ Error on {filename}, moved to error/")
        return None

    try:
        parsed = json.loads(output)
        row["Description"] = parsed.get("Description", "")
        shutil.move(filepath, os.path.join(SUCCESS_DIR, filename))
        print(f"✅ Success: {filename}")
        return row
    except Exception as e:
        log_error(filename, "Parse Error", output)
        move_to_error(filepath, filename)
        print(f"❌ Parse error on {filename}, moved to error/")
        return None

def process_images(folder, workers=3):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    rows = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(process_single_image, f): f for f in files}
        for future in as_completed(futures):
            result = future.result()
            if result:
                rows.append(result)
    if rows:
        write_csv(rows)

def show_summary():
    not_p = len(os.listdir(NOT_PROCESS_DIR))
    succ = len(os.listdir(SUCCESS_DIR))
    err = len(os.listdir(ERROR_DIR))
    print("\n📊 Status Summary")
    print(f"   🕒 Not Processed: {not_p}")
    print(f"   ✅ Success:       {succ}")
    print(f"   ❌ Errors:        {err}")
    return not_p, err
