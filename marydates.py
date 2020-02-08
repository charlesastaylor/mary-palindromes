import datetime


def datestring(d):
    return d.strftime('%d%m%Y')

def is_palindrome(s):
    assert len(s) == 8, "Only care about 8 character datestrings"
    return s[:4] == s[4:][::-1]

if __name__ == "__main__":
    # Assumptions:
    # Using Uk dd/mm/yyyy format only

    # 02/02/2020 was palindromic
    # When was last?
    d = datetime.date(2020, 2, 2)
    while True:
        d -= datetime.timedelta(days=1)
        if is_palindrome(datestring(d)):
            print("Previous to 02022020: ", datestring(d))
            break
    # You're correct

    # When is next?
    d = datetime.date(2020, 2, 2)
    count = 0
    while True:
        d += datetime.timedelta(days=1)
        if is_palindrome(datestring(d)):
            print("\nFollowing 02022020: ", datestring(d))
            break
    # You're correct
    
    # When is one after that?
    d = datetime.date(2020, 2, 2)
    count = 0
    while True:
        d += datetime.timedelta(days=1)
        if is_palindrome(datestring(d)):
            count += 1
            if count == 2:
                print("\nOne after that: ", datestring(d))
                break
    # You're incorrect,  you missed 22022022
    
    # Next 100
    d = datetime.date(2020, 2, 2)
    count = 0
    with open("next100.txt", "w") as f:
        while count < 100:
            d += datetime.timedelta(days=1)
            s = datestring(d)
            if is_palindrome(s):
                count += 1
                f.write(f'{s}\n')
    
    # Can occur in month other than Feb this century?
    print("\nCan palindrome occur in month other than Feb this Century?")
    d = datetime.date(2000, 1, 1)
    dates_found = []
    while d.year < 2100:
        d += datetime.timedelta(days=1)
        if d.month == 2:
            continue # skip feburary
        if is_palindrome(datestring(d)):
            dates_found.append(datestring(d))
    if dates_found:
        print("Yes", dates_found)
    else:
        print("No")
    # You're correct

    # Will it ever happen again in Feburary after this century?
    # Feburary => first two digits of year must be 20 so no
    # not until after year 9999 anyway
    # You're mostly correct ;)

    # How many years is next after 29 12 2192?
    d = datetime.date(2192, 12, 29)
    while True:
        d += datetime.timedelta(days=1)
        if is_palindrome(datestring(d)):
            print("\nNext after 29 12 2192: ", datestring(d))
            break
    start, finish = datetime.date(2192, 12, 29), d
    years, days = divmod((finish - start).days, 365)
    print(f'Ie. {years} years and {days} days')

    # Correct

    # Is this same as gap between 29 11 1192 and 10 02 2001?
    d = datetime.date(1192, 11, 29)
    while True:
        d += datetime.timedelta(days=1)
        if is_palindrome(datestring(d)):
            print("\nNext after 29 11 1192: ", datestring(d))
            break
    start, finish = datetime.date(1192, 11, 29), d
    years, days = divmod((finish - start).days, 365)
    print(f'Ie. {years} years and {days} days')

    # Correct

    # What is probabilty of being born on palendromic date in:
    # a) this century?
    d = datetime.date(2000, 1, 1)
    days_in_century = (datetime.date(2100,1,1) - datetime.date(2000, 1, 1)).days
    dates_found = []
    while d.year < 2100:
        d += datetime.timedelta(days=1)
        if is_palindrome(datestring(d)):
            dates_found.append(datestring(d))
    print(f'\nNumber of palindromic dates in 21st century: {len(dates_found)}')
    print(f'Total number of days in century: {days_in_century}')
    print(f'Prob of being born on a palindromic date: {100 * len(dates_found) / days_in_century:.2f}%')

    # b) this millenium?
    d = datetime.date(2000, 1, 1)
    days_in_millenium = (datetime.date(3000,1,1) - datetime.date(2000, 1, 1)).days
    dates_found = []
    while d.year < 3000:
        d += datetime.timedelta(days=1)
        if is_palindrome(datestring(d)):
            dates_found.append(datestring(d))
    print(f'\nNumber of palindromic dates in this millenium: {len(dates_found)}')
    print(f'Total number of days in millenium: {days_in_millenium}')
    print(f'Prob of being born on a palindromic date: {100 * len(dates_found) / days_in_millenium:.2f}%')


