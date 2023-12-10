from bs4 import BeautifulSoup
from selenium import webdriver
from Classes.Product_Class import Product

class Altex_Scraper():
    def __init__(self, altex_link: str) -> None:
        self.name = 'Altex'
        self.altex_link = altex_link
        self.page_nr = 1
        self.raw_product_list = self.get_raw_product_list(altex_link)
        self.product_list = self.get_product_list(self.raw_product_list)
    
    def get_page_raw_product_list(self, altex_link: str) -> list:
        url = altex_link
        driver = webdriver.Edge()
        driver.get(url)
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        raw_page_product_list = soup.find('ul', {'class': 'Products flex flex-wrap relative -mx-1 sm:-mx-2'})
        if not raw_page_product_list:
            raise Exception('Error: This page cannot be scraped, try another one')
        raw_page_product_list = raw_page_product_list.find_all('li', {'class': 'Products-item w-1/2 sm:w-1/3 p-1 sm:p-2 border-transparent md:border-2 min-h-330px lg:min-h-400px bg-white lg:w-1/4'}) 

        return raw_page_product_list   
    
    def get_raw_product_list(self, altex_link: str) -> list:
        raw_product_list = []
        next_page_link = altex_link
        while next_page_link:
            raw_product_list.extend(self.get_page_raw_product_list(next_page_link))
            next_page_link = self.get_next_page_link(next_page_link)
        return raw_product_list
    
    def get_product_list(self, raw_product_list: list) -> list:
        product_list = []
        for product_li in raw_product_list:
            product_div = product_li.find('div', {'class': 'Product'})

            in_stock = product_div.find(string="in stoc")
            if not in_stock:
                continue

            name = product_div.find('span', {'class': 'Product-name Heading leading-20 text-sm min-h-[68px] line-clamp-3 max-h-[68px]'}).text.strip()

            prices = product_div.find_all('span', {'class': 'Price-int leading-none'})
            if len(prices) == 2:
                price = float(prices[1].text.strip().replace('.', '').replace(',', '.'))
                full_price = float(prices[0].text.strip().replace('.', '').replace(',', '.'))
            else:
                price = float(prices[0].text.strip().replace('.', '').replace(',', '.'))
                full_price = price

            product_link = product_div.find('a')['href']
            link = "https://altex.ro" + product_link

            product_list.append(Product(name, price, full_price, link))

        return product_list

    
    def get_next_page_link(self, altex_link: str) -> str:
        url = altex_link
        print(f'Getting products from page {self.page_nr}')
        self.page_nr += 1
        driver = webdriver.Edge()
        driver.get(url)
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        next_page_link = soup.find_all('a', {'class': 'inline-block py-1 px-2 mx-0.5 sm:mx-1 text-sm border border-gray-1100 rounded-md items-center text-center bg-white'})
        if not next_page_link:
            return None
        elif next_page_link[-1].text.strip() == 'Pagina urmatoare':
            next_page_link = next_page_link[-1].get('href')
        else:
            return None
        return next_page_link