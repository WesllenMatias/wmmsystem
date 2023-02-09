import requests

url = "https://api-football-v1.p.rapidapi.com/v3/odds/bets"

headers = {
	"X-RapidAPI-Key": "df445527d2msh12b1bd4742e9f9cp183509jsn035fabe53b47",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)