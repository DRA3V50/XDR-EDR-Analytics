import os

kql_folder = "./detections/"

def validate_kql(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    if "-enc" in content or "DeviceProcessEvents" in content:
        print(f"{file_path}: Looks valid")
    else:
        print(f"{file_path}: Needs review")

for file in os.listdir(kql_folder):
    if file.endswith(".kql"):
        validate_kql(os.path.join(kql_folder, file))
