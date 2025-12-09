# R course for beginners
# week 7

subject_number = seq(from = 1, to = 100, by = 1)
age = sample((15:40), 100, replace = T)
gender = sample(c('F','M'), 100, replace = T)
depression = rbinom(100, size = 1, prob = 0.15)

df = data.frame(subject_number, gender, age, depression)
