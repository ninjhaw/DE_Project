## PART 1
1. Get the files from FTP Server to Local folder
2. Create FTP Task
    a. requires connection manager
    b. at the right side(Solution Explorer), right click Connection Managers -> New Connection Manager
    c. Look for FTP -> Add, there will be a pop up window for ftp connection manager editor
        Put the ff:
            i. Server Name or IP Address
            ii. Server port(Default is 21)
            iii. Username and password of ftp server configured in WSL
            iv. You can click `Test Connection` to test if you're connected to the ftp user, if not try to      identify your server name or ip address. Also the username and password must be correct
3. Modifying FTP Task Content
    a. Double-click FTP Task, pop up window will appear(FTP Task Editor)
    b. General > Select FTP Connection and select the FTP Connection Manager
    c. You can rename the the task. Just be descriptive
    d. File Transfer > Operation > Select Receive files(since this task is to download csv file from ftp server)
4. Creating Local Path Variable - for ExtractFolder
    a. Go to View > Other Windows > Variables
    b. Create variable by clicking the first icon.
    c. Set the name to ExtractFolder
    d. Set the data type to string
    e. Copy the path of the folder and paste it to Value
5. Creating Local Path Variable - for SourceFolder
    a. same procedure from above, but you paste the directory from the ftpserver: /home/ftpuser/ftp/new/OFAC_*.csv(since you want all ofac files in csv format to download)
    b. Double-click FTP Task > File Transfer > IsRemoteVariable = True
        Remote Variable = User::SourceFolder(dependes on the given name)
6. Executing task
    a. Right Click the FTP Task > Execute task

## PART2
1. Data Flow Task
    a. Double-click dataflow task
    b. On the left side pane, go to Other Sources > Flat File Source
    c. 