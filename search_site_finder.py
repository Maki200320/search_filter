#To run this code\
#create new .venv(python Environment) so our installed packages will be available only in this file directory
#pip install googlesearch-python
#pip install urllib3
#run those commands above in terminal


import webbrowser
from googlesearch import search
from urllib.parse import urlparse

# Google search with multiple site restrictions
def search_query(query):
    # List of sites to include in the search
    sites = [
        "stackoverflow.com",
        "medium.com",
        "w3schools.com",
        "tutorialspoint.com",
        "geeksforgeeks.org"
    ]
    
    # Construct the site restriction part of the query
    site_restriction = " OR ".join(f"site:{site}" for site in sites)
    
    # Append the site restrictions to the search query
    query_with_sites = f"{query} ({site_restriction})"
    
    # Perform the search
    return search(query_with_sites)  

# Filter URLs to get only the first result for each site
def get_first_result_per_site(urls, sites):

    site_results = {site: None for site in sites}
    
    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        # Check if the domain matches one of the allowed sites and has not been added yet
        for site in sites:
            if site in domain and site_results[site] is None:
                site_results[site] = url
                break
    
    # Filter out None values and return the list of URLs
    return [url for url in site_results.values() if url is not None]

# Open the browser
def open_browser(urls):
    for url in urls:
        webbrowser.open(url)


#--------------------------------------------------------------------------------------------------------------------------------
def main():
    #order
    allowed_sites = [
        "stackoverflow.com",
        "medium.com",
        "w3schools.com",
        "tutorialspoint.com",
        "geeksforgeeks.org"
    ]
    
    input_query = input("Search for something about programming: ")

    # Get search results
    results = search_query(input_query)

    # Get the first result from each site
    filtered_results = get_first_result_per_site(results, allowed_sites)
    
    if filtered_results:
        print("Opening the following URLs in your browser:")
        for url in filtered_results:
            print(url)
        open_browser(filtered_results)
    else:
        print("No matching results found.")

if __name__ == "__main__":
    main()
