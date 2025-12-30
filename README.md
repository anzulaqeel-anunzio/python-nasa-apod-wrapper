# NASA APOD Wrapper (Python)

A simple Python wrapper for the NASA Astronomy Picture of the Day (APOD) API.

## Features

-   **Easy Access**: Fetch APOD data with a single method call.
-   **Date Range**: Support for fetching images within a date range.
-   **Random Images**: Fetch random APOD images (count supported).
-   **Lightweight**: Minimal dependencies (only `requests`).

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install Package (Optional)**
    ```bash
    pip install .
    ```

## Usage

```python
import os
from nasa_apod import ApodClient
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

client = ApodClient(api_key=api_key)

# Get today's APOD
today = client.get_today()
print(f"Title: {today['title']}")
print(f"URL: {today['url']}")

# Get random APODs
random_snaps = client.get_random(count=3)
for snap in random_snaps:
    print(f"Random Title: {snap['title']}")
```

## Configuration

Obtain an API Key from [api.nasa.gov](https://api.nasa.gov/).

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
