import os
import shutil
import base64
import mimetypes
from datetime import datetime
from src.config import ERROR_DIR, LOG_DIR

def encode_image(image_path):
    """Convert image to base64 data URI."""
    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type is None:
        mime_type = "image/png"
    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime_type};base64,{b64}"

def log_filename():
    return f"{LOG_DIR}/error-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"

def log_error(filename, error_type, output):
    """Write error details to a log file with timestamp."""
    if isinstance(output, bytes):
        output = output.decode("utf-8", errors="replace")
    with open(log_filename(), "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}] File: {filename}\n")
        f.write(f"Error Type: {error_type}\n")
        f.write(f"Output: {output}\n")
        f.write("="*60 + "\n")

def move_to_error(filepath, filename):
    shutil.move(filepath, os.path.join(ERROR_DIR, filename))

def main_menu():
    from src.processor import process_images, show_summary
    while True:
        not_p, err = show_summary()
        print("\nChoose an action:")
        print("1. Process remaining (not_process/)")
        print("2. Retry errors (error/)")
        print("3. Show summary only")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            if not_p > 0:
                process_images("images/not_process")
            else:
                print("🎉 No files left in not_process/")
        elif choice == "2":
            if err > 0:
                process_images("images/error")
            else:
                print("🎉 No files left in error/")
        elif choice == "3":
            continue
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice, try again.")
