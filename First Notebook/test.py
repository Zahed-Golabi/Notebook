import sys
import os

if len(sys.argv) > 1:
    folder = sys.argv[1]
    
files = os.listdir(folder)
identifirs = [id(file.split(".")[0]) for file in files])
ids = sorted(set(identifirs))
