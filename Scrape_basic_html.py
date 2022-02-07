import csv
from requests_html import HTMLSession

s = HTMLSession()


def get_product_link(page):
    url = f"https://themes.woocommerce.com/storefront/product-category/clothing/page/{page}"
    link = []
    r = s.get(url)
    products = r.html.find("ul.product li")
    for item in products:
        link.append(item.find("a", first=True).attrs['href'])
    return link


def parse_product(url):
    r = s.get(url)
    title = r.html.find("h1.product_title.entry-title", first = True).text.strip()
    price = r.html.find("p.price", first=True).text.strip().replace("\n", " ")
    cat = r.html.find("span.posted_in", find=True).text.strip()
    try:
        sku = r.html.find("span.sku", first=True).text.strip()
    except AttributeError as err:
        sku = "None"
        # print(sku)

    product = {
        "title": title,
        "price": price,
        "sku" : sku,
        "cat": cat
    }
    return product


def save_csv(result):
    keys = result[0].key()

    with open("product.csv", "w") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(result)


def main():
    result = []
    for x in range(1, 5):
        print("Getting page", x)
        urls = get_product_link(x)
        for url in urls:
            result.append(parse_product(url))
        print("Total result", len(result))
        save_csv(result)


if __name__ == "__main__":
    main()
