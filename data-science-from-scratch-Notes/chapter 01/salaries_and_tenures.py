# from page 23 onwards
 salaries_and_tenures = [(83000, 8.7), (88000, 8.1), 
                        (48000, 0.7), (76000, 6), 
                        (69000, 6.5), (76000, 7.5), 
                        (60000, 2.5), (83000, 10), 
                        (48000, 1.9), (63000, 4.2)]
                        
                        
# Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure]append(salary)
    
# Keys are years, each value is average salary for that tenure.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for  tenure, salaries in salaries_and_tenures.items()
}

# output for above:
 # {0.7: 48000.0, 
 # 1.9: 48000.0, 
 # 2.5: 60000.0, 
 # 4.2: 63000.0, 
 # 6: 76000.0, 
 # 6.5: 69000.0, 
 # 7.5: 76000.0, 
 # 8.1: 88000.0, 
 # 8.7: 83000.0, 
 # 10: 83000.0}
 
 
 def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Keys are tenure buckets, values are lists of salaries for that bucket.
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
    
# Keys are tenure buckets, values are average salary for that bucket.
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

# Output:
# {'between two and five': 61500.0, 
# 'less than two': 48000.0, 
# 'more than five': 79166.66666666667}


# Page 26
# You notice that there seems to be a correspondence between years of
# experience and paid accounts:
# 0.7  paid 
# 1.9  unpaid 
# 2.5  paid 
# 4.2  unpaid 
# 6.0  unpaid 
# 6.5  unpaid 
# 7.5  unpaid 
# 8.1  unpaid 
# 8.7  paid 
# 10.0 paid


# Page 27
def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
        
        
