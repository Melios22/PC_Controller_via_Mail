# PC Controller via Mail 🌐
<h1 align="left">
  <img src="src/assets/icon.png" alt="icon" width="200"></img>
</h1>


## 📖 Table of contents 
- [🛠️Setup environment](#%EF%B8%8Fsetup-environment)
- [🤔How to use](#How-to-use)
- [💡How it works](#How-it-works)
- [🎞️Tutoriall video](#%EF%B8%8Ftutorial-video)
- [🏅Member](#Member)

## 🛠️Setup environment

First, you need to clone the repository at: https://github.com/Melios22/PC_Controller_via_Mail.git

```bash
git clone https://github.com/Melios22/PC_Controller_via_Mail.git
```

Language: Python \
Version: 3.10+ \
Install require module
```python
pip install -r module.txt
```

<details>
  <summary>Or you can</summary>
  
```python
pip install opencv-python pillow pynput customtkinter
```
</details>

## 🤔How to use
Redirect to the `src` folder and locate the `main.py` file. Run the file with Python:
```python
python main.py
```

## 💡How it works
The program will wait for a new email sent from any user to `emailcontrolmmt@gmail.com` with the subject of *Mail Control*
The included body is the command to be executed. The program will execute the command and reply to the user with the result of the command.
- From:  
```bash
  emailcontrolmmt@gmail.com
```
- Subject: 
```bash
  Mail Control
```
- 📝Command list: 
```python
  screenshot [file_name]
```
> <details>
>  <summary>How it works</summary>
>
>Take the picture of your screen and save it into file_name.png. \
>**Path**: “Files\Pictures\file_name.png” \
>**Default file_name**: “a.png” 
></details>


```python
  webcam [file_name]
```
> <details>
>  <summary>How it works</summary>
>
>Take a picture from your webcam and save it in file_name.png. \
>**Path**: “Files\Pictures\file_name.png. \
>**Default file_name**: “b.png”
></details>


```python
  keylog [time_in_seconds]
```
> <details>
>  <summary>How it works</summary>
>
>When recive mail the app will wating time in seconds and capture all keys from your keyboard. \
>**Path**: “Files\Keylog.txt”  \
>**Default time in seconds**: 5s
></details>


```python
  logout
```
> <details>
>  <summary>How it works</summary>
>Logout account in your computer.
></details>


```python
  shutdown [time_in_seconds]
```
> <details>
>  <summary>How it works</summary>
>  
>Shutdown your computer after time in seconds.  \
>**Default time in seconds**: 1 second
></details>


```python
  listApp
```
> <details>
>  <summary>How it works</summary>
>  
>Take all your running app and write it into Applications.txt.  \
>**Path**: “File\Applications.txt”  
></details>

```python
  listProcess
```
> <details>
>  <summary>How it works</summary>
>  
>Take all of your running app and write it to Processes.txt.  \
>**Path**: “Files\Processes.txt”
></details>

```python
  terminateProcess [PID/Process_Name]
```
> <details>
>  <summary>How it works</summary>
>  
>Terminate a process using PID or Process Name.  \
>Must pass PID/Process Name  \
>**Error handling**  
> -	**Missing agrument**: “ERROR: Terminate process command misses an argument.”  \
> -	**Cannot be terminated**: “ERROR: The process with PID/Process Name could not be terminated.”  \
> -	**Not found process**: “ERROR: The process PID/Process Name not found.”
></details>

```python
  log
```
> <details>
>  <summary>How it works</summary>
>  
>Record all mails sent to Server.  \
>**Format**:  \
>----------------------------------------  \
>**Time**:		DD MMM YYY HH:MM:SS  \
>**From**:		sender email  \
>**Content**:            all commands in mail  \
>**Reply**:  \
>**Attachment**:	Path  \
>----------------------------------------  \
>**Path**: “Files\mail.log”
></details>

```python
  help
```
> <details>
>  <summary>How it works</summary>
>  
>List of all commands. If server recive any command not in help it will replaced by help  \
>**Path**: “Files\help.txt”
></details>

## 🎞️Tutorial video
[ ![YouTube](https://cdn.emojidex.com/emoji/mdpi/YouTube.png "YouTube") Tutorial video on Youtube](https://www.youtube.com/watch?v=Doc2UtP7quE)

Or watch directly in here 👇

  https://github.com/kggmt/kggmt/assets/81817335/98cd5df2-e72c-4908-b321-51ad53c1825b  




## 🏅Member
**22127275 - [Tran Anh Minh](https://github.com/Melios22)** \
**22127280 - [Doan Dang Phuong Nam](https://github.com/Namronaldo08102004)** \
**22127465 - [Bui Nguyen Lan Vy](https://github.com/buinguyenlanvy)** \
**22127475 - [Diep Gia Huy](https://github.com/kggmt)** 

# [🏠 Back to top](#PC-Controller-via-Mail-)
