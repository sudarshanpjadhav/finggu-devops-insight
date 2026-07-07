import requests


def finggu_integration_with_jenkins(job_name):
    jenkins_url = os.getenv('FINGGU_JENKINS_URL')
    response = requests.get(f'{jenkins_url}/job/{job_name}/api/json')
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from Jenkins'}