from pyscript import document

# Function that generates the SKU
def generate_sku(event):

    # Get the values entered by the user
    category = document.getElementById("category").value
    product = document.getElementById("product").value.strip()
    stock = document.getElementById("stock").value
    # Get the area where the generated SKU will be displayed
    result = document.getElementById("sku_result")

    # Check if the user selected a product category
    if category == "":
        result.innerHTML = """
            <p>Please select a category.</p>
        """
        return

    # Check if the user selected a product name
    if product == "":
        result.innerHTML = """
            <p>Please enter a product name.</p>
        """
        return

    # Check if the user selected a stock quantity
    if stock == "":
        result.innerHTML = """
            <p>Please enter the stock quantity.</p>
        """
        return

    # Split the product name into individual words
    words = product.upper().split()

    # Create the product code
    product_code = ""

    # Format the stock quantity
    stock_code = str(int(stock)).zfill(3)

    for word in words:

        product_code += word[0] 

    # Combine category, product code, and stock code to create the SKU
    sku = f"{category}-{product_code}-{stock_code}"

    # Display the generated SKU and product information
    result.innerHTML = f"""
        <h3>Generated SKU</h3>
        <h2>{sku}</h2>
        <p>Product: {product}</p>
        <p>Stock Quantity: {stock}</p>
    """
           
