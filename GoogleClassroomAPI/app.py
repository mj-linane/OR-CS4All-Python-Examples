import json
import requests

# with open('GoogleClassroomAPI\CS4AllData2018.json') as json_file:
#     CS4AllData2018 = json.load(json_file)

# Open JSON Requests and Assign Variables
# with open('GoogleClassroomAPI\CS4AllData2018.json') as json_file:
#     CS4AllData2018 = json.load(json_file)

course_list = requests.get(
    'https://developers.google.com/classroom/reference/rest/v1/courses/list?apix_params=%7B%22courseStates%22%3A%5B%22ACTIVE%22%5D%7D')

if course_list:
    print('Success!')
else:
    print('An error has occurred.')


def course_name_id_fetcher(file_course_name_list_path):
    with open(file_course_name_list_path) as json_file:
        data = json.load(json_file)
    course_dict = {}
    for course in data['courses']:
        course_dict.update({course['name']: course['id']})
    return course_dict


def get_all_assignment_titles(data_file):
    all_assignment_titles = []
    for assignment in data_file['courseWork']:
        if 'title' in assignment.keys():
            all_assignment_titles.append(assignment['title'])
    return all_assignment_titles
