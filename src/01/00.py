#  Write a program that unzips one of your zip-files into another directory

from zipfile import ZipFile

with ZipFile('../../resources/files.zip') as zin:
    zin.extractall('../../playground/extracted-zip')
