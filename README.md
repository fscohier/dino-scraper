# dino-scraper
As part of a project, I needed to create some fake financial data.
In order to replicate fake company names, I created this scraper which extracts all dinosaur names from a Wikipedia page.

This scraper uses the BeautifulSoup library to parse the HTML. Once parsed, we extract the dinosaur names based on the HTML tags (ul > li > i) and add to a list.
Finally, the list is exported in a CSV file for further use and a success message is printed in the terminal.

<div align="center">
  <img src="https://github.com/fscohier/dino-scraper/blob/5a4dcfbfed213ca56b681cd5ec97f9ef2bd57e35/terminal_output.png" alt="output" />
</div>
