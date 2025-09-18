from backtestingScripts.getFileLocation import getFileLocation
import inquirer
import os
import pandas


def readDataFolder(data_location_name):
    parent_data_folder_location = getFileLocation('backtestingData')
    target_dir = os.path.join(parent_data_folder_location,data_location_name)
    
    

def getDataFolderList():
    parent_data_folder_location = getFileLocation('backtestingData')
    dir_contents = os.listdir(parent_data_folder_location)
    return dir_contents

def getDfArr():
    folder_choice = [inquirer.List('selection',
                                    message='Select A Folder/File to use for the Backtesting Data:',
                                    choices=getDataFolderList())]

    folder_to_use = inquirer.prompt(folder_choice)['selection']

    split = folder_to_use.split('.')
    if len(split) == 1: #if there is a folder of backtesting csv data rather than a single instance
        print('reading data from a folder')
        df_arr = readDataFolder(split[0])

    else: #if the selection is a single csv file with backtesting data
        print('reading data from a single folder')

if __name__ == '__main__':
    getDfArr()
