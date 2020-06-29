try:
    from flask import Flask,request,render_template,g,send_from_directory
except:
    print("you need to run:\n\t'python -m pip install flask'")

try:
    from flask import Flask,request,render_template,g,send_from_directory
except:
    print("you need to run:\n\t'python -m pip install flask'")

try:
    import pandas as pd
except:
    print("you need to run:\n\t'python -m pip install pandas'")


import sqlite3

import os

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 


import subprocess
subprocess.Popen(["python.exe",os.path.join(os.path.dirname(__file__),"app.py")])
subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe","http://127.0.0.1:5000/"])


