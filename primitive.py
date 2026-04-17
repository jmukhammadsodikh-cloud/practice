print("======")
# in JAVA: variable is name of storage location
# in PYTHON: variable is named reference

count = 500
count_type = type(count)
print("count:", count, count_type)

# qulayroq print qlishni hohlasak format print
print(f"the count:{count} and type: {count_type}")

# qoida pythonda primit variable ham object
result1 = count.bit_count()  # method
reulst2 = count.numerator  # state
print(result1, reulst2)
