from typing import Any, Dict, Optional

import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class HttpClient:
    """HTTP client wrapper providing a configured requests.Session with retries."""

    def __init__(
        self,
        *,
        timeout_seconds: float = 10.0,
        total_retries: int = 3,
        backoff_factor: float = 0.5,
    ) -> None:
        self._timeout_seconds = timeout_seconds
        self._session = requests.Session()

        retry = Retry(
            total=total_retries,
            connect=total_retries,
            read=total_retries,
            backoff_factor=backoff_factor,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=(
                "HEAD",
                "GET",
                "OPTIONS",
            ),
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)

        # Default headers can be extended by callers if needed
        self._session.headers.update({
            "Accept": "application/json",
            "User-Agent": "mairui-client/1.0 (+python-requests)",
        })

    def get_json(
        self,
        *,
        url: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        response = self._session.get(url, params=params, timeout=self._timeout_seconds)
        response.raise_for_status()
        return response.json()


