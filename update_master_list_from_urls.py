import requests
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_list_content(session: requests.Session, url: str) -> str:
    """
    Fetches content from a given URL using the provided session.

    Parameters:
    - session (requests.Session): The session object to make requests.
    - url (str): The URL to fetch content from.

    Returns:
    - str: The content fetched from the URL.
    """
    try:
        response = session.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to fetch content from {url}: {e}")
        raise

def update_master_list(urls: list[str], master_file_path: str) -> None:
    """
    Updates the master list file with content fetched from the given URLs.

    Parameters:
    - urls (list[str]): A list of URLs to fetch content from.
    - master_file_path (str): Path to the master file to be updated.
    """
    try:
        with requests.Session() as session, open(master_file_path, 'w') as master_file:
            for url in urls:
                content = fetch_list_content(session, url)
                master_file.write(content + "\n\n")
    except Exception as e:
        logging.error(f"Failed to update master list: {e}")
        raise

if __name__ == "__main__":
    urls = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Claude/Claude.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Gemini/Gemini.list"
    ]
    master_file_path = "master.list"
    try:
        update_master_list(urls, master_file_path)
    except Exception as e:
        logging.error(f"Script execution failed: {e}")
