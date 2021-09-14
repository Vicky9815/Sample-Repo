def decode(days):
    years,days_= divmod(days,365)
    months,days_= divmod(days_,30)
    weeks,days_= divmod(days_,7)
    return print('These are {} years, {} months, {} weeks and {} days' .format(years, months, weeks, days_))
decode(452)



