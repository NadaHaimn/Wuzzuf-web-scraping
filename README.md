# Web Scraper for Wuzzuf Job Listings

This Python script scrapes job listings from Wuzzuf.net for Data Analyst positions and exports the data into a CSV file. The script uses the requests library to fetch web pages, BeautifulSoup from the bs4 library for parsing HTML, and csv for writing the scraped data into a CSV file.

## Features

- Scrapes Job Titles: Extracts job titles from the search results.
- Scrapes Company Names: Extracts the names of companies offering the jobs.
- Scrapes Location Data: Extracts the job location.
- Scrapes Job Skills: Extracts the required skills for the job.
- Scrapes Posting Date: Extracts the date when the job was posted.
- Handles Pagination: Automatically fetches data from multiple pages until all relevant pages are scraped.
- CSV Export: Saves the scraped data into a CSV file for easy analysis and storage.

## Installation

To run this script, you'll need Python 3.x installed on your machine. Additionally, you'll need to install the following Python packages:

pip install requests
pip install beautifulsoup4
## Customization

- Change Search Query: You can modify the search query by changing the URL in the result = requests.get(...) line to target different jobs or locations.
- Additional Fields: The script includes commented-out sections for scraping salary and job requirements. Uncomment and modify these sections as needed.

## Limitations

- Dynamic Content: The script might not work correctly if the website changes its HTML structure.
- Rate Limiting: Frequent scraping may lead to your IP being blocked. Consider adding delays between requests if scraping a large number of pages.

## Contributing

If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This version of the README omits the "Usage" section while retaining key information about the project.
