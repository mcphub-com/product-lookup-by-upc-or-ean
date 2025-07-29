import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/go-upc-go-upc-default/api/product-lookup-by-upc-or-ean'

mcp = FastMCP('product-lookup-by-upc-or-ean')

@mcp.tool()
def product_by_barcode(code: Annotated[str, Field(description='')]) -> dict: 
    '''Retrieves product data based on the given barcode. Supports the following fomats: UPC, EAN, GTIN, ISBN.'''
    url = 'https://product-lookup-by-upc-or-ean.p.rapidapi.com/code/829576019311'
    headers = {'x-rapidapi-host': 'product-lookup-by-upc-or-ean.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'code': code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
