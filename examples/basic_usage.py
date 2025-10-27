from mairui_client import MairuiClient


def main() -> None:
    # Reads MAIRUI_LICENSE from environment, optionally from .env
    client = MairuiClient.from_env()

    # 1) Basic list
    stocks = client.stock_list()
    print(f"Stocks: {len(stocks)} items (showing first 3)")
    print(stocks[:3])

    # 2) Realtime snapshot (public data source)
    rt = client.realtime_trade_public("000001")
    print("Realtime public for 000001:", rt)

    # 3) Latest daily bars (use SZ by default if market not provided)
    latest = client.latest_bars(stock_code="000001", level="d", adj="n", latest_count=1)
    print("Latest daily bar for 000001.SZ:", latest)


if __name__ == "__main__":
    main()


