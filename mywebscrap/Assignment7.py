import requests
import bs4

# Specify the URL for the new link
url = "https://www.cosmopolitan.com/entertainment/tv/news/a31651/10-best-novelas-of-all-time/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # Select H2 headers that contain the telenovela titles
    h2_headers = soup.select('h2')  # Select all H2 headers

    # Extract titles and store in a list
    telenovela_titles = [header.get_text() for header in h2_headers]

    # Print out the titles
    if telenovela_titles:
        for index, title in enumerate(telenovela_titles, start=1):
            print(f"{index}. {title}")
    else:
        print("No titles found.")

    # Save the titles to a file
    with open("telenovela_titles.txt", "w", encoding="utf-8") as file:
        for title in telenovela_titles:
            file.write(title + "\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")