from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional
import os

from .http import HttpClient


API_HOST = "https://api.mairuiapi.com"
ALT_HOST = "https://a.mairuiapi.com"


class MairuiClient:
    """High-level client for MaiRui stock APIs.

    Parameters
    ----------
    license_key: str
        Your MaiRui API license string placed in path segments.
    timeout_seconds: float
        Per-request timeout.
    total_retries: int
        Total retries for transient errors.
    backoff_factor: float
        Backoff factor used by urllib3 Retry.
    base_host: str
        Base host for standard endpoints. Defaults to api.mairuiapi.com (HTTPS).
    alt_host: str
        Alternate host used by certain "all" endpoints.
    """

    def __init__(
        self,
        *,
        license_key: str,
        timeout_seconds: float = 10.0,
        total_retries: int = 3,
        backoff_factor: float = 0.5,
        base_host: str = API_HOST,
        alt_host: str = ALT_HOST,
    ) -> None:
        if not license_key or not isinstance(license_key, str):
            raise ValueError("license_key must be a non-empty string")
        self._license_key = license_key
        self._http = HttpClient(
            timeout_seconds=timeout_seconds,
            total_retries=total_retries,
            backoff_factor=backoff_factor,
        )
        self._base_host = base_host.rstrip("/")
        self._alt_host = alt_host.rstrip("/")

    # ---------- Construction helpers ----------

    @classmethod
    def from_env(
        cls,
        *,
        env_var: str = "MAIRUI_LICENSE",
        use_dotenv: bool = True,
        dotenv_path: Optional[str] = None,
        timeout_seconds: float = 10.0,
        total_retries: int = 3,
        backoff_factor: float = 0.5,
        base_host: str = API_HOST,
        alt_host: str = ALT_HOST,
    ) -> "MairuiClient":
        """Create client from environment variable, optionally loading a .env file.

        Parameters
        ----------
        env_var: str
            The environment variable name that holds the licence (default MAIRUI_LICENSE).
        use_dotenv: bool
            If True, attempt to load variables from a .env file.
        dotenv_path: Optional[str]
            Path to .env file. If None, load from default search location.
        """
        if use_dotenv:
            try:
                from dotenv import load_dotenv
                load_dotenv(dotenv_path=dotenv_path)
            except Exception:
                # Proceed even if dotenv is not installed or load fails
                pass
        license_key = os.environ.get(env_var)
        if not license_key:
            raise RuntimeError(f"Environment variable '{env_var}' is not set")
        return cls(
            license_key=license_key,
            timeout_seconds=timeout_seconds,
            total_retries=total_retries,
            backoff_factor=backoff_factor,
            base_host=base_host,
            alt_host=alt_host,
        )

    # ---------- Helpers ----------

    def _url(self, *parts: str, use_alt: bool = False) -> str:
        base = self._alt_host if use_alt else self._base_host
        clean_parts = [p.strip("/") for p in parts if p]
        return f"{base}/" + "/".join(clean_parts)

    @staticmethod
    def _join_codes(stock_codes: Iterable[str]) -> str:
        codes = [c.strip() for c in stock_codes if c and c.strip()]
        if not codes:
            raise ValueError("stock_codes must contain at least one code")
        return ",".join(codes)

    @staticmethod
    def _code_with_market(stock_code: str, market: Optional[str] = None) -> str:
        code = stock_code.strip()
        if not code:
            raise ValueError("stock_code must be a non-empty string")
        if "." in code:
            return code
        if market is None:
            # Caller should supply market if needed; defaulting to SZ is safer for common A-shares like 000001
            return f"{code}.SZ"
        return f"{code}.{market.upper()}"

    # ---------- Basic lists ----------

    def stock_list(self) -> Any:
        return self._http.get_json(url=self._url("hslt", "list", self._license_key))

    def new_stock_calendar(self) -> Any:
        return self._http.get_json(url=self._url("hslt", "new", self._license_key))

    # ---------- Index/Industry/Concept tree ----------

    def index_industry_concept_tree(self) -> Any:
        return self._http.get_json(url=self._url("hszg", "list", self._license_key))

    def stocks_by_index_code(self, code: str) -> Any:
        code_clean = code.strip()
        if not code_clean:
            raise ValueError("code must be a non-empty string")
        return self._http.get_json(url=self._url("hszg", "gg", code_clean, self._license_key))

    def concepts_by_stock(self, stock_code: str) -> Any:
        code_clean = stock_code.strip()
        if not code_clean:
            raise ValueError("stock_code must be a non-empty string")
        return self._http.get_json(url=self._url("hszg", "zg", code_clean, self._license_key))

    # ---------- Thematic pools ----------

    def limit_up_pool(self, date_yyyy_mm_dd: str) -> Any:
        return self._http.get_json(url=self._url("hslt", "ztgc", date_yyyy_mm_dd, self._license_key))

    def limit_down_pool(self, date_yyyy_mm_dd: str) -> Any:
        return self._http.get_json(url=self._url("hslt", "dtgc", date_yyyy_mm_dd, self._license_key))

    def strong_stock_pool(self, date_yyyy_mm_dd: str) -> Any:
        return self._http.get_json(url=self._url("hslt", "qsgc", date_yyyy_mm_dd, self._license_key))

    def new_stock_pool(self, date_yyyy_mm_dd: str) -> Any:
        return self._http.get_json(url=self._url("hslt", "cxgc", date_yyyy_mm_dd, self._license_key))

    def broken_limit_pool(self, date_yyyy_mm_dd: str) -> Any:
        return self._http.get_json(url=self._url("hslt", "zbgc", date_yyyy_mm_dd, self._license_key))

    # ---------- Realtime and ticks ----------

    def realtime_trade_public(self, stock_code: str) -> Any:
        return self._http.get_json(url=self._url("hsrl", "ssjy", stock_code, self._license_key))

    def tick_trades_today(self, stock_code: str) -> Any:
        return self._http.get_json(url=self._url("hsrl", "zbjy", stock_code, self._license_key))

    def realtime_trade_broker(self, stock_code: str) -> Any:
        return self._http.get_json(url=self._url("hsstock", "real", "time", stock_code, self._license_key))

    def order_book_five(self, stock_code: str) -> Any:
        return self._http.get_json(url=self._url("hsstock", "real", "five", stock_code, self._license_key))

    def realtime_trade_all_broker(self) -> Any:
        # All stocks real-time (broker source) on alternate host
        return self._http.get_json(url=self._url("hsrl", "ssjy", "all", self._license_key, use_alt=True))

    def realtime_trade_multi(self, stock_codes: Iterable[str]) -> Any:
        params = {"stock_codes": self._join_codes(stock_codes)}
        return self._http.get_json(url=self._url("hsrl", "ssjy_more", self._license_key), params=params)

    def realtime_trade_all_public(self) -> Any:
        # All stocks real-time (public/net source) on alternate host
        return self._http.get_json(url=self._url("hsrl", "real", "all", self._license_key, use_alt=True))

    # ---------- Money flow ----------

    def money_flow_history(
        self,
        *,
        stock_code: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        latest_count: Optional[int] = None,
    ) -> Any:
        params: Dict[str, Any] = {}
        if start_date:
            params["st"] = start_date
        if end_date:
            params["et"] = end_date
        if latest_count is not None:
            params["lt"] = int(latest_count)
        return self._http.get_json(
            url=self._url("hsstock", "history", "transaction", stock_code, self._license_key),
            params=params or None,
        )

    # ---------- Bars and indicators ----------

    def latest_bars(
        self,
        *,
        stock_code: str,
        market: Optional[str] = None,
        level: str = "d",
        adj: str = "n",
        latest_count: Optional[int] = None,
    ) -> Any:
        code_market = self._code_with_market(stock_code, market)
        params = {"lt": int(latest_count)} if latest_count is not None else None
        return self._http.get_json(url=self._url("hsstock", "latest", code_market, level, adj, self._license_key), params=params)

    def history_bars(
        self,
        *,
        stock_code: str,
        market: Optional[str] = None,
        level: str = "d",
        adj: str = "n",
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        latest_count: Optional[int] = None,
    ) -> Any:
        code_market = self._code_with_market(stock_code, market)
        params: Dict[str, Any] = {}
        if start_time:
            params["st"] = start_time
        if end_time:
            params["et"] = end_time
        if latest_count is not None:
            params["lt"] = int(latest_count)
        return self._http.get_json(
            url=self._url("hsstock", "history", code_market, level, adj, self._license_key),
            params=params or None,
        )

    def stop_price_history(
        self,
        *,
        stock_code: str,
        market: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Any:
        code_market = self._code_with_market(stock_code, market)
        params: Dict[str, Any] = {}
        if start_date:
            params["st"] = start_date
        if end_date:
            params["et"] = end_date
        return self._http.get_json(
            url=self._url("hsstock", "stopprice", "history", code_market, self._license_key),
            params=params or None,
        )

    def indicators(
        self,
        *,
        stock_code: str,
        market: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Any:
        code_market = self._code_with_market(stock_code, market)
        params: Dict[str, Any] = {}
        if start_date:
            params["st"] = start_date
        if end_date:
            params["et"] = end_date
        return self._http.get_json(
            url=self._url("hsstock", "indicators", code_market, self._license_key),
            params=params or None,
        )

    # ---------- Technicals ----------

    def history_macd(
        self,
        *,
        stock_code: str,
        market: Optional[str] = None,
        level: str = "d",
        adj: str = "n",
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        latest_count: Optional[int] = None,
    ) -> Any:
        code_market = self._code_with_market(stock_code, market)
        params: Dict[str, Any] = {}
        if start_time:
            params["st"] = start_time
        if end_time:
            params["et"] = end_time
        if latest_count is not None:
            params["lt"] = int(latest_count)
        return self._http.get_json(
            url=self._url("hsstock", "history", "macd", code_market, level, adj, self._license_key),
            params=params or None,
        )

    def history_ma(
        self,
        *,
        stock_code: str,
        market: Optional[str] = None,
        level: str = "d",
        adj: str = "n",
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        latest_count: Optional[int] = None,
    ) -> Any:
        code_market = self._code_with_market(stock_code, market)
        params: Dict[str, Any] = {}
        if start_time:
            params["st"] = start_time
        if end_time:
            params["et"] = end_time
        if latest_count is not None:
            params["lt"] = int(latest_count)
        return self._http.get_json(
            url=self._url("hsstock", "history", "ma", code_market, level, adj, self._license_key),
            params=params or None,
        )

    def history_boll(
        self,
        *,
        stock_code: str,
        market: Optional[str] = None,
        level: str = "d",
        adj: str = "n",
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        latest_count: Optional[int] = None,
    ) -> Any:
        code_market = self._code_with_market(stock_code, market)
        params: Dict[str, Any] = {}
        if start_time:
            params["st"] = start_time
        if end_time:
            params["et"] = end_time
        if latest_count is not None:
            params["lt"] = int(latest_count)
        return self._http.get_json(
            url=self._url("hsstock", "history", "boll", code_market, level, adj, self._license_key),
            params=params or None,
        )

    def history_kdj(
        self,
        *,
        stock_code: str,
        market: Optional[str] = None,
        level: str = "d",
        adj: str = "n",
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        latest_count: Optional[int] = None,
    ) -> Any:
        code_market = self._code_with_market(stock_code, market)
        params: Dict[str, Any] = {}
        if start_time:
            params["st"] = start_time
        if end_time:
            params["et"] = end_time
        if latest_count is not None:
            params["lt"] = int(latest_count)
        return self._http.get_json(
            url=self._url("hsstock", "history", "kdj", code_market, level, adj, self._license_key),
            params=params or None,
        )


