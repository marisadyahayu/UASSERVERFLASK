from logging import error
from random import choice, choices
from click import parser
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None

class halamanhome(Resource):
    def get(seft):
        return {
            "halamanhome" : [
                {
                    "Header" : [
                        {
                            "topHeader" : [
                                {
                                    "text" : "Free shipping for standard order over $100"
                                },
                                {
                                    "text" : "Help & FAQs",
                                    "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                },
                                {
                                    "text" : "My Accout",
                                    "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                },
                                {
                                    "language" : [
                                        {
                                            "text" : "EN",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        }
                                    ]
                                },
                                {
                                    "text" : "USD",
                                    "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                }
                            ]
                        },
                        {
                            "mainHeader" : [
                                {
                                    "Left" : [
                                        {
                                            "image" : "data:image/webp;base64,UklGRqACAABXRUJQVlA4TJQCAAAvhAAEEH8gEEhy2p9vhZmZmYlI6DigvP//GUle0ztpu8e2nducPHOy7Vneam0zy8ZxbdverNU87bF1WqaVLudz+P3Sz0T0fwLAe/XN9Zj3fflICVx1owlcc+MyrFf/cYvDg77v+5Ww+de3pgH3+/6VDlf5vu/D/LykWcCHkr51GZQJpNVk8WJpIwVJmoeXl8IKyEi6g0CSHAYkKXTxYknaOJ6iQkvfsxNaQ6dxQjR7gsNAz9HLcs9C5sThl1UWnJ0wYQIU1POPVEuf9FVBPc5VN974qjrBk1RmjNVBsQKiWpgfV8HmuIJMJWRqgrMA5xSWklaKrFazOVYF0K1N0KxQVUamFg64tufeBYjmWkbm2QKdhav0LnHowojqgJwqoFdPaJ4RzcVqDG8y3rvTMpQwqDrMzXoWCLQO9ulbINIRpYygp3wcUa1x1beWsVrbiGosV+lO4CrthX6tBXJy4k6jMR/uSEpb9nUaXqEieNf3lzN6MfIqg0a9S1YuwL6/tTshM472tuKzBJLOMpSwWU3Ac9rLVXoWuEopIlUY8LNKbWOWc0ahqYTg7IQJDl1aB5u/fGS+eoA+NTCiOUCgzi/zqrORq7GN1BvNTWQqn2uC4CxAs76F73QneVVBTlUUVAoMy9wL7C+FqN4W3Gn07SVT2RiXJsyXbn8g1lxG1XnFn5J7l+4EyFieBaJ6iOps58ISIFdDppJ0TQJpmeVcJTPFoEyK4fbt2+MQ6HoWctU2snfAh6FrvHdn0lVGCkhLCssT9ulZIKty8OJHPgvdhGZ1tGkDhhe6QWdbWxvQGusZF5j/l3qWk9Css0CkauCFWKtI4GPpMcdCpiaQJAegBPsWh4vsTQZoxLplCUAj0OgwYcKECQA=",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "text" : "Home",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html",
                                            "atribut" : [
                                                {
                                                    "text" : "Homepage 1",
                                                    "url" : "https://preview.colorlib.com/theme/cozastore/index.html"
                                                },
                                                {
                                                    "text" : "Homepage 2",
                                                    "url" : "https://preview.colorlib.com/theme/cozastore/home-02.html"
                                                },
                                                {
                                                    "text" : "Homepage 3",
                                                    "url" : "https://preview.colorlib.com/theme/cozastore/home-03.html"
                                                }
                                            ]
                                        },
                                        {
                                            "text" : "Shop",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/product.html"
                                        },
                                        {
                                            "text" : "Feature",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/shoping-cart.html"
                                        },
                                        {
                                            "text" : "Blog",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/blog.html"
                                        },
                                        {
                                            "text" : "About",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/about.html"
                                        },
                                        {
                                            "text" : "Contact",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/contact.html"
                                        }
                                    ],
                                    "Right" : [
                                        {
                                            "icon" : "search",
                                            "type" : "button-click",
                                            "defaultValue" : null,
                                            "popup" : [
                                                {
                                                    "placeholder" : "Search...",
                                                    "icon" : "search"
                                                }
                                            ]
                                        },
                                        {
                                            "icon" : "cart",
                                            "type" : "button-click",
                                            "qty" : 3,
                                            "cartItem" : [
                                                {
                                                    "text" : "YOUR CART",
                                                    "icon" : "cross",
                                                    "type" : "button-click"
                                                },
                                                {
                                                    "id" : 1,
                                                    "name" : "White Shirt Pleat",
                                                    "image" : "data:image/webp;base64,UklGRn4EAABXRUJQVlA4IHIEAAD…f6B2I41xQGT2nLVkVyY/uzHOvm+e0JPf6h1jnZBJndEjcugAA",
                                                    "price" : "19.00",
                                                    "type" : "Shirt",
                                                    "qty" : 1
                                                },
                                                {
                                                    "id" : 2,
                                                    "name" : "Converse All Star",
                                                    "image" : "data:image/webp;base64,UklGRnoCAABXRUJQVlA4IG4CAAD…TU9YIuM9qUzkCQpyPLBkjPQOOkVE2nPNPeahAuvsiHKriZ0AA",
                                                    "price" : "39.00",
                                                    "type" : "Shoes",
                                                    "qty" : 1
                                                },
                                                {
                                                    "id" : 3,
                                                    "name" : "Nixon Porter Leather",
                                                    "image" : "data:image/webp;base64,UklGRs4DAABXRUJQVlA4IMIDAAD…fOxhUc0OkuPowqthuT/olxlP5Xv/8DNEw4PaB6o93/R0AAA==",
                                                    "price" : "17.00",
                                                    "type" : "Watches",
                                                    "qty" : 1
                                                },
                                                {
                                                    "text" : "Total: $75.00",
                                                    "qty_total" : 3
                                                },
                                                {
                                                    "text" : "VIEW CART",
                                                    "url" : "https://preview.colorlib.com/theme/cozastore/shoping-cart.html"
                                                },
                                                {
                                                    "text" : "CHECK OUT",
                                                    "url" : "https://preview.colorlib.com/theme/cozastore/shoping-cart.html"
                                                }
                                            ]
                                        },
                                        {
                                            "icon" : "love",
                                            "type" : "button-click",
                                            "value" : null
                                        }
                                    ]
                                } 
                            ]
                        }
                    ],
                    "Body" : [
                        {
                            "Banner" : [
                                {
                                    "text" : "Women Collection 2018",
                                    "title" : "NEW SEASON",
                                    "image" : "images/xslide-01.jpg.pagespeed.ic.XotvXKn0Mi.webp",
                                    "button" : [
                                        {
                                            "text" : "SHOP NOW ",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/product.html"
                                        }
                                    ]
                                },
                                {
                                    "text" : "Men New-Season",
                                    "title" : "JACKETS & COATS",
                                    "image" : "images/xslide-02.jpg.pagespeed.ic.__MQeyG5T4.webp",
                                    "button" : [
                                        {
                                            "text" : "SHOP NOW ",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/product.html"
                                        }
                                    ]
                                },
                                {
                                    "text" : "Men Collection 2018",
                                    "title" : "NEW ARRIVALS",
                                    "image" : "images/xslide-03.jpg.pagespeed.ic.tP-L47NU9M.webp",
                                    "button" : [
                                        {
                                            "text" : "SHOP NOW ",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/product.html"
                                        }
                                    ]
                                }
                            ],
                            "rekomendasi" : [
                                {
                                    "title" : "Women",
                                    "text" : "Spring 2018",
                                    "image" : "	https://preview.colorlib.com/theme/cozastore/images/xbanner-01.jpg.pagespeed.ic.Uj5FE94mgU.webp",
                                    "button" : [
                                        {
                                            "text" : "SHOP NOW",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/product.html"
                                        }
                                    ]
                                },
                                {
                                    "title" : "Men",
                                    "text" : "Spring 2018",
                                    "image" : "		https://preview.colorlib.com/theme/cozastore/images/xbanner-02.jpg.pagespeed.ic.MQuZq6F18q.webp",
                                    "button" : [
                                        {
                                            "text" : "SHOP NOW",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/product.html"
                                        }
                                    ]
                                },
                                {
                                    "title" : "Accessories",
                                    "text" : "New Trend",
                                    "image" : "	https://preview.colorlib.com/theme/cozastore/images/xbanner-03.jpg.pagespeed.ic.1rqLomOaMb.webp",
                                    "button" : [
                                        {
                                            "text" : "SHOP NOW",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/product.html"
                                        }
                                    ]
                                }
                            ],
                            "produk" : [
                                {
                                    "title" : "PRODUCT OVERVIEW",
                                    "filter" : [
                                        {
                                            "beforeClick" : [
                                                {
                                                    "icon" : "icon-filter",
                                                    "text" : "Filter"
                                                }
                                            ],
                                            "afterClick" : [
                                                {
                                                    "icon" : "icon-close",
                                                    "text" : "Filter"
                                                },
                                                {
                                                    "sortby" : [
                                                        {
                                                            "title" : "Sort By"
                                                        },
                                                        {
                                                            "text" : "Default",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Popularity",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Average rating",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Newness",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Price:Low to High",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Price:High to Low",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        }
                                                    ],
                                                    "price" : [
                                                        {
                                                            "title" : "Price"
                                                        },
                                                        {
                                                            "text" : "All",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "$0.00-$50.00",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "$50.00-$100.00",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "$100.00-$150.00",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "$150.00-$200.00",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "$200.00-",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        }
                                                    ],
                                                    "color" : [
                                                        {
                                                            "title" : "Color"
                                                        },
                                                        {
                                                            "icon" : "circle-black",
                                                            "text" : "Black",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "icon" : "circle-blue",
                                                            "text" : "Blue",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "icon" : "circle-grey",
                                                            "text" : "Grey",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "icon" : "circle-green",
                                                            "text" : "Green",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "icon" : "circle-red",
                                                            "text" : "Red",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "icon" : "circle-white",
                                                            "text" : "White",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        }
                                                    ],
                                                    "tags" : [
                                                        {
                                                            "title" : "Tags"
                                                        },
                                                        {
                                                            "text" : "Fashion",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Lifestyle",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Denim",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Streetstyle",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        },
                                                        {
                                                            "text" : "Craft",
                                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ],
                                    "search" : [
                                        {
                                            "beforeClick" : [
                                                {
                                                    "icon" : "icon-search",
                                                    "text" : "Search",
                                                }
                                            ],
                                            "afterClick" : [
                                                {
                                                    "icon" : "icon-close",
                                                    "text" : "Search",
                                                    "dropdown" : [
                                                        {
                                                            "icon" : "icon-search",
                                                            "placeholder" : "Search"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                        
                                    ],
                                    "listproduct" : [
                                        {
                                            "text" : "All Product",
                                            "isiproduk" : [
                                                {                                
                                                    "id": "01",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                                                    "name" : "Esprit Ruffle Shirt",
                                                    "price" : "16.64"
                                                },
                                                {
                                                    "id": "02",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                                                    "name" : "Herschel supply",
                                                    "price" : "35.31"
                                                },
                                                {
                                                    "id": "03",
                                                    "type" : "men",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                                                    "name" : "Only Check Trouser",
                                                    "price" : "25.50"
                                                },
                                                {
                                                    "id": "04",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                                                    "name" : "Classic Trench Coat",
                                                    "price" : "75.00"
                                                },
                                                {
                                                    "id": "05",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                                                    "name" : "Front Pocket Jumper",
                                                    "price" : "34.75"
                                                },
                                                {
                                                    "id": "06",
                                                    "type" : "watches",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                                                    "name" : "Vintage Inspired Classic",
                                                    "price" : "93.20"
                                                },
                                                {
                                                    "id": "07",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                                                    "name" : "Shirt in Stretch Cotton",
                                                    "price" : "52.66"
                                                },
                                                {
                                                    "id": "08",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                                                    "text" : "Pieces Metallic Printed",
                                                    "price" : "18.96"
                                                },
                                                {
                                                    "id": "09",
                                                    "type" : "shoes",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                                                    "text" : "Converse All Star Hi Plimsolls",
                                                    "price" : "75.00"
                                                },
                                                {
                                                    "id": "10",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                                                    "text" : "Femme T-Shirt In Stripe",
                                                    "price" : "25.85"
                                                },
                                                {
                                                    "id": "11",
                                                    "type" : "men",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-11.jpg.pagespeed.ic.fJxJBqHZzv.webp",
                                                    "text" : "Herschel supply",
                                                    "price" : "63.16"
                                                },
                                                {
                                                    "id": "12",
                                                    "type" : "men",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                                    "text" : "Herschel supply",
                                                    "price" : "63.15"
                                                },
                                                {
                                                    "id": "13",
                                                    "type" : "men",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                                    "text" : "Herschel supply",
                                                    "price" : "63.15"
                                                },
                                                {
                                                    "id": "12",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                                                    "text" : "T-Shirt with Sleeve",
                                                    "price" : "18.49"
                                                },
                                                {
                                                    "id": "13",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                                                    "text" : "Pretty Little Thing",
                                                    "price" : "54.79"
                                                },
                                                {
                                                    "id": "14",
                                                    "type" : "watches",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                                                    "text" : "Mini Silver Mesh Watch",
                                                    "price" : "86.85"
                                                },
                                                {
                                                    "id": "15",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-16.jpg.pagespeed.ic.AbLwZITYaU.webp",
                                                    "text" : "Square Neck Back",
                                                    "price" : "29.64"
                                                }
                                            ]
                                        },
                                        {
                                            "text" : "Women",
                                            "isiproduk" : [
                                                {                                
                                                    "id": "01",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                                                    "name" : "Esprit Ruffle Shirt",
                                                    "price" : "16.64"
                                                },
                                                {
                                                    "id": "02",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                                                    "name" : "Herschel supply",
                                                    "price" : "35.31"
                                                },
                                                {
                                                    "id": "04",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                                                    "name" : "Classic Trench Coat",
                                                    "price" : "75.00"
                                                },
                                                {
                                                    "id": "05",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                                                    "name" : "Front Pocket Jumper",
                                                    "price" : "34.75"
                                                },
                                                {
                                                    "id": "07",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                                                    "name" : "Shirt in Stretch Cotton",
                                                    "price" : "52.66"
                                                },
                                                {
                                                    "id": "08",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                                                    "text" : "Pieces Metallic Printed",
                                                    "price" : "18.96"
                                                },
                                                {
                                                    "id": "10",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                                                    "text" : "Femme T-Shirt In Stripe",
                                                    "price" : "25.85"
                                                },
                                                {
                                                    "id": "12",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                                                    "text" : "T-Shirt with Sleeve",
                                                    "price" : "18.49"
                                                },
                                                {
                                                    "id": "13",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                                                    "text" : "Pretty Little Thing",
                                                    "price" : "54.79"
                                                },
                                                {
                                                    "id": "15",
                                                    "type" : "women",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-16.jpg.pagespeed.ic.AbLwZITYaU.webp",
                                                    "text" : "Square Neck Back",
                                                    "price" : "29.64"
                                                }
                                            ]
                                        },
                                        {
                                            "text" : "Men",
                                            "isiproduk" : [
                                                 {
                                                    "id": "03",
                                                    "type" : "men",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                                                    "name" : "Only Check Trouser",
                                                    "price" : "25.50"
                                                },
                                                {
                                                    "id": "12",
                                                    "type" : "men",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                                    "text" : "Herschel supply",
                                                    "price" : "63.15"
                                                },
                                                {
                                                    "id": "13",
                                                    "type" : "men",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                                    "text" : "Herschel supply",
                                                    "price" : "63.15"
                                                }
                                            ]
                                        },
                                        {
                                            "text" : "Bag"
                                        },
                                        {
                                            "text" : "Shoes",
                                            "isiproduk" : [
                                                {
                                                    "id": "09",
                                                    "type" : "shoes",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                                                    "text" : "Converse All Star Hi Plimsolls",
                                                    "price" : "75.00"
                                                }
                                            ]
                                        },
                                        {
                                            "text" : "Watches",
                                            "isiproduk" : [
                                                {
                                                    "id": "06",
                                                    "type" : "watches",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                                                    "name" : "Vintage Inspired Classic",
                                                    "price" : "93.20"
                                                },
                                                {
                                                    "id": "14",
                                                    "type" : "watches",
                                                    "image": "https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                                                    "text" : "Mini Silver Mesh Watch",
                                                    "price" : "86.85"
                                                }
                                            ]
                                        }
                                    ],
                                    "load" : [
                                        {
                                            "text" : "LOAD MORE",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "Footer" : [
                        {
                            "mainFooter" : [
                                {
                                    "categori" : [
                                        {
                                            "text" : "CATEGORIES"
                                        },
                                        {
                                            "text" : "Women",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "text" : "Men",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "text" : "Shoes",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "text" : "Watches",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        }
                                    ],
                                    "help" : [
                                        {
                                            "text" : "HELP"
                                        },
                                        {
                                            "text" : "Track Order",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "text" : "Return",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "text" : "Shipping",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "text" : "FAQs",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        }
                                    ],
                                    "getintouch" : [
                                        {
                                            "text" : "Any questions? Let us know in store at 8th floor, 379 Hudson St, New York, NY 10018 or call us on (+1) 96 716 6879"
                                        },
                                        {
                                            "medsos" : [
                                                {
                                                    "icon" : "fa fa-facebook",
                                                    "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                },
                                                {
                                                    "icon" : "fa fa-instagram",
                                                    "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                },
                                                {
                                                    "icon" : "fa fa-pinterest",
                                                    "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                                }
                                            ]
                                        }
                                    ],
                                    "newsletter" : [
                                        {
                                            "text" : "NEWSLETTER"
                                        },
                                        {
                                            "placeholder" : "email@example.com"
                                        },
                                        {
                                            "button" : [
                                                {
                                                    "text" : "SUBSCRIBE"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "lowerFooter" : [
                                {
                                    "pembayaran" : [
                                        {
                                            "image" : "https://preview.colorlib.com/theme/cozastore/images/icons/xicon-pay-01.png.pagespeed.ic.x3ksseq-Ro.webp",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "image" : "https://preview.colorlib.com/theme/cozastore/images/icons/xicon-pay-02.png.pagespeed.ic.VV76jih-LZ.webp",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "image" : "https://preview.colorlib.com/theme/cozastore/images/icons/xicon-pay-03.png.pagespeed.ic.qm10pI94h8.webp",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "image" : "https://preview.colorlib.com/theme/cozastore/images/icons/xicon-pay-04.png.pagespeed.ic.afX_pRP1xW.webp",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        },
                                        {
                                            "image" : "https://preview.colorlib.com/theme/cozastore/images/icons/xicon-pay-05.png.pagespeed.ic.j9rtlz4R-L.webp",
                                            "url" : "https://preview.colorlib.com/theme/cozastore/index.html#"
                                        }
                                    ],
                                    "copyright" : [
                                        {
                                            "text" : "Copyright ©2022 All rights reserved | This template is made with  by"
                                        },
                                        {
                                            "text" : "Colorlib",
                                            "url" : "https://colorlib.com/"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

class menubar(Resource):
    def get(self):
        return {
            "bawah" :[
                            {
                                "logo" : {
                                    "text" : "COLOSHOP",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
        
                                "home" : {
                                    "text" : "home",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
        
                                "shop" : {
                                    "text" : "shop",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
        
                                "promo" : {
                                    "text" : "promotion",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
        
                                "pages" : {
                                    "text" : "pages",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
        
                                "blog" : {
                                    "text" : "blog",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
        
                                "contact" : {
                                    "text" : "contact",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
                                "pencarian" : {
                                    "icons" : "search",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
                                "item" : {
                                    "icons" : "contact",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                },
        
                                "keranjang" : [
                                    {
                                    "defaultvalue" : "2",
                                    "icons" : "shopping",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                }
                                ]
                            }
                        ]
        }

class setting(Resource):
    def get(sefl):
        return {
            "setting" :[
                {
                  "matauang" : [
                                    {
                                        "currently" : {
                                            "item1" :{
                                                "text" : "USD",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                            }
                                        },
                                        "dropdown" :[
                                            {
                                                "item2" :{
                                            "text" : "CAD",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                        },
                                        "item3" :{
                                            "text" : "AUD",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                        },
                                        "item4" :{
                                            "text" : "EUR",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                        },
                                        "item5" :{
                                            "text" : "GBP",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                        }
                                            }
                                        ]
                                        
                                    }
                                ]  
                },
                {
                   "bahasa" : [
                                    {
                                       "currently" : {
                                        "item1" :{
                                            "text" : "english",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        }
                                       ,
                                       "dropdown" : [
                                           {
                                            "item1" :{
                                                "text" : "english",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            },
                                            "item2" :{
                                                "text" : "french",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            },
                                            "item3" :{
                                                "text" : "italian",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            },
                                            "item4" :{
                                                "text" : "german",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            },
                                            "item5" :{
                                                "text" : "spainish",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                           }
                                       ]
                                    }
                                ] 
                }
            ]
        }

class account(Resource):
    def get(sefl):
        return {
            "akun" : [
            {
                "isloggin" : null,
                "sign" : {
                     "text" : "SIGN IN",
                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                    },
        
                "register" : {
                    "text" : "REGISTER",
                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                    }
                }
            ]
        }

class bodyall(Resource):
    def get(sefl):
        return {
            "body" : [
                    {
                        "slider": [
                            {
                            "img" : "photos.jpg",
                            "text1" : "SPRING/SUMMER COLLECTION 2017"
                            },
                            {
                            "text2" : "Get up to 30% Off New Arrivals"
                            },
                            {
                            "button" : {
                                "text" : "shop now",
                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                }
                            }
                    ]
                    },
                    {
                        "banner" : [
                            {
                            "item1" : {
                                "img" : "photos.jpg",
                                "text" : "women's",
                                "url" : "https://preview.colorlib.com/theme/coloshop/categories.html"
                            },
                            "item2" : {
                                "img" : "photos2.jpg",
                                "text" : "accessories's's",
                                "url" : "https://preview.colorlib.com/theme/coloshop/categories.html"
                            },
                            "item3" : {
                                "img" : "photos3.jpg",
                                "text" : "men's",
                                "url" : "https://preview.colorlib.com/theme/coloshop/categories.html"
                            }
                        }
                        ]
                    },
                    {
                        "newArrivals" :[
                            {
                            "text" : "New Arrivals",
                            "currentlymenu" :{
                                "all" : 
                                {
                                "button" :{
                                    "text" : "all",
                                    "produk1" : {
                                        "item1" : {
                                            "img" : "photos.jpg",
                                            "text" : "fujifilm x100t 16 mp digital camera (silver)",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$520.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item2" : {
                                            "img" : "photos.jpg",
                                            "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$610.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item3" : {
                                            "img" : "photos.jpg",
                                            "text" : "blue yeti usb microphone black edition",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$120.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item4" : {
                                            "img" : "photos.jpg",
                                            "text" : "dymo label writer 450 turbo thermal label printer",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$410.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item5" : {
                                            "img" : "photos.jpg",
                                            "text" : "pryma headphones, rose gold & grey",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$180.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item6" : {
                                            "img" : "photos.jpg",
                                            "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$610.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item7" : {
                                            "img" : "photos.jpg",
                                            "text" : "blue yeti usb microphone black edition",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$120.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item8" : {
                                            "img" : "photos.jpg",
                                            "text" : "dymo label writer 450 turbo thermal label printer",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$410.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item9" : {
                                            "img" : "photos.jpg",
                                            "text" : "pryma headphones, rose gold & grey",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$180.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item10" : {
                                            "img" : "photos.jpg",
                                            "text" : "pryma headphones, rose gold & grey",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$180.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        }
                                    }
                                }
                                }
                            },
                            "menu" : {
                                "all" : 
                                {
                                "button" :{
                                    "text" : "all",
                                    "produk1" : {
                                        "item1" : {
                                            "img" : "photos.jpg",
                                            "text" : "fujifilm x100t 16 mp digital camera (silver)",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$520.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item2" : {
                                            "img" : "photos.jpg",
                                            "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$610.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item3" : {
                                            "img" : "photos.jpg",
                                            "text" : "blue yeti usb microphone black edition",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$120.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item4" : {
                                            "img" : "photos.jpg",
                                            "text" : "dymo label writer 450 turbo thermal label printer",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$410.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item5" : {
                                            "img" : "photos.jpg",
                                            "text" : "pryma headphones, rose gold & grey",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$180.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item6" : {
                                            "img" : "photos.jpg",
                                            "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$610.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item7" : {
                                            "img" : "photos.jpg",
                                            "text" : "blue yeti usb microphone black edition",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$120.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item8" : {
                                            "img" : "photos.jpg",
                                            "text" : "dymo label writer 450 turbo thermal label printer",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$410.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item9" : {
                                            "img" : "photos.jpg",
                                            "text" : "pryma headphones, rose gold & grey",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$180.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        },
                                        "item10" : {
                                            "img" : "photos.jpg",
                                            "text" : "pryma headphones, rose gold & grey",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                            "price" : "$180.000",
                                            "button" : {
                                                "text" : "add to card",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                            }
                                            
                                        }
                                    }
                                }
                                },
                                "women" :
                                     {
                                    "button" :{
                                        "text" : "women's",
                                        "produk1" : {
                                            "item1" : {
                                                "img" : "photos.jpg",
                                                "text" : "fujifilm x100t 16 mp digital camera (silver)",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$520.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                }
                                                
                                            },
                                            "item2" : {
                                                "img" : "photos.jpg",
                                                "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$610.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                }
                                                
                                            },
                                            "item3" : {
                                                "img" : "photos.jpg",
                                                "text" : "blue yeti usb microphone black edition",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$120.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                }
                                                
                                            },
                                            "item4" : {
                                                "img" : "photos.jpg",
                                                "text" : "dymo label writer 450 turbo thermal label printer",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$410.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                }
                                            }
                                        }
                                            
                                    }
                                },
                                "accessories" : 
                                    {
                                    "button" :{
                                        "text" : "accessories",
                                        "produk1" :[ {
                                            "item1" : {
                                                "img" : "photos.jpg",
                                                "text" : "dymo label writer 450 turbo thermal label printer",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$410.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                }
                                                
                                            }
                                        },
                                        {
                                        "produk2" : {
                                            "item1" : {
                                                "img" : "photos.jpg",
                                                "text" : "fujifilm x100t 16 mp digital camera (silver)",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$520.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                    }  
                                                }
                                            }
                                        },
                                        {
                                        "produk3" : {
                                             "item1" : {
                                                "img" : "photos.jpg",
                                                "text" : "Blue yeti USB Microphone Blackout Edition",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$120.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                    }  
                                                }
                                            }
                                        }
                                        ]
                                    }
                                }      
                            }
                            }
                        ]
                    },   
                    {
                        "flashsale" :[
                            {
                                "img" : "gambar2",
                                "text" : "deal of the week"
                            },
                            {
                                "hitungundur" : [
                                    {
                                        "item1" :
                                            {
                                                "id" : "2",
                                                "text" : "day"
                                            }
                                    },
                                    {
                                        "item2" : 
                                            {
                                                "id" : "23",
                                                "text" : "hours"
                                            }
                                    },
                                    {
                                        "item3" : 
                                            {
                                                "id" : "59",
                                                "text" : "mins"
                                            }
                                    },
                                    {
                                        "item4" :
                                            {
                                                "id" : "59",
                                                "text" : "sec"
                                            }
                                    }
                                ]
                            },
                            {
                                "buttontext" : "shop now"
                            }
                        ]
                    },
                    {
                        "bestSellers" :[
                            {
                                "teks" : "Best Seller",
                                "produk" :[ 
                                    {
                                    "item1" : {
                                        "img" : "photos.jpg",
                                        "text" : "fujifilm x100t 16 mp digital camera (silver)",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$520.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item2" : {
                                        "img" : "photos.jpg",
                                        "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$610.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item3" : {
                                        "img" : "photos.jpg",
                                        "text" : "blue yeti usb microphone black edition",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$120.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item4" : {
                                        "img" : "photos.jpg",
                                        "text" : "dymo label writer 450 turbo thermal label printer",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$410.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item5" : {
                                        "img" : "photos.jpg",
                                        "text" : "pryma headphones, rose gold & grey",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$180.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item6" : {
                                        "img" : "photos.jpg",
                                        "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$610.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item7" : {
                                        "img" : "photos.jpg",
                                        "text" : "blue yeti usb microphone black edition",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$120.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item8" : {
                                        "img" : "photos.jpg",
                                        "text" : "dymo label writer 450 turbo thermal label printer",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$410.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item9" : {
                                        "img" : "photos.jpg",
                                        "text" : "pryma headphones, rose gold & grey",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$180.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item10" : {
                                        "img" : "photos.jpg",
                                        "text" : "pryma headphones, rose gold & grey",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$180.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    }
                                }
                                ]
                            }
                        ]
                    },
                    {
                       "payment"  : [
                           {
                               "item" : [
                                   {
                                       "icons" : "truck",
                                       "text" : "free shiping",
                                       "desc" : "Suffered Alteration in Some Form"
                                   },
                                   {
                                       "icons" : "money",
                                       "text" : "cash on delivery",
                                       "desc" : "The Internet Tend To Repeat"
                                   },
                                   {
                                       "icons" : "back",
                                       "text" : "45 days return",
                                       "desc" : "The Internet Tend To Repeat"
                                   },
                                   {
                                       "icons" : "jam",
                                       "text" : "opening all week",
                                       "desc" : "8am-09pm"
                                   }
                               ]
                           }
                       ]
                    },
                    {
                        "blogs" : [
                            {
                                "text" : "Latest Blogs",
                                "blogs" :[
                                    {
                                        "img"  : "gambar1",
                                        "hover" : [
                                            {
                                                "atas" : "Here are the trends I see coming this fall",
                                                "tengah" : "by admin | dec 01, 2017",
                                                "bawah" : {
                                                    "text" : "read more",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                                }
                                            }
                                        ]
        
                                    },
                                    {
                                        "img"  : "gambar2",
                                        "hover" : [
                                            {
                                                "atas" : "Here are the trends I see coming this fall",
                                                "tengah" : "by admin | dec 01, 2017",
                                                "bawah" : {
                                                    "text" : "read more",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                                }
                                            }
                                        ]
        
                                    },
                                    {
                                        "img"  : "gambar3",
                                        "hover" : [
                                            {
                                                "atas" : "Here are the trends I see coming this fall",
                                                "tengah" : "by admin | dec 01, 2017",
                                                "bawah" : {
                                                    "text" : "read more",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                                }
                                            }
                                        ]
        
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "bawah" : [
                            {
                                "judul" : "Newsletter",
                                "text" : "Subscribe to our newsletter and get 20% off your first purchase",
                                "placeholder" : "your email",
                                "button" : "subscribe"
                            }
                        ]
                    }
        
                ]
        }

class slider(Resource):
    def get(sefl):
        return {
            "slider": [
                            {
                            "img" : "photos.jpg",
                            "text1" : "SPRING/SUMMER COLLECTION 2017"
                            },
                            {
                            "text2" : "Get up to 30% Off New Arrivals"
                            },
                            {
                            "button" : {
                                "text" : "shop now",
                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                }
                            }
                    ]
        }

class banner(Resource):
    def get(sefl):
        return {
            "banner" : [
                            {
                            "item1" : {
                                "img" : "photos.jpg",
                                "text" : "women's",
                                "url" : "https://preview.colorlib.com/theme/coloshop/categories.html"
                            },
                            "item2" : {
                                "img" : "photos2.jpg",
                                "text" : "accessories's's",
                                "url" : "https://preview.colorlib.com/theme/coloshop/categories.html"
                            },
                            "item3" : {
                                "img" : "photos3.jpg",
                                "text" : "men's",
                                "url" : "https://preview.colorlib.com/theme/coloshop/categories.html"
                            }
                        }
                        ]
        }

class newarrivals(Resource):
    def get(sefl):
        return {
            "data" :{
                "text" : "New Arrivals",
                "menu" :[
                    {
                      "text" : "all"  
                    },
                    {
                        "text" : "women's"
                    },
                    {
                       "text" : "accessories" 
                    }
                ]
            }
        }

class all(Resource):
    def get(sefl):
        return {
             "all" : [
            {
                "button" :{
                "text" : "all",
                "produk1" : {
                     "item1" : {
                        "img" : "photos.jpg",
                        "text" : "fujifilm x100t 16 mp digital camera (silver)",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$520.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                    }
                    },
                     "item2" : {
                        "img" : "photos.jpg",
                        "text" : "samsung cf591 series curved 27- inc fdh monitor",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$610.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }
                                            
                        },                                   
                     "item3" : {
                        "img" : "photos.jpg",
                        "text" : "blue yeti usb microphone black edition",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$120.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }     
                    },
                     "item4" : {
                        "img" : "photos.jpg",
                        "text" : "dymo label writer 450 turbo thermal label printer",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$410.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }    
                    },
                     "item5" : {
                        "img" : "photos.jpg",
                        "text" : "pryma headphones, rose gold & grey",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$180.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }                                            
                    },
                     "item6" : {
                        "img" : "photos.jpg",
                        "text" : "samsung cf591 series curved 27- inc fdh monitor",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$610.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }                                            
                    },
                     "item7" : {
                        "img" : "photos.jpg",
                        "text" : "blue yeti usb microphone black edition",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$120.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }                                           
                    },
                     "item8" : {
                        "img" : "photos.jpg",
                        "text" : "dymo label writer 450 turbo thermal label printer",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$410.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }                                          
                    },
                     "item9" : {
                        "img" : "photos.jpg",
                        "text" : "pryma headphones, rose gold & grey",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$180.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }
                                            
                                        },
                     "item10" : {
                        "img" : "photos.jpg",
                            "text" : "pryma headphones, rose gold & grey",
                            "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                            "price" : "$180.000",
                            "button" : {
                                "text" : "add to card",
                                "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                }                                           
                        }
                    }
                }
            } 
           ]
        }

class women(Resource):
    def get(sefl):
        return {
         "women" :
            {
                "button" :{
                "text" : "women's",
                "produk1" : {
                    "item1" : {
                        "img" : "photos.jpg",
                        "text" : "fujifilm x100t 16 mp digital camera (silver)",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$520.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }
                                                
                                            },
                    "item2" : {
                        "img" : "photos.jpg",
                        "text" : "samsung cf591 series curved 27- inc fdh monitor",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$610.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }             
                    },
                    "item3" : {
                        "img" : "photos.jpg",
                        "text" : "blue yeti usb microphone black edition",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$120.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                    }         
                    },
                    "item4" : {
                        "img" : "photos.jpg",
                        "text" : "dymo label writer 450 turbo thermal label printer",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$410.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }
                    }
                }
                }
            }   
        }

class accessories(Resource):
    def get(sefl):
        return {
            "accessories" : 
                {
                "button" :{
                    "text" : "accessories",
                    "produk1" :[
                        {
                        "item1" : {
                        "img" : "photos.jpg",
                        "text" : "dymo label writer 450 turbo thermal label printer",
                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                        "price" : "$410.000",
                        "button" : {
                            "text" : "add to card",
                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                            }
                                                
                        }
                        },
                        {
                         "item1" : {
                                                "img" : "photos.jpg",
                                                "text" : "fujifilm x100t 16 mp digital camera (silver)",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$520.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                    }  
                                                }
                        },
                        {
                        "item1" : {
                                                "img" : "photos.jpg",
                                                "text" : "Blue yeti USB Microphone Blackout Edition",
                                                "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                                "price" : "$120.000",
                                                "button" : {
                                                    "text" : "add to card",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                                    }  
                                                }
                        }
                    ]
                }
                } 
            } 

class flashsale(Resource):
    def get(sefl):
        return {
           "flashsale" :[
                            {
                                "img" : "gambar2",
                                "text" : "deal of the week"
                            },
                            {
                                "hitungundur" : [
                                    {
                                        "item1" :
                                            {
                                                "id" : "2",
                                                "text" : "day"
                                            }
                                    },
                                    {
                                        "item2" : 
                                            {
                                                "id" : "23",
                                                "text" : "hours"
                                            }
                                    },
                                    {
                                        "item3" : 
                                            {
                                                "id" : "59",
                                                "text" : "mins"
                                            }
                                    },
                                    {
                                        "item4" :
                                            {
                                                "id" : "59",
                                                "text" : "sec"
                                            }
                                    }
                                ]
                            },
                            {
                                "buttontext" : "shop now"
                            }
                        ] 
        }

class bestseller(Resource):
    def get(sefl):
        return {
            "bestSellers" :[
                            {
                                "teks" : "Best Seller",
                                "produk" :[ 
                                    {
                                    "item1" : {
                                        "img" : "photos.jpg",
                                        "text" : "fujifilm x100t 16 mp digital camera (silver)",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$520.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item2" : {
                                        "img" : "photos.jpg",
                                        "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$610.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item3" : {
                                        "img" : "photos.jpg",
                                        "text" : "blue yeti usb microphone black edition",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$120.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item4" : {
                                        "img" : "photos.jpg",
                                        "text" : "dymo label writer 450 turbo thermal label printer",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$410.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item5" : {
                                        "img" : "photos.jpg",
                                        "text" : "pryma headphones, rose gold & grey",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$180.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item6" : {
                                        "img" : "photos.jpg",
                                        "text" : "samsung cf591 series curved 27- inc fdh monitor",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$610.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item7" : {
                                        "img" : "photos.jpg",
                                        "text" : "blue yeti usb microphone black edition",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$120.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item8" : {
                                        "img" : "photos.jpg",
                                        "text" : "dymo label writer 450 turbo thermal label printer",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$410.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item9" : {
                                        "img" : "photos.jpg",
                                        "text" : "pryma headphones, rose gold & grey",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$180.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    },
                                    "item10" : {
                                        "img" : "photos.jpg",
                                        "text" : "pryma headphones, rose gold & grey",
                                        "url" : "https://preview.colorlib.com/theme/coloshop/single.html",
                                        "price" : "$180.000",
                                        "button" : {
                                            "text" : "add to card",
                                            "url" : "https://preview.colorlib.com/theme/coloshop/index.html#"
                                        }
                                        
                                    }
                                }
                                ]
                            }
                        ]
        }

class payment(Resource):
    def get(sefl):
        return {
            "payment"  : [
                           {
                               "item" : [
                                   {
                                       "icons" : "truck",
                                       "text" : "free shiping",
                                       "desc" : "Suffered Alteration in Some Form"
                                   },
                                   {
                                       "icons" : "money",
                                       "text" : "cash on delivery",
                                       "desc" : "The Internet Tend To Repeat"
                                   },
                                   {
                                       "icons" : "back",
                                       "text" : "45 days return",
                                       "desc" : "The Internet Tend To Repeat"
                                   },
                                   {
                                       "icons" : "jam",
                                       "text" : "opening all week",
                                       "desc" : "8am-09pm"
                                   }
                               ]
                           }
                       ]
        }

class blogs(Resource):
    def get(sefl):
        return {
             "blogs" : [
                            {
                                "text" : "Latest Blogs",
                                "blogs" :[
                                    {
                                        "img"  : "gambar1",
                                        "hover" : [
                                            {
                                                "atas" : "Here are the trends I see coming this fall",
                                                "tengah" : "by admin | dec 01, 2017",
                                                "bawah" : {
                                                    "text" : "read more",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                                }
                                            }
                                        ]
        
                                    },
                                    {
                                        "img"  : "gambar2",
                                        "hover" : [
                                            {
                                                "atas" : "Here are the trends I see coming this fall",
                                                "tengah" : "by admin | dec 01, 2017",
                                                "bawah" : {
                                                    "text" : "read more",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                                }
                                            }
                                        ]
        
                                    },
                                    {
                                        "img"  : "gambar3",
                                        "hover" : [
                                            {
                                                "atas" : "Here are the trends I see coming this fall",
                                                "tengah" : "by admin | dec 01, 2017",
                                                "bawah" : {
                                                    "text" : "read more",
                                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                                }
                                            }
                                        ]
        
                                    }
                                ]
                            }
                        ]
        }

class footer(Resource):
    def get(sefl):
        return {
            "footer" : [
                    {
                        "top" :[
                            {
                                "item" : "blog",
                                "url" :  "https://preview.colorlib.com/theme/coloshop/#"
                            },
                            {
                                "item" : "faqs",
                                "url" :  "https://preview.colorlib.com/theme/coloshop/#"
                            },
                            {
                                "item" : "contact us",
                                "url" :  "https://preview.colorlib.com/theme/coloshop/contact.html"
                            }
                        ]
                    },
                    {
                        "tengah" :[
                            {
                                "item" : {
                                    "icons" : "facebook",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                }
                            },
                            {
                                "item" : {
                                    "icons" : "twiter",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                }
                            },
                            {
                                "item" : {
                                    "icons" : "instagram",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                }
                            },
                            {
                                "item" : {
                                    "icons" : "skype",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                }
                            },
                            {
                                "item" : {
                                    "icons" : "pinterest",
                                    "url" : "https://preview.colorlib.com/theme/coloshop/#"
                                }
                            }
                        ]
                    },
                    {
                        "bawah" : [
                            {
                                "text" : "©2018 All Rights Reserverd. This template is made with",
                                "icons" : "love"
                            },
                            {
                                "text" : "colorib",
                                "url" : "https://preview.colorlib.com/theme/coloshop/#"
                            }
                        ] 
                    }
                ]
        }





api.add_resource(halamanhome, '/home/')
api.add_resource(menubar, '/menubar/')
api.add_resource(setting, '/setting/')
api.add_resource(account, '/account/')
api.add_resource(bodyall, '/bodyall/')
api.add_resource(slider, '/slider/')
api.add_resource(banner, '/banner/')
api.add_resource(newarrivals, '/newarrivals/')
api.add_resource(all, '/all/')
api.add_resource(women, '/women/')
api.add_resource(accessories, '/accessories/')
api.add_resource(flashsale, '/flashsale/')
api.add_resource(bestseller, '/bestseller/')
api.add_resource(payment, '/payment/')
api.add_resource(blogs, '/blogs/')
api.add_resource(footer, '/footer/')

@app.errorhandler(404)
def page_not_found(e):
    return {"error":"not found end point"}, 404

if __name__ == '__main__':
    app.run(debug=True)