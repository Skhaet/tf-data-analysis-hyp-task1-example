import pandas as pd
import numpy as np

import statsmodels.stats.proportion as st

chat_id = 270620880 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    res = st.proportions_ztest([x_success, y_success], [x_cnt, y_cnt], 0)
    a = 0.08
    ret = False
    if res[1] <=a:
        ret = True
        
    return ret # Ваш ответ, True или False
