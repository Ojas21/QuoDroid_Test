import json
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def execute_tests(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tests = data.get('tests', [])
            test_suite = f"""*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
"""
            for test in tests:
                steps = test.get('steps', [])
    
                adjusted_steps = []
                #extracting .robot keywords
                for step in steps:
                    if "Open Browser" in step:
                     
                        browser = step.split("browser='")[1].split("'")[0]
                        
                    elif "Go To" in step:
               
                        url = step.split("url='")[1].split("'")[0]
                        url="".join(url)
                        
                    else:
                        adjusted_steps.append(step)
                #creating the robot file
                adjusted_steps.append(f"Open Browser  {url}  {browser}\n")

                test_suite += f"""Test {test['title']}
    {'    '.join(adjusted_steps)}
"""
                
          
            with open('test_suite.robot', 'w') as f:
                f.write(test_suite)
            # Executing the test suite using Robot Framework
            result = subprocess.run(['robot', 'test_suite.robot'], capture_output=True, text=True)
            # Returning the results
           
            return JsonResponse({'result': result.stdout})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
