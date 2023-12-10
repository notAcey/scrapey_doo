from Classes.PCGarage_Scraper import PCGarage_Scraper
from Classes.OLX_Scraper import OLX_Scraper
from Classes.Altex_Scraper import Altex_Scraper
from Modules.Function_Module import Func

class UI:
    def __init__(self):
        self.scraper = None
        self.func = None

    def initialize_scraper(self, link):
        if 'altex.ro' in link:
            self.scraper = Altex_Scraper(link)
        elif 'olx.ro' in link:
            self.scraper = OLX_Scraper(link)
        elif 'pcgarage.ro' in link:
            self.scraper = PCGarage_Scraper(link)
        else:
            raise ValueError('No scraper for this site yet')
        self.func = Func(self.scraper.product_list)

    def sort_products(self, sort_type):
        if sort_type == 'name':
            self.func.sort_by_name()
        elif sort_type == 'price':
            self.func.sort_by_price()
        elif sort_type == 'discount':
            self.func.sort_by_discount()
        else:
            raise ValueError('Invalid sort type')

    def filter_products(self, filter_type, value):
        if filter_type == 'name':
            self.func.product_list = self.func.filter_by_name(value)
        elif filter_type == 'price':
            price = float(value)
            self.func.product_list = self.func.filter_by_price(price)
        elif filter_type == 'discount':
            discount = int(value)
            self.func.product_list = self.func.filter_by_discount(discount)
        elif filter_type == 'price_range':
            min_price, max_price = map(float, value.split(','))
            self.func.product_list = self.func.filter_by_price_range(min_price, max_price)
        elif filter_type == 'discount_range':
            min_discount, max_discount = map(int, value.split(','))
            self.func.product_list = self.func.filter_by_discount_range(min_discount, max_discount)
        else:
            raise ValueError('Invalid filter type')

    def export_products(self, export_type, filename):
        if export_type == 'excel':
            self.func.export_to_excel(filename)
        elif export_type == 'csv':
            self.func.export_to_csv(filename)
        else:
            raise ValueError('Invalid export type')

    def get_product_list(self):
        return [product.to_dict() for product in self.func.product_list]