import os

def create_directories(base_path):
    directories = [
        "tree/c/other_courses/cpp",
        "tree/c/other_courses/python",
        "tree/cpp/other_courses/c",
        "tree/cpp/other_courses/python",
        "tree/python",
    ]
    
    for directory in directories:
        path = os.path.join(base_path, directory)
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {path}")

if __name__ == "__main__":
    base_path = "."  # Base path where the directories will be created
    create_directories(base_path)
