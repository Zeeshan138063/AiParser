import requests

from pydantic import BaseModel

from oxyparser.oxyparser import OxyParser


class ProductItem(BaseModel):
    title: str
    price: str
    # rating:float
    review_count: str
    delivery: str
    about: str


URL: str = "https://www.ebay.com/itm/285683170025"


async def main() -> None:
    parser = OxyParser()
    html = requests.get(URL).text
    job_item = await parser.parse(URL, ProductItem, html=html)
    print(job_item)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
