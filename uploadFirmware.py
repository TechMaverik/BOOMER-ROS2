import os
import subprocess

BOOMER_PORT = "COM6"
folder_path = "Micropython"
all_items = os.listdir(folder_path)
files_to_upload = [f for f in all_items if os.path.isfile(os.path.join(folder_path, f))]


def upload_files(port, files):
    for file in files:
        print(f"Uploading {file} to BOOMER...")
        try:
            subprocess.run(
                [
                    "mpremote",
                    "connect",
                    port,
                    "fs",
                    "cp",
                    "micropython/" + file,
                    f":{file}",
                ],
                check=True,
            )
            print(f"✅ {file} uploaded successfully.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to upload {file}: {e}")


if __name__ == "__main__":
    upload_files(BOOMER_PORT, files_to_upload)
