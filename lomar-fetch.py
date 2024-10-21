import requests

def lomar():
    url = "https://www.lockheedmartin.com"
    cur = "Fetching Lockheed Martin data..."
    print(cur)
    curr = "Processing request..."
    print(curr)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Data fetched successfully!")

            with open("lockheed_data.html", "w") as file:
                file.write(response.text)
        else:
            print(f"Failed to fetch data, status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    lomar()
