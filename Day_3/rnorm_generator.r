
w <- seq(0, 100, by = 1)
x <- rnorm(w, mean = 2.5, sd = 0.5)
y <- rnorm(w, mean = 2.5, sd = 0.5)
z <- rnorm(w, mean = 2.5, sd = 0.5)
t=cbind(x,y,z)

library(MASS)
write.matrix(t,file="uwe.csv")