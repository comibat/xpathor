#!/usr/bin/python3

import os, sys

def usage():
    print ("""
Script used for extracting parts of html using xpath.

Usage: 
\tTo parse a file:
\t\t{} <html_file_path:string> <xpath:string> [<count:int>]
\tor to parse a stream:
\t\t{} - <xpath:string> [<count:int>]


<html_file_path>\tpath to the filename containing html content to be parsed
<xpath>\t\t\txpath selector. If selector contains quotes, then enclose xpath string into single quotes or whatever works.
<count>\t\t\toptions. How many results you want to print out. After <count> results, script exits.

Example:

To extract only Plugin Output from Nesses scan results in html file, use this xpath:
//div[contains(@class,"section-wrapper")]/div[contains(@class,"details-header")][last()]/following-sibling::div[2]/text()
    """.format(sys.argv[0],sys.argv[0]))
    exit()

def main():
    if len(sys.argv) < 3:
        usage()
    filename = sys.argv[1]
    xpath = sys.argv[2]
    try:
        from scrapy.selector import Selector
        from scrapy.http import TextResponse
    except:
        print("You need to install scrapy to make this work. Try: pip install scrapy")
        exit()
    if filename != '-':
        with open(filename, "r") as html_content:
            body = html_content.read()
    else:
        body = ''
        for line in sys.stdin:
            body += line
    results = Selector(text=body).xpath(xpath).getall()
    try:
        count = int(sys.argv[3])
    except:
        count = len(results)
    for result in results:
        count -= 1
        if count < 1:
            exit()
        print (result.strip())

if __name__ == "__main__":
    main()