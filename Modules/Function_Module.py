from pandas import DataFrame
class Func:
    def __init__(self, product_list: list):
        self.product_list = product_list
        self.full_list = product_list
    
    def sort_by_name(self) -> None:
        self.product_list.sort(key=lambda product: product.name)
    
    def sort_by_price(self) -> None:
        self.product_list.sort(key=lambda product: product.curr_price)
    
    def sort_by_discount(self) -> None:
        self.product_list.sort(key=lambda product: product.discount, reverse=True)
    
    def get_product_list(self) -> list:
        return self.product_list
    
    def filter_by_name(self, name: str) -> list:
        return [product for product in self.product_list if name in product.name]

    def filter_by_price(self, price: float) -> list:
        return [product for product in self.product_list if price == product.curr_price]
    
    def filter_by_discount(self, discount: int) -> list:
        return [product for product in self.product_list if discount == product.discount]
    
    def filter_by_price_range(self, min_price: float, max_price: float) -> list:
        return [product for product in self.product_list if min_price <= product.curr_price <= max_price]
    
    def filter_by_discount_range(self, min_discount: int, max_discount: int) -> list:
        return [product for product in self.product_list if min_discount <= product.discount <= max_discount]
    
    def export_to_excel(self, file_name: str = 'products.xlsx'):
        df = DataFrame([product.to_dict() for product in self.product_list])
        df.to_excel(f'{file_name}.xlsx')

    def export_to_csv(self, file_name: str = 'products.xlsx'):
        df = DataFrame([product.to_dict() for product in self.product_list])
        df.to_csv(f'{file_name}.csv')
