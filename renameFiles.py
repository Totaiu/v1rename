import os
import fnmatch

folderPath = r'' #путь к папке
seriesNumber = 1  #с какого числа начинаются серии
seriesFormat = '.mkv'
seriesFormatSearch = '*' + seriesFormat

subtitlesNumber = 1 # с какого числа начинаются субтитры
subtitleFormat = '.ass'
subtibleFormatSearch = '*' + subtitleFormat


for filename in os.listdir(folderPath):
    if fnmatch.fnmatch(filename, subtibleFormatSearch):
      os.rename(folderPath + '\\' + filename, folderPath + '\\' + str(subtitlesNumber) + subtitleFormat)
      subtitlesNumber +=1
    if fnmatch.fnmatch(filename, seriesFormatSearch):
      os.rename(folderPath + '\\' + filename, folderPath + '\\' + str(seriesNumber) + seriesFormat)
      seriesNumber +=1