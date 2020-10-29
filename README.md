# xpathor

Script used for extracting parts of html using xpath.

## Usage: 
To parse a file:

`./xpathor.py <html_file_path:string> <xpath:string> [<count:int>]`

or to parse a stream:

`./xpathor.py - <xpath:string> [<count:int>]`

where

`<html_file_path>` - path to the filename containing html content to be parsed<br/>
`<xpath>` - xpath selector. If selector contains quotes, then enclose xpath string into single quotes or whatever works.<br/>
`<count>` options. How many results you want to print out. After `<count>` results, script exits.<br/>


## Example:

To extract only Plugin Output from Nesses scan results in html file, use this xpath:

`//div[contains(@class,"section-wrapper")]/div[contains(@class,"details-header")][last()]/following-sibling::div[2]/text()`
