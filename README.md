# dino-scraper
As part of a project, I needed to create some fake financial data.
In order to replicate fake company names, I created this scraper which extracts all dinosaur names from a Wikipedia page.

This scraper uses the BeautifulSoup library to parse the HTML. Once parsed, we extract the dinosaur names based on the HTML tags (ul > li > i) and add to a list.
Finally, the list is exported in a CSV file for further use (random company name generator).
