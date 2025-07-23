python3 -m venv .venv  # Create a virtual environment named '.venv'
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
.venv\Scripts\activate  # Activate the virtual environment (Windows)
pip install -qqq pandas==1.5.3 matplotlib
python your_script_name.py # replace your_script_name.py with the actual name of your python file.
deactivate # Deactivate the virtual environment when finished
