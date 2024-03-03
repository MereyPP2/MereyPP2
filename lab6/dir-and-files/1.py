import os
def files(path):
    d = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    f = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    print("Directories:")
    print(d)
    
    print("\nFiles:")
    print(f)
    
    print("\nAll Directories and Files:")
    print(os.listdir(path))

path = "C:"
files(path)