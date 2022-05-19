import requests



Try = 1
while Try <= 3:
    date = int(input("Enter a date between 1 to 31 please: ")) 
    if 1 <= date <= 31:
        Try = 4
        response = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-07-{date}&end_date=2016-07-{date}&api_key=qJuirK8yAyaPUufRVd52PCV7zklVV9GL8KhcPFzu")
        response1 = response.json()["near_earth_objects"]
        if len(str(date)) == 1:
            index = 0
            while True:
                try:
                    asteroid = response1[f"2016-07-0{date}"][index]['is_potentially_hazardous_asteroid']
                    if asteroid == True:
                        with open("asteroid.csv", "a") as file:
                            file.write(str(response1[f"2016-07-0{date}"][index])+"\n")
                    else:
                        pass
                    index += 1
                except IndexError:
                    break
        else:
            index = 0
            while True:
                try:
                    asteroid = response1[f"2016-07-{date}"][index]['is_potentially_hazardous_asteroid']
                    if asteroid == True:
                        with open("asteroid.csv", "a") as file:
                            file.write(str(response1[f"2016-07-{date}"][index])+"\n")
                    else:
                        pass
                    index += 1
                except IndexError:
                    break
        print("Success!!")
    else:
        print("Please Enter number between 1 to 31 please!!")
    Try += 1
