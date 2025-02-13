import os 
from pathlib import Path

list_of_files=[
    "notebook/ml.ipynb",
    "requirements.txt"
    "app.py",
    "static/style.css",
    "templates/index.html",
    "data/raw.csv",

    "app.py"
    ""

    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


     
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  
    
    
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass  