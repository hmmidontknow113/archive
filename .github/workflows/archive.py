import savepagenow
import time

BASE_URL = "https://robey100.com"

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


archive_url(BASE_URL)

print("Done.")
