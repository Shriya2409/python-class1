import os
from pathlib import Path
project_name = "src"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/input/data.csv",
    f"{project_name}/src/train.py",
    f"{project_name}/src/predict.py",
    f"{project_name}/src/model_selection.py",
    f"{project_name}/src/tune_model.py",
    f"{project_name}/src/utils.py",
    f"{project_name}/models/model1.pkl",
    f"{project_name}/models/model2.pkl",
    f"{project_name}/notebooks/exploration.ipynb",
    f"{project_name}/README.md",
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    