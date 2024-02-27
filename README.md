# DATA ENGINEERING PROJECT 🖥️
Guided By: [Josh Dev](https://www.facebook.com/profile.php?id=100087019650476)<br>

## Prerequisites in this Project
- Download and Install [Python](https://www.python.org/downloads/)
- Download and Install [Git](https://git-scm.com/downloads)
- Download and Install [Postgresql](https://www.postgresql.org/download/)
- Download and Install [SQL Server 2022 Developer Edition](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- Download and Install [Visual Studio](https://visualstudio.microsoft.com/downloads/)
- Download and Install [PowerBI Desktop](https://powerbi.microsoft.com/en-us/downloads/) or in Microsoft Store 

## A. Connecting Local and Remote Repositories
### In your Local Machine
1. Create a folder in your local machine 
```bash
mkdir <folder_name>
```
2. Change directory to the created folder
```bash
cd <folder_name>
```
3. Initialize git
```bash
git init .
```
If you don't have git yet, you can download [here](https://github.com/ninjhaw/DE_Project?tab=readme-ov-file#prerequisites-in-this-project)  
4. Now you can create some files inside your folder. For example, README.md and put some text in it.  
![README.md](/images/create_readme.png)  <br>
5. Add file to the staging area by typing the command in the VSCode terminal:
```bash
git add README.md
```
Note: You can specify a file to add. However, you can use `.` to add all files in the folder.  
6. Commit the changes you've made by typing the command in the VSCode terminal:  
```bash
git commit -m "Your commit message here"
```
7. Push file to git
```bash
git push
```
### In Github repository
1. Go to [github](https://github.com)
2. Navigate to the top right corner, click `+` and choose `New Repository`
![New_repo](images/new_repository.png)  
3. Put a repository name
4. Select Public and Create repository
5. Generate your SSH Key [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?fbclid=IwAR2z7JJtyg304j8Awvd6i60FIaopo7tuQsqXHMbziOMYfZwmIDexVZe_Y8k)  
6. After generating the ssh key, go back to terminal and copy the first line of code below:
![remote_add](images/push_remote.png)  
7. Create branch main, copy the second line of code
8. Finally, push the changes to main branch

## Success! You push an existing repository to Github
- For Git Cheat Sheet, you can view [here](cheat_sheet/git_commands.md)  

## B. Setting Up Virtual Environment in Python
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

    ```bash
    env\Scripts\activate.bat
    ```
    b. On Windows PowerShell:  

    ```bash
    env\Scripts\Activate.ps1
    ```
    c. On Linux/Unix:  

    ```bash
    source env/bin/activate
    ```

4. Observe that the environment name (<your_environment_name>) appears on the left side before the command prompt.
5. You can now install packages listed in your requirements.txt file. 

    ```bash
    pip install -r requirements.txt
    ```
## Uploading Files from Web to FTP Server
1. Download and Install WSL(Windows for Subsytem for Linux)
    To see Linux distributions:
    ```bash
    wsl --list -o
    ```
    To install wsl:
    ```bash
    wsl --install -d Ubuntu
    ```

    Note: Ubuntu is the default distro when not specified

2. Download FTP Server(vsftpd) in wsl
    ```bash
    sudo apt install vsftpd
    ```
    or
    ```bash
    sudo apt install vsftpd -y
    ```
3. (Optional) Backup vsftpd.conf
    Though this is optional, it is a good practice to backup configuration files when trying to modify it for recovery.

    a. Navigate to vsftpd.conf
    ```bash
    ls /etc/
    ```
    You will see the files inside /etc/ folder including the vsftpd.conf. Now, it's time to back it up
    b. Backup vsftpd.conf
    ```bash
    cp /etc/vsftpd.conf /etc/vsftpd.conf_backup
    ```
    Use `cp` command to copy and paste it in same directory
    `cp <source> <destination>`

    You must have administrative priveleges in order to do this.
4. Modify vsftpd.conf
    In this part we will modify vsftpd.conf using nano
    Uncomment or add this line in vsftpd.conf:
    ```bash
    local_enable=YES
    write_enable=YES
    chroot_local_user=YES
    chroot_list_enable=YES
    chroot_list_file=/etc/vsftpd.chroot_list # or just uncomment
    ssl_enable=YES
    require_ssl_reuse=NO # add to the bottom of the file
    ```
5. Restarting and Checking vsftpd status
    a. vsftpd status
    ```bash
    sudo systemctl status vsftpd
    ```
    b. restart vsftpd service
    ```bash
    sudo systemctl restart vsftpd
    ```
    Note: after some or any changes in the conf, you must restart the service or else it won't work.
6. Creating an FTP User
    ```bash
    sudo adduser <username>
    ```
    a. Create directory for ftp user
    ```bash
    mkdir /home/ftpuser/ftp
    ```
    b. Change the access/ownership of the directory
    ```bash
    chown nobody:nogroup /home/ftpuser/ftp
    ```
    ```bash
    chmod a-w /home/ftpuser/ftp
    ```
    c. Create also a file for chroot_list
    ```bash
    echo "ftpuser" | sudo tee -a /etc/vsftpd.chroot_list
    ```




### Join our community: <br> 
Discord: [Data Engineering Pilipinas](https://discord.gg/H8fuv5DF),
         [DataCamp](https://discord.gg/UUWAEQQ6)<br>
FB Group: [Data Engineering Pilipinas](https://www.facebook.com/groups/dataengineeringpilipinas/)<br>
You may also visit Data Engineering Website [here](https://dataengineering.ph/)