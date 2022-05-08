# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 01:54:27 2021

@author: Jake
"""


from datetime import datetime, date,timedelta,timezone


est=timezone(-timedelta(hours=4))

date = date.today()
day=date.strftime("%d/%b/%Y")



dt = datetime.strptime(day, '%d/%b/%Y')
start = dt - timedelta(days=dt.weekday()+2)
end = start + timedelta(days=6+1)
start=(start.strftime("%B %d, %Y"))
end=(end.strftime("%B %d, %Y"))






string="""
    
**{start} - {end}**
   
**Issues**: There are no issues to report.  
**Activity Report**

{story} - {task} - {col}
{length} mins

{report}

{date} moved to {endcol}

    """


story=input("What user story does your task apply to?")
task=input("What task does your code/work apply to?")
col=input("What column did your task come from? (ToDo, In Progress, Review, Done)")
length=input("How long did you work on the task?")
report=input("Enter your activity report:\n")
endcol=input("Where did you move the task to?")

print(string.format(start=start,end=end,
                    story=story,task=task,col=col,
                    length=length,report=report,
                    date=datetime.now().strftime("%b %d, %Y @%I:%M %p"),
                    endcol=endcol))
