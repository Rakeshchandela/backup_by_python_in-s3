import shutil
import datetime
import os

def backups_file(source,destination):
    today=datetime.date.today()
    backups_file_name=os.path.join(destination, f"backups{today}.tar.gz")
    shutil.make_archive(backups_file_name,'gztar',source)

source=r"\Users\Charan\Desktop\python\chapter 4"
destination=r"\Users\Charan\Desktop\python\chapter 4\backup"

backups_file(source,destination)