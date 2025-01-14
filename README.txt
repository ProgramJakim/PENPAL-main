Step 1:
Install the dependencies
pip install -r requirements.txt

Step 2: run the following Commands
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate

Step 3:
Run the penpalmain.py application
python penpalmain.py

Note: The `penpalmain.py` script will automatically start the server (`server.py`) before launching the main application.