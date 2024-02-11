# DATA ENGINEERING PROJECT

## Prerequisite in this Project
- Download and Install [Git](https://git-scm.com/downloads)
- Download and Install [Postgresql](https://www.postgresql.org/download/)
- Download and Install [SQL Server 2022 Developer Edition](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)



## A. Setting Up Virtual Environment in Python
1. Open the repository in Visual Studio Code (VSCode).<br>
    Ensure that you are in the correct directory where your repository is located.

2. Press Ctrl + ~ to open the terminal.  
    Enter the command:  

    ```bash
    python -m venv <environment_name>
    ```  

    Replace ```<environment_name>``` with the name you want. 
    Take note that a folder will be added with the name of the environment you created. 

3. Activate the virtual environment:  
    a. On Windows command prompt: 

    ```
    env\Scripts\activate.bat
    ```
    b. On Windows PowerShell:  

    ```
    env\Scripts\Activate.ps1
    ```
    c. On Linux/Unix:  

    ```
    source env/bin/activate
    ```

4. Observe that the environment name (<your_environment_name>) appears on the left side before the command prompt.
5. You can now install packages listed in your requirements.txt file. 

    ```bash
    pip install -r requirements.txt
    ```

    