# Django3 README

## Exercises 

### Exercise 1 - Project Setup
Create the project "marketplace", create the app "products", and install the application in the project.
---
### Exercise 2 - Creating Project Models
Implement the models Product, Seller, Buyer, and Order in the models.py file:

- Product should have the fields name, description, price, and seller;
- Seller should have the fields name and email;
- Buyer should have the fields name and email;
- Order should have the fields buyer and product.
---
### Exercise 3 - Creating Forms
Implement a form for each of the models created in the previous exercise. These forms will be used to insert data into the database:

- CreateProductForm;
- CreateSellerForm;
- CreateBuyerForm;
- CreateOrderForm.
---
### Exercise 4 - Implementing the View Layer
Implement the following functions in the views layer:

- index: renders the initial template of the project (index.html);
- product: renders the product creation template (product.html) and creates a product when it receives a POST request with the data;
- seller: renders the seller creation template (seller.html) and creates a seller when it receives a POST request with the data;
- buyer: renders the buyer creation template (buyer.html) and creates a buyer when it receives a POST request with the data;
- order: renders the order creation template (order.html) and creates an order when it receives a POST request with the data.
---
### Exercise 5 - Creating URLs
Implement the project's URLs:

- /: linked to the view index;
- /product: linked to the view index_product;
- /seller: linked to the view index_seller;
- /buyer: linked to the view index_buyer;
- /order: linked to the view index_order.
---
### Exercise 6 - Creating Templates
Implement the project templates:

- base.html: the base template of the project which should be inherited by all other templates;
- index.html: the initial template of the project which should be able to navigate to each of the creation pages;
- product.html: the product creation template;
- seller.html: the seller creation template;
- buyer.html: the buyer creation template;
- order.html: the order creation template.