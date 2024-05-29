# reshape 패키기
# melt() >> 와이드 포맷을 롱 포맷으로
# cast() >> 롱포맷을 와이드 포맷으로

install.packages("reshape2")
library(reshape2)

smiths
# 와이드 포맷이 되어 있는 자료

# melt()
# smiths를 롱포맷으로 바꿔주기
melt(data = smiths)
# variable과 value을 열로 사용하여 롱포맷으로 변환됨

#Using subject as id variables
# 식별자 변수를 지정하지 않으면 변수들 중 팩터나 문자열로 되어있는 변수를 자동으로 식별자 변수로 사용함

# 식별자 변수 지정하기 : id.vars
melt(data = smiths,
     id.vars = "subject")

#  측정 변수 지정하기 : measure.vars (측정변수로 지정되지 않은 나머지 변수들이 식별자 변수가 된다.)
melt(data = smiths,
     measure.vars = c(2:5)) # 인덱스를 사용하여 지정

melt(data = smiths,
     measure.vars = "tiem", "age", "weight", "height")

# 둘 다 지정하기
melt(data = smiths,
     id.vars = "subject",
     measure.vars = c(2:4))

# variable과 value 이름 지정하기 : variable.name / value.name
melt(data = smiths,
     id.vars = "subject",
     measure.vars = c(2:4),
     variable.name = "var",
     value.name = "val")


# cast()
smiths.long <- melt(data = smiths,
                    id.vars = "subject",
                    measure.vars = c(2:4),
                    variable.name = "var",
                    value.name = "val")

#smiths.long
# smiths,long를 와이드 포맷으로 바꿔주기

# cast(data = 롱포맷 데이터 이름, formula= 식별자 변수 ~ 측정 변수)
# formula : 틸다(~)를 중심으로해서 왼쪽에 식별자 변수(id)를 지정 오른쪽에 측정 변수(variable)를 지정 여러개일 경우 +로 이어서 지정
dcast(data = smiths.long,
      formula=subject ~ var)

# Using val as value column: use value.var to override.
# 값이 들어가 있는 열을 지정하지 않게되면 마지막 열을 값이 들어가있는 열로 간주하여 자동으로 만든다.

# 값이 들어있는 열 지정해주기 : value.var
dcast(data = smiths.long,
      formula=subject ~ var,
      value.var = "val")

------------------------------------------------------------------
# 실전 연습
  
head(airquality)
# 전형적인 와이드 포맷 데이터

aq.long <- melt(airquality,
                c("Month", "Day"))

head(aq.long)
tail(aq.long)

aq.wide <- dcast(aq.long,
                 Month + Day ~ variable,
                 value.var = "value")

head(aq.wide)

# 주의
dcast(aq.long, Month ~ variable)
# Aggregation function missing: defaulting to length
# 식별자 변수가 각각의 요소를 하나씩 구분하지 못하도록 설정되어 식별자 요소별 variable의 값들을 모아서 반환해주고 해당 값을 어떻게 활용할지 물어봄
# 따라서 식별자 변수를 지정할 때 요소가 구분되어 하나씩 담기도록 설정하도록 주의

# 또는 해야할 일을 지정해줘서 해결도 가능
dcast(aq.long, Month ~ variable,
      fun.aggregate = mean, na.rm=TRUE)