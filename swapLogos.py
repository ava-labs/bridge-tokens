#!/usr/bin/python3

import csv
import json
import pandas
import shutil
import os
from git import Repo

OLD_TOKEN_MAP = 'current_mapping_libre.csv'
TOKEN_MAP = 'penultimate.csv'
LOGOS_IN_DIR = 'Logos'
LOGOS_OUT_DIR = 'avalanche-tokens'
#HOSTED_URL = 'https://raw.githubusercontent.com/ava-labs/bridge-tokens/main/'

def read_logos():
    token_map = pandas.read_csv(TOKEN_MAP)
    #print(token_map.loc[2:5, ["Avalanche Token Address", "Ethereum Token Address"]])
    return token_map

def read_old_logos():
    token_map = pandas.read_csv(OLD_TOKEN_MAP)
    #print(token_map.loc[2:5, ["Avalanche Token Address", "Ethereum Token Address"]])
    return token_map

def swap_logos(token_map, old_token_map):
    for _, row in token_map.iterrows():
        old_row = old_token_map[old_token_map["Avalanche Token Symbol"] == row['Avalanche Token Symbol']]
        if len(old_row.index) == 0:
            print("No token for ", row['Avalanche Token Symbol'])
        elif len(old_row.index) > 1:
            print("Collision for ", row['Avalanche Token Symbol'])
        else:
            ava_address = row['Avalanche Token Address']
            old_ava_address = old_row.iloc[0]['Avalanche Token Address']

            old_out_dir = LOGOS_OUT_DIR + '/' + old_ava_address
            out_dir = LOGOS_OUT_DIR + '/' + ava_address

            #old_logo = old_out_dir + '/logo.png'
            #new_logo = out_dir + '/logo.png'

            #os.mkdir(out_dir)

            try:
                shutil.move(old_out_dir, out_dir)
            except:
                print("Couldn't rename ", old_out_dir, out_dir)

def main():
    token_map = read_logos()
    old_token_map = read_old_logos()
    swap_logos(token_map, old_token_map)

if __name__ == '__main__':
    main()