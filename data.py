import json
import requests
#Make a request from the api
url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country":"Ghana"}

headers = {
	"X-RapidAPI-Key": "e054a471d2msh1a9779d4c13e032p18bfe2jsn279e8b8365d6",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#Check that the request was successful
if response.status_code == 200:
    #Load the JSON data from the response
    data = response.json()

    #Write data to a text file
    with open("ghanaData_raw.txt","w") as f:
        json.dump(data, f)

else:
    print('Failed! status code:', response.status_code)


# Open the file and read its contents
with open('ghanaData_raw.txt', 'r') as f:
    data = f.read()

# Parse the JSON data
data = json.loads(data)
# Extract the statistics for Ghana
ghana_statistics = next((item for item in data['response'] if item['country'] == 'Ghana'), None)

# Write cleaned data to a text file
with open('cleaned_data.txt', 'w') as f:
    print(f'Population_of_Ghana: {ghana_statistics["population"]}', file=f)
    print(f'Active_cases_in_Ghana: {ghana_statistics["cases"]["active"]}', file=f)
    print(f'Recovered_cases_in_Ghana: {ghana_statistics["cases"]["recovered"]}', file=f)
    print(f'Deaths_in_Ghana: {ghana_statistics["deaths"]["total"]}', file=f)
    print(f'Tests_conducted_in_Ghana: {ghana_statistics["tests"]["total"]}', file=f)


# Read the contents of the cleaned_data.txt file
with open('cleaned_data.txt', 'r') as f:
    contents = f.read()

# Parse the contents as a dictionary
data = {}
lines = contents.strip().split('\n')
for line in lines:
    key, value = line.split(': ')
    data[key] = value

# Write the data to a new file in JSON format
with open('cleaned_data.json', 'w') as f:
    json.dump(data, f, indent=4)