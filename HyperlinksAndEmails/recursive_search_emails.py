import urllib.request
from scraper import find_urls, find_emails


def recursive_search_emails(url, depth):
    """  
    Searches for all the emails on the URL page.
    """
    def recursive_search_URL(url, depth, visit=[]):
        """
        Inner function to search recursively and save the visited URL's.
        """
        if depth < 1:
            raise ValueError("The depth has to be 1 or higher.")
        cont = ""
        try:
            cont = str(urllib.request.urlopen(url).read())
        except:
            return [], visit
        # Find all the email addresses in the content
        email_addresses = find_emails(cont)
        
        # If depth is higher than 1 then search the content of all the links
        if depth > 1:
            for found_url in find_urls(cont):
                # Searching through each linkonce
                if found_url not in visit:
                    visit.append(found_url)
                    print(found_url)
                    # recursively search this function
                    found_email_address, visited_urls = recursive_search_URL(found_url, depth - 1, visit)
                    email_addresses = email_addresses + found_email_address
                    visit = visited_urls
        return list(set(email_addresses)), visit
    # Call the inner function and only return the addresses and not the links
    return recursive_search_URL(url, depth)[0]

if __name__ == "__main__":
    email_addresses = recursive_search_emails(r"""http://www.uio.no/studier/emner/matnat/ifi/INF3331/h17/oppgaver.html""", 2)
    # Save the adresses to a text file for fun
    with open("addresses.txt", "w") as address_list:
        for address in email_addresses:
            address_list.write(address + "\n")
    print("\nNumer of email addresses found: {}.".format(len(email_addresses)))
    print(email_addresses)
    print("The addresses are written to addresses.txt")
