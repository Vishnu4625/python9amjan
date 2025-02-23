import pandas as pd

# Load the dataset
# Assuming the dataset is in CSV format, with columns like 'School', 'Year', 'Student', 'Subject', 'Marks'
data = pd.read_csv('student_marks.csv')

# 1. Reward the top performer based on cumulative marks over 3 years
def top_performer(data):
    # Group by School and Student, summing marks across 3 years for all subjects
    cumulative_marks = data.groupby(['School', 'Student']).agg({'Marks': 'sum'}).reset_index()
    top_performers = cumulative_marks.loc[cumulative_marks.groupby('School')['Marks'].idxmax()]
    return top_performers

# 2. Rank each student within their school for 2020 and compare Rank 10 across schools
def rank_2020(data):
    data_2020 = data[data['Year'] == 2020]
    total_marks_2020 = data_2020.groupby(['School', 'Student']).agg({'Marks': 'sum'}).reset_index()
    total_marks_2020['Rank'] = total_marks_2020.groupby('School')['Marks'].rank(ascending=False, method='min')
    rank_10_marks = total_marks_2020[total_marks_2020['Rank'] == 10].sort_values(by='Marks', ascending=False)
    return rank_10_marks

# 3. Find students with highest improvement from 2019-2021 for each subject
def highest_improvement(data):
    data_2019 = data[data['Year'] == 2019].groupby(['School', 'Student', 'Subject']).agg({'Marks': 'sum'}).reset_index()
    data_2021 = data[data['Year'] == 2021].groupby(['School', 'Student', 'Subject']).agg({'Marks': 'sum'}).reset_index()
    
    improvement = pd.merge(data_2021, data_2019, on=['School', 'Student', 'Subject'], suffixes=('_2021', '_2019'))
    improvement['Improvement'] = improvement['Marks_2021'] - improvement['Marks_2019']
    
    highest_improvement_students = improvement.loc[improvement.groupby('Subject')['Improvement'].idxmax()]
    return highest_improvement_students

# 4. Identify the best school for Arts, Science, and Commerce streams based on marks in respective subjects
def best_school_per_stream(data):
    stream_subjects = {
        'Arts': ['Hindi', 'English', 'History', 'Geography', 'Civics'],
        'Science': ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science'],
        'Commerce': ['Hindi', 'English', 'Mathematics', 'Computer Science', 'Physical Education']
    }
    
    best_schools = {}
    
    for stream, subjects in stream_subjects.items():
        stream_data = data[data['Subject'].isin(subjects)]
        stream_data_avg = stream_data.groupby(['School', 'Student']).agg({'Marks': 'mean'}).reset_index()
        best_school = stream_data_avg.groupby('School')['Marks'].mean().idxmax()
        best_schools[stream] = best_school
        
    return best_schools

# 5. Categorize marks and count students in each category per school per year
def categorize_marks(data):
    def categorize(row):
        if row <= 20:
            return 'Very Poor'
        elif 20 < row <= 40:
            return 'Poor'
        elif 40 < row <= 60:
            return 'Average'
        elif 60 < row <= 80:
            return 'Good'
        else:
            return 'Very Good'
    
    # Calculate average marks per student per year
    data_avg = data.groupby(['School', 'Year', 'Student']).agg({'Marks': 'mean'}).reset_index()
    data_avg['Category'] = data_avg['Marks'].apply(categorize)
    
    category_counts = data_avg.groupby(['School', 'Year', 'Category']).size().unstack(fill_value=0)
    return category_counts

# 6. Identify best school for each year based on the highest number of students in Good and Very Good category
def best_school_for_year(data):
    category_counts = categorize_marks(data)
    best_schools = {}
    
    for year in [2019, 2020, 2021]:
        good_and_very_good = category_counts.loc[year, ['Good', 'Very Good']].sum(axis=1)
        best_school = good_and_very_good.idxmax()
        best_schools[year] = best_school
        
    return best_schools

# 7. Identify the fastest-growing school based on Good and Very Good category
def fastest_growing_school(data):
    category_counts = categorize_marks(data)
    
    growth_rate = {}
    for school in category_counts.index:
        good_and_very_good_2019 = category_counts.loc[school, 2019, ['Good', 'Very Good']].sum()
        good_and_very_good_2021 = category_counts.loc[school, 2021, ['Good', 'Very Good']].sum()
        growth_rate[school] = good_and_very_good_2021 - good_and_very_good_2019
    
    fastest_growing_school = max(growth_rate, key=growth_rate.get)
    return fastest_growing_school

# Running all analyses
top_performers = top_performer(data)
rank_10_comparison = rank_2020(data)
highest_improvement_students = highest_improvement(data)
best_schools_per_stream = best_school_per_stream(data)
category_counts = categorize_marks(data)
best_schools_by_year = best_school_for_year(data)
fastest_growing = fastest_growing_school(data)

# Results can be printed or saved as needed
print(top_performers)
print(rank_10_comparison)
print(highest_improvement_students)
print(best_schools_per_stream)
print(category_counts)
print(best_schools_by_year)
print(fastest_growing)

# Optionally: Save results to CSV or Excel for presentation purposes
top_performers.to_csv('top_performers.csv', index=False)
rank_10_comparison.to_csv('rank_10_comparison.csv', index=False)
highest_improvement_students.to_csv('highest_improvement.csv', index=False)
category_counts.to_csv('category_counts.csv')
best_schools_by_year.to_csv('best_schools_by_year.csv')
