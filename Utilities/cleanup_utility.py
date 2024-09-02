import os
import glob

def delete_files_in_directory(directory):
    if os.path.exists(directory):
        files = glob.glob(os.path.join(directory, '*'))
        for f in files:
            try:
                os.remove(f)
                print(f"Deleted file: {f}")
            except Exception as e:
                print(f"Error deleting file {f}: {str(e)}")
    else:
        print(f"Directory {directory} does not exist.")

def cleanup_logs():
    logs_directory = os.path.join(os.getcwd(), 'selenium_logs')
    print("Cleaning up logs...")
    delete_files_in_directory(logs_directory)
    print("Logs cleanup complete.")

def cleanup_screenshots():
    screenshots_directory = os.path.join(os.getcwd(), 'screenshots')
    print("Cleaning up screenshots...")
    delete_files_in_directory(screenshots_directory)
    print("Screenshots cleanup complete.")