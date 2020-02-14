import os
import time

import pandas as pd
from bs4 import BeautifulSoup
from pandas import ExcelWriter

main_path = "D:\PycharmProjects\YocketAdmits"
os.chdir(main_path)
os.environ["LANG"] = "en_US.UTF-8"

file = open(r"C:\Users\Others\Desktop\ScrapHTML.txt")
page = file.read()
soup = BeautifulSoup(page, 'html.parser')

all_names = []
all_cgpa = []
all_workexp = []
all_TOEFL = []
all_GRE = []
all_universiy =[]
all_dept = []
all_term =[]
b = []

name = soup.find_all("div", attrs="col-sm-9")
score = soup.findAll("div", attrs="col-sm-3 col-xs-6")
course = soup.find_all("div", attrs={"ui-widget col-sm-4"})

for n in range(0,len(course)):
    a = course[n].find("input")
    b.append(a.get("value"))

for n  in range(0, len(name)):
    a = str(name[n].text)
    if not("Find admits & rejects") in a:
        a = a.split("\n")
        while(a.__contains__("")):
            a.remove("")
        all_names.append(a[0])
        all_universiy.append(b[0])
        all_term.append(a[2])
        all_dept.append(b[1])




for i in range(0, len(score)):
    a = str(score[i].text)
    if a.__contains__("GRE") and not("APPLICATION") in a:
        a = a.replace("\n GRE\n","")
        all_GRE.append(a)
    if a.__contains__("TOEFL") and not("APPLICATION") in a:
        a = a.replace("\nTOEFL\n", "")
        all_TOEFL.append(a)
    if a.__contains__("IELTS") and not("APPLICATION") in a:
        a = a.replace("\nIELTS\n","")
        all_TOEFL.append(a)
    if a.__contains__("UNDERGRAD") and not("APPLICATION") in a:
        a = a.replace("\nUNDERGRAD\n","")
        all_cgpa.append(a)
    if a.__contains__("WORK EX") and not("APPLICATION") in a:
        a = a.replace("\nWORK EX\n", "")
        all_workexp.append(a)

final_result = pd.DataFrame({'Name' : all_names, 'University' : all_universiy, 'Term' : all_term, 'Department' : all_dept, 'GRE' : all_GRE, 'TOEFL' : all_TOEFL, 'WORK Exp' : all_workexp, 'CGPA' : all_cgpa})

results_path = 'D:\Web_Scraping'
os.chdir(results_path)
time1 = time.strftime("%m%d-%H%M")
folder_name = "admit_buffalo" + time1
writer = ExcelWriter(folder_name + '.xlsx')
final_result.to_excel(writer, 'all_summary_roles', index=False)
writer.save()

print(final_result)

