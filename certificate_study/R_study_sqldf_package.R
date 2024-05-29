# sqldf()
# R에서 sql문을 사용할 수 있도록 해주는 함수

install.packages("sqldf")
library(sqldf)

data("mtcars")
mtcars

sqldf("select * from mtcars where mpg > 30", row.names = TRUE)
# row.names = TRUE >> 행의 이름을 같이 출력시키기 위함

sqldf("select * from mtcars where cyl = 6 order by mpg", row.names = TRUE)

sqldf("select avg(mpg) as avg_mpg, avg(wt) as avg_wt, gear from mtcars where cyl in (4, 6) group by gear", row.names = TRUE)

--------------------------------------------------
  
data("iris")

sqldf("select distinct Species from iris")

sqldf("select * from iris limit 3")

sqldf("select avg([Sepal.Length]) from iris where Species='setosa'")
# 변수 이름안에 '.'이 포함된 경우 []로 묶어서 표기해준다













