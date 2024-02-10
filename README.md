# DATA ENGINEERING PROJECT

## Setting Up Virtual Environment in Python
1. Open the repository in Visual Studio Code (VSCode).<br>
    Ensure that you are in the correct directory where your repository is located.

2. Press Ctrl + ~ to open the terminal.  <br>
    Enter the command:  <br>
        ```python -m venv <environment_name>```  
    Replace ```<environment_name>``` with the name you want.  
    Take note that a file will be added with the name of the environment you created.<br>

3. Activate the virtual environment: <br>
    a. On Windows command prompt:  <br>
        ```.\<your_environment_name>\Scripts\activate.bat```<br>
    b. On Windows PowerShell:  <br>
        ```.\<your_environment_name>\Scripts\Activate.ps1```<br>
    c. On Linux/Unix:  <br>
        ```source <your_environment_name>/bin/activate```<br>

4. Observe that the environment name (<your_environment_name>) appears on the left side before the command prompt.
5. You can now install packages listed in your requirements.txt file.