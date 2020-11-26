import os
import fnmatch

folderPath = r'' #путь к папке
seriesNumber = 1  #с какого числа начинаются серии
subtitlesNumber = 1 # с какого числа начинаются субтитры

for filename in os.listdir(folderPath):
    if fnmatch.fnmatch(filename, '*.ass'):
      os.rename(folderPath + '\\' + filename, folderPath + '\\' + str(subtitlesNumber) + '.ass')
      subtitlesNumber +=1
    if fnmatch.fnmatch(filename, '*.mkv'):
      os.rename(folderPath + '\\' + filename, folderPath + '\\' + str(seriesNumber) + '.mkv')
      seriesNumber +=1