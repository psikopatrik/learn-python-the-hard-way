formatter = "{!r} {!r} {!r} {!r}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I had this thing.",                # 'I had this thing.'
    "That you could type up right.",    # 'That you could type upright.'
    "But it didn't sing.",              # "But it didn't sing."  <- double quotes!
    "So I said goodnight.",             # 'So I said goodnight."
))
