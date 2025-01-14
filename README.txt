Step 1:
Install the dependencies
pip install -r requirements.txt

Step 2: run the following Commands
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate

Step 3:
Ensure that XAMPP is installed and the MySQL service is running.

Step 4:
Import the SQL scripts into your MySQL database.
The SQL scripts are located in the `BACKEND` folder:
- `penpaldb.sql`
- `penpaldbaccount.sql [with accounts]`

Step 5:
Run the penpalmain.py application
python penpalmain.py

Note: The `penpalmain.py` script will automatically start the server (`server.py`) before launching the main application.