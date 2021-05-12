# # 1.	Името на архитекта - текст;
# # 2.	Брой на проектите - цяло число.
# •	"The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."

name = input()
projects = int(input())
timeForOneProj = 3
timeNeeded = projects * timeForOneProj
print(f"The architect {name} will need {timeNeeded} hours to complete {projects} project/s.")

name = input()
projects = int(input())
time = projects * 3
print(f"The architect {name} will need {time} hours to complete {projects} project/s.")
