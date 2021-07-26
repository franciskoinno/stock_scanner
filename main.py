from selenium import webdriver

# github change
# git change
chrome_driver_path = r"C:\Users\Francis\Desktop\chromedriver_win32\chromedriver.exe"
driver_long_lower_shadow = webdriver.Chrome(chrome_driver_path)
driver_hammer = webdriver.Chrome(chrome_driver_path)
driver_dragon = webdriver.Chrome(chrome_driver_path)
driver_white = webdriver.Chrome(chrome_driver_path)
driver_long_lower_shadow.get("https://finviz.com/screener.ashx?v=211&f=cap_smallover,fa_salesqoq_o5,sh_curvol_o50,sh_instown_o10,sh_price_o15,ta_candlestick_lls,ta_highlow52w_b0to10h,ta_sma200_sb50,ta_sma50_pa&ft=3")
driver_hammer.get("https://finviz.com/screener.ashx?v=211&f=cap_smallover,fa_salesqoq_o5,sh_curvol_o50,sh_instown_o10,sh_price_o15,ta_candlestick_h,ta_highlow52w_b0to10h,ta_sma200_sb50,ta_sma50_pa&ft=3")
driver_dragon.get("https://finviz.com/screener.ashx?v=211&f=cap_smallover,fa_salesqoq_o5,sh_curvol_o50,sh_instown_o10,sh_price_o15,ta_candlestick_dd,ta_highlow52w_b0to10h,ta_sma200_sb50,ta_sma50_pa&ft=3")
driver_white.get("https://finviz.com/screener.ashx?v=211&f=cap_smallover,fa_salesqoq_o5,sh_curvol_o50,sh_instown_o10,sh_price_o15,ta_candlestick_mw,ta_highlow52w_b0to10h,ta_sma200_sb50,ta_sma50_pa&ft=3")
