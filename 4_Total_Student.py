#WAP If there are 20 students who like football, 
# 30 students like badminton and 10 like both.
# There are 20 who are not interested in any of the games. How many total number of students are there?

football = 20
Badminton = 30
Both = 10
Not_interested = 20

Total_student = (football-Both)+(Badminton-Both)+(Both)+(Not_interested)
Total_student = (football)+(Badminton-Both)+(Not_interested)

print("Total Number of Student: ", Total_student)