from pyscript import document

def generate_sku(event):

    category = document.getElementById("category").value

    product = document.getElementById("product").value.strip()

    result = document.getElementById("sku_result")

    if category == "":

        result.innerHTML = """
            <p>Please select a category.</p>
        """

    if product == "":

         result.innerHTML = """
            <p>Please enter a product name.</p>
        """

        return

    words = product.upper().split()

    product_code = ""

    for word in words:

        product_code += word[0] 

    sku = f"{category}-{product_code}"

    result.innerHTML = f"""
        <h3>Generated SKU</h3>
        <h2>{sku}</h2>
        <p>Product: {product}</p>
    """
           
