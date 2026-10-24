# پروژه چهارم
# موجودی یک فروشگاه
# یک تابع برای گرفتن اطلاعات محصول بسازی.
# تعداد محصولات اولیه رو از کاربر بگیری.
# با for همه محصولات رو بسازی.
# داخل products ذخیره‌شون کنی.
# آخرش products رو چاپ کنی.
def goods(name= None):
    if name is None:
        name=input("name : ")
    count = int(input("count:"))
    price = int(input("price in Toomans >>>"))
    products = {
        "name": name,
        "price": price,
        "count": count
    }
    return products


list_of_products = {}
# تعداد محصولات اولیه
i = int(input("how many products exists ? >>>"))
for number in range(i):
    thing = goods()
    list_of_products[thing["name"]] = thing
print(list_of_products)

# Menue
while True:
    search = input("search here...")
    # add
    if search.lower() == "add product":
        product_name=input("enter the name of product to add :")
        if product_name in list_of_products:
            print("already exists")
        else:

            thing = goods(product_name)
            list_of_products[thing["name"]] = thing
        
# search
    elif search.lower() == "search":
        name = input("which product are you looking for ? ...")
        if name in list_of_products:
            print(list_of_products[name])

    # show products

    elif search.lower() == "show products":
        print(list_of_products)
# exit
    elif search.lower() == "exit":
        print("exiting...")
        break
    else:
        print("Not Found")
