# پروژه چهارم
# موجودی یک فروشگاه
# یک تابع برای گرفتن اطلاعات محصول بسازی.
# تعداد محصولات اولیه رو از کاربر بگیری.
# با for همه محصولات رو بسازی.
# داخل products ذخیره‌شون کنی.
# آخرش products رو چاپ کنی.
def goods(name= None):
    if name is None:
        name=input("name : ").strip()
    else:
        name=name.strip()
    while not name:
        print("product name cannot be empty")
        name=input("name: " ).strip()
    while True:
        try:
            count = int(input("count:"))
            if count<0:
                print("count cannot be negative ")
            else:
                break
        except ValueError:
            print("please enter a valid integer")
    while True:
        try:
            price = int(input("price in Toomans >>>"))
            if price <0:
                print("price cannot be negative")
            else:
                break
        except ValueError:
            print("please enter a valid integer")
    products = {
        "name": name,
        "price": price,
        "count": count
    }
    return products


list_of_products = {}
# تعداد محصولات اولیه
while True:
    try:
        i = int(input("how many products exists ? >>>"))
        if i <0:
            print("number of products cannot be negative")
        else:
            break
    except ValueError:
        print("please enter a valid integer")
for number in range(i):
    thing = goods()
    while thing["name"] in list_of_products:
        print("this product already exists")
        thing=goods()
    list_of_products[thing["name"]] = thing
print(list_of_products)

print("menu: add , search , show products , exit")
while True:
    search = input("search here...shoose from menu : ")
    # add
    if search.lower() == "add product":
        product_name=input("enter the name of product to add :").strip()
        if product_name in list_of_products:
            print("already exists")
        else:

            thing = goods(product_name)
            list_of_products[thing["name"]] = thing
        
# search
    elif search.lower() == "search":
        name = input("which product are you looking for ? ...").strip()
        if name in list_of_products:
            print(list_of_products[name])
        else:
            print("not found")

    # show products

    elif search.lower() == "show products":
        print(list_of_products)
# exit
    elif search.lower() == "exit":
        print("exiting...")
        break
    else:
        print("Not Found")
