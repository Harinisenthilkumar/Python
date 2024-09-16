#MODULE 1
shop_name = input("Enter the shop name: ")
print(shop_name)
print("-" * 70)
product = {
    "mobile": ["Redmi", "Vivo", "Oppo"],
    "tv": ["LG", "Samsung", "Sony"],
    "laptops": ["Dell", "HP", "Lenovo"]
}

for i,j in product.items():
    print(i,end="\t\t\t")
print()
pick1=input("pick any one:")
print("-" * 70)

for i,j in product.items():
    if i == pick1:
        print(pick1)
        for x in j :
            print(x,end="\t\t\t")

# module 2

Brands={"Redmi":{"Brandname":"redmi",
        "model Name":"NOTE 10 pro",
        "ram":"6gb",
        "Price":"20,000"
        "GST":10
        "final price":22,000
        },
        "Vivo":{"Brandname":"Vivo",
        "model Name":"Vivo Y50",
        "ram":"6gb",
        "Price":20,000
        "GST":10,
        "final price":22,000
        },
        "Oppo":{"Brandname":"Oppo",
        "model Name":"Oppo f17",
        "ram":"6gb",
        "Price:"17,000,
        "GST":10,
        "final price":19,000
        },
        "LG":{"Brandname":"LG",
        "model Name":"LQ 5",
        "ram:""6gb",
        "Price:"40,000,
        "GST":10,
        "final price":42,000
        },
        "Samsung":{"Brandname":"Samsung",
        "model Name":"Samsung pro",
        "ram":"6gb",
        "Price:"80,000,
        "GST":10,
        "final price":82,000
        },
        "Sony":{"Brandname":"Sony",
        "model Name":"Sony series",
        "ram":"6gb",
        "Price:"75,000,
        "GST":10,
        "final price":76,000
        },
        "Dell":{"Brandname":"Dell",
        "model NameDell i7",
        "ram":"6gb",
        "Price:"86,000,
        "GST":10,
        "final price":88,000
        },
        "HP":{"Brandname":"HP",
        "model Name":"HP i3",
        "ram":"6gb",
        "Price:"90,000,
        "GST":10,
        "final price":92,000
        },
        "Lenovo":{"Brandname":"Lenovo",
        "model Name":"Lenovo",
        "ram":"6gb",
        "Price:"43,000,
        "GST":10,
        "final price:"45,000
        },
        }



        





