library(lavaan)
# 데이터 불러오기
data <- read.csv("survey_data_standardized.csv")


model <- '
    # Define observed variables
    commute_time =~ total_commute_minutes 
    sleep_time =~ total_sleep_minutes
    work_time =~ total_work_minutes
    income =~ ADQ3E
    time_with_family =~ AQ37_1 + AQ37_2 + AQ37_3 + AQ37_4 + AQ37_5
    #+ gu_140 + gu_170 + gu_200 + gu_215 + gu_230 + gu_260 + gu_290 + gu_305 + gu_320 + gu_350 + gu_380 + gu_410 + gu_440 + gu_470 + gu_500 + gu_530 + gu_545 + gu_560 + gu_590 + gu_620 + gu_650 + gu_680 + gu_710 + gu_740
    #+ ADQ3A_2 + ADQ3A_3 + ADQ3A_4 + ADQ3A_5 + ADQ3A_6 + ADQ3A_7
    
    # Define paths
    work_time ~ a_1*commute_time
    sleep_time ~ r*work_time + a_2*commute_time
    income ~ b_1*sleep_time + b_2*time_with_family +c*commute_time + ADQ3A_2 + ADQ3A_3 + ADQ3A_4 + ADQ3A_5 + ADQ3A_6 + ADQ3A_7
  
'


# SEM 모델 적합
fit <- sem(model, data = data)

# Calculating TLI, CFI, RMSEA
fit_indices <- fitMeasures(fit, c("TLI", "CFI", "RMSEA"))

fit_indices
# 모델 요약 보기
summary(fit)

0# SEM 모델 결과 시각화
semPaths(fit, "est", whatLabels = "std", layout = "tree")
