from pyscript import document

# Function that processes the customer's order
def order(event):

    # Set the starting subtotal to zero
    subtotal = 0

    # Create a list to store the selected items
    receipt_lines = []

    # Get all checkbox items from the menu
    checkboxes = document.querySelectorAll("input[type='checkbox']")

    # Check which menu items were selected
    for item in checkboxes:

        if item.checked:

            # Get the item's price and SKU
            price = int(item.getAttribute("data-price"))
            sku = item.getAttribute("data-sku")

            # Add the item price to the subtotal
            subtotal += price

            # Convert the item ID into a readable product name
            item_name = item.id.replace("_", " ").title()

            # Add the item details to the receipt
            receipt_lines.append(f"{item_name} - {price} pesos - SKU {sku}")

    # Get the selected soft drink to the receipt
    soft_drink = document.getElementById("soft_drink")

    # If a soft drink was selected
    if soft_drink.value != "":

        selected = soft_drink.options[soft_drink.selectedIndex]

        soft_drink_price = int(selected.getAttribute("data-price"))

        sku = selected.getAttribute("data-sku")

        # Add the drink price to the subtotal
        subtotal += soft_drink_price

        # Add the drink details to the receipt
        receipt_lines.append(f"{selected.text} - SKU: {sku}")

    # Calculate the 12% VAT
    vat = subtotal * 0.12

    # Calculate the final total
    total = subtotal + vat
   
    # Create the receipt heading
    receipt = "<h4>Receipt</h4>"

    # Display if no items were selected
    if len(receipt_lines) == 0:

        receipt += """
             <p>No items selected.</p>
        """

    # Add each selected item to the receipt
    else:

        for item in receipt_lines:

            receipt += f"""
                <p>{item}</p>
            """

    # Add the subtotal, VAT, and total amount
    receipt += f"""
        <hr>
        <p>Subtotal: {subtotal:.2f} pesos</p>
        <p>VAT: {vat:.2f} pesos</p>
        <p class="total">
           <strong>
              Total Amount: {total:.2f} pesos
           </strong>
        </p>
    """

    # Display the completed receipt
    document.getElementById("receipt").innerHTML = receipt