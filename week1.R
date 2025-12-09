# R course for beginners
# week 1

subject_number = c(1:6)
gender = c("F","M","F","M","M","F")
age = c(27,24,30,26,40,35)
depression = c(0,0,1,0,1,0)

df = data.frame(subject_number, gender, age, depression)

write.csv(df, file = "C:/Users/danie/OneDrive/Desktop/code/subjects.csv")
