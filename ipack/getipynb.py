import json

def convert(filename):
    file = open(filename, "r")
    lines = file.readlines()
    ipynb = {
    "cells" : [
        {
            "cell_type" : "code",
            "metadata" : {},
            "outputs" : [],
            "source" : lines
        }
    ],
    "metadata" : {
        "kernelspec" : {
            "display_name" : "Python 3",
            "language" : "python",
            "name" : "python3"
        },
        "language_info" : {
            "codemirror_mode" : {
                "name" : "ipython",
                "version" : 3
            },
            "file_extension" : ".py",
            "mimetype" : "text/x-python",
            "name" : "python",
            "nbconvert_exporter" : "python",
            "pygments_lexer" : "ipython3",
            "version" : "3.10.0"
        }
    },
    "nbformat" : 4,
    "nbformat_minor" : 5
}

    json_obj = json.dumps(ipynb)

    with open('jupnote.ipynb', 'w') as output:
        output.write(json_obj)


    
