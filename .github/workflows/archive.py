import savepagenow
import time

URLS = [
    "https://robey100.com",
    "https://defacube.serv00.net/RDHV/",
    "https://defacube.serv00.net/IRCED/",
    "https://defacube.serv00.net/ucp/",
    "https://defacube.serv00.net/sitemap.xml",
    "https://apidocs.sixteensrc.zip/"
]

def archive_url(url):
    try:
        print(f"Archiving: {url}")
        archive_url, captured = savepagenow.capture_or_cache(
            url,
            authenticate=True
        )

        if captured:
            print(f"Fresh capture: {archive_url}")
        else:
            print(f"Cached version used: {archive_url}")

        time.sleep(5)  # prevent rate limiting

    except Exception as e:
        print(f"Failed: {url} -> {e}")


for url in URLS:
    archive_url(url)

print("Done.")
