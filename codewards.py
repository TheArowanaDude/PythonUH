def printer_error(s):
    check_bad = 'nopqrstuvwxyz'
    count = len(s)
    bad = 0

    for i in check_bad:
        for j in s:
            if i == j:
                bad += 1

    return (bad)


print(printer_error('akdsjfhkjdfzzzzzz'))
