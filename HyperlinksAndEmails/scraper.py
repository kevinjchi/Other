import re

def find_emails(text):
    """ 
    Finds an email-like substring of the form NAME@SERVER.DOMAIN
    and returns a list of email-like substrings.
    """
    email_list = []
    NAME = r"[\w\d.#$%&~'*+\-\/=\?_`|{}]+"
    SERVER = r"[\w\d.#$%&~'*+\-\/=?_`|{}]+"
    DOMAIN = r"[a-zA-Z][\w\.]{0,}[a-zA-Z]"
    regex = NAME + r"@" + SERVER + r"\." + DOMAIN
    emails = re.findall(regex,text)
    for email in emails:
        email_list.append(email)
    return email_list


def find_hyperlinks(text):
    """
    Searching though the html string given as an input parameter using the
    regular expression to find the URL
    
    <a href="PROTOCOL://www.HOST.DOMAIN/PATH"></a>
    <a href="PROTOCOL://HOST.DOMAIN/PATH"> </a>
    <a href=’PROTOCOL://www.HOST.DOMAIN/PATH’></a>
    <a href=’PROTOCOL://HOST.DOMAIN/PATH’></a>

    PROTOCOL is http or https.
    HOST and DOMAIN are alphanumeric characters or any of . - ~
    PATH is alphanumeric or any of / . - ~

    URL's are returned.
    """
    HOST = r"[\w\.\-~]"
    DOMAIN = r"[\w\.\-~]"
    PATH = r"[\w\.\-/~\?=\(\)]"

    # .*? non-greedy matcher
    regex = r"""<a.*?href=(["'])((?:http|https)://(?:www.)?""" + HOST + r"+." + DOMAIN + r"+/" + PATH + r"*)\1.*?>.*?</a>"
    matches = re.findall(regex, text)

    #Collect values
    hyperlinks = [match[1] for match in matches]
    return hyperlinks


def find_urls(text):
    """
    If this find_hyperlinks is imported instead of find_urls
    """
    return find_hyperlinks(text)