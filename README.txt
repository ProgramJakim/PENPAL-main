Step 1:
Install the dependencies
pip install -r requirements.txt

Step 2: run the following Commands
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate

Step 3:
Run the server
python BACKEND/server.py [for database mysql:xammp]

Note: The executable file only includes the main application (`penpalmain.py`). Ensure the server is running before starting the main application.

Step 4:
Run the penpalmain.py application
Double-click the `start_app.bat` file to start the main application.