# LEPortableHelper
LEPortableHelper, using Locale Emulator without installing.  (or...portablized?)  

這是一個讓你免安裝就可以用Loacle Emulator的小工具。(或是叫做…攜帶版?)

# What's this
This is a helper script for [Locale Emulator](https://github.com/xupefei/Locale-Emulator).  
這是一個Locale Emulator的外部工具。  

The script reads the setting file of Locale Emulator (LE) and generate a batch file (or just run it) for running another program, without install Locale Emulator or/and click it in context menu.  
這個腳本可以讀取Locale Emulator (LE)的設定檔，然後產生一個.bat檔案(或直接執行)，讓你不必安裝LE就可以換區執行其他程式。  

This make using LE more like using MS Applocale.  
這可以讓LE用起來更像MS Applocale.

#How to use
You have to install and uninstall LE as least one time to generate necessary files (e.g. setting files).  You don't have to do this step for every computers. Just do it once and keep the generated files.  
Then copy **LEPortableHelper.py** to the same folder of **LEProc.exe**  and run it.  

你需要至少安裝再移除LE一次，好讓LE產生一些必要的檔案(例如設定)。你不需要在每台電腦都做一次，留下那些檔案即可。
然後複製**LEPortableHelper.py**到**LEProc.exe**的目錄下，並執行它。

# How to bulid
Python 2.7.X for  
for executing the script.
  
py2exe  
for buliding an exe version.

#Known Issues
**Unicode path is not supported.** Because Windows Command Prompt dose not support unicode.  
So, this script only support path which is composed by English letters.  

**不支援Unicode路徑**，因為Windows命令列視窗也不支援Unicode，所以沒辦法。  
所以目前只能使用在純英文路徑上。

#Q&A

Q: 為什麼介面是英文?  
A:  因為Sublime好像跟我家的輸入法八字不合，打中文有點麻煩。

Q: The code is so messy.  
A: Sorry, I'm still a beginner.

