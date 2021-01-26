#!/usr/bin/python3

import csv
import json
import pandas

TOKEN_MAP = 'eth_token_mapping.csv'
LOGOS_DIR = 'Logos'
ETH_CONFIG = 'ethereum.config'
AVA_CONFIG = 'avalanche.config'

def read_logos():
    token_map = pandas.read_csv(TOKEN_MAP)
    #print(token_map.head())
    print(token_map.loc[2:5, ["Avalanche Token Address", "Ethereum Token Address"]])
    #with open(TOKEN_MAP) as csvfile:
    #    reader = csv.DictReader(csvfile)
    #    for row in reader:
    #        print(row['Ethereum Token Address'], row['Avalanche Token Address'])

def generateEthConfig():
    with open(TOKEN_MAP) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Ethereum Token Address'], row['Avalanche Token Address'])

def main():
    read_logos()

if __name__ == '__main__':
    main()