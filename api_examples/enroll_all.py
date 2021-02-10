import requests

username = ''
password = ''

base_url = 'http://localhost:8000/api/'

# Retrieve all courses
r = requests.get(f'{base_url}courses/')
courses = r.json()


available_courses = ', '.join([course['title'] for course in courses])
print(f'Available Courses: {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(
        f'{base_url}courses/{course_id}/enroll/', auth=(username, password))

    if r.status_code == 200:
        # Success
        print(f'Successfully enrolled in {course_title}')
