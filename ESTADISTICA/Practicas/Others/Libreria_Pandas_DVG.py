    
def date_fixer(x):

    """   fixes the usual error on dates   """
    
    import datetime
    if x.year > 1989:
        year = x.year - 100
    else:
        year = x.year
    return datetime.date(year,x.month,x.day)