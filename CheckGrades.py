import sys
import time
import ctypes
import os
from subprocess import Popen
from MyBamaChecker import MyBamaChecker

USERNAME=None
PASSWORD=None

try:
    USERNAME = sys.argv[1]
except:
    USERNAME = os.environ["MYBAMA_USERNAME"]
try:
    PASSWORD = sys.argv[2]
except:
    PASSWORD = os.environ["MYBAMA_PASS"]

if USERNAME == None or PASSWORD == None:
    print("A username or password was not supplied.")
    print("Username and password can also be environment variables:")
    print("\tMYBAMA_USERNAME")
    print("\tMYBAMA_PASS")
    sys.exit(1)

def main():
    crawler = MyBamaChecker(True)
    crawler.login(USERNAME, PASSWORD)
    crawler.click_student()
    crawler.view_grades()
    crawler.select_term_registration("Spring 2016")
    if crawler.new_grades_posted():
        print("A grade has been posted!")
    sys.exit(0)

if __name__ == "__main__":
    main()
