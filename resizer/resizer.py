from resizer_lib import open_file
from pdf2image import convert_from_path
import glob
import sys
import os
import tempfile
args = sys.argv

if len(args) < 2:
    print("Podaj nazwy plików")

files = glob.glob('./zadania/*')
for f in files:
    os.remove(f)

filenames = []

for arg in args[1:]:
    for filename in glob.glob(arg):
        name, extension = os.path.splitext(filename.lower())
        if extension in ['.jpg', '.png']:
            filenames.append(filename)
        if extension == '.pdf':
            pages = convert_from_path(filename, 100)
            for page in pages:
                ff = tempfile.TemporaryFile()
                filename = ff.name + '.png'
                ff.close()
                page.save(filename, 'png')
                filenames.append(filename)
                
try:
    os.makedirs('./zadania/')
except:
    pass

for filename in filenames:
    open_file(filename)

    