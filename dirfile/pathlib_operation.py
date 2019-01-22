from pathlib import Path
import os

path = Path(os.getcwd())
npath = path.joinpath('desi')
print(npath.parts)
print(npath.name)

# select path
for idx, dirz in enumerate(path.iterdir()):
    print(idx, dirz)

# select path with all file .py
for idx, file in enumerate(path.glob('*.py')):
    print(file)

# open sintaks
pp = list(path.glob('*.py'))
for line in pp[0].open():
    print(line)