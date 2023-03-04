import ftplib
import os
from datetime import datetime
FTP_HOST = ""
FTP_USER = ""
FTP_PASS = ""
def get_size_format(n, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if n < 1024:
            return f"{n:.2f}{unit}{suffix}"
        n /= 1024

def get_datetime_format(date_time):
    date_time = datetime.strptime(date_time, "%Y%m%d%H%M%S")
    return date_time.strftime("%Y/%m/%d %H:%M:%S")
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
print(ftp.getwelcome())
ftp.cwd("") #в скобках писать директорию
print("*"*50, "LIST", "*"*50)
ftp.dir()

