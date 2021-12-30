![image info](./pictures/getipynb_banner.png)
# getipynb - A python module to convert .py to .ipynb

getipynb is a python module which aims to solve the very common problem of opening .py files in jupyter notebook in an executable form. It ends the problem of copy and pasting the whole of your .py code into the jupyter notebooks.

# Installation

## Dependencies

Python (>= v3.7)

## User Installation

The easiest way to install is by using `pip`:

`pip install getipynb`

## Usage

To use it, open the python terminal and type:

`from ipack import getipynb`

And then:

`getipynb.convert(file_address)`

It will create the jupyter equivalent notebook in the same directory. 
