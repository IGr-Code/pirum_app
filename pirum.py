# The goal of pirum app is quick and useful use of different needs for CTF or something else
# pirum.py

import argparse
from functions import caesar, meta_data



def main():
    parser = argparse.ArgumentParser(description='A simple program that does something.')
    parser.add_argument('-ceasar', action='store_true', help='Show tutorial on how to use this program')
    parser.add_argument('-metadata', action='store_true', help='Show tutorial on how to use this program')
  
    
    args = parser.parse_args()
    
    if args.ceasar:
        caesar()
    elif args.metadata:
        meta_data()
    else:
        print("Hello, Pirum!")

if __name__ == "__main__":
    main()

