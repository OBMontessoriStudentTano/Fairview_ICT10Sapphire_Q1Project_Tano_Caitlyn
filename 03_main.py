from pyscript import document

def order(event):

    subtotal = 0

    receipt_lines = []

    checkboxes = document.querySelectorAll("input[type='checkbox']")

    for item in checkboxes:

        if item.checked:

            price = int(item.getAttribute("data-price"))

            sku = item.getAttribute("data-sku")

            subtotal += price

            item_name = item.id.replace("_", " ").title()

            receipt_lines.append(f"{item_name} - {price} pesos - SKU {sku}")

    soft_drink = document.getElementById("soft_drink")

    if soft_drink.value != "":

        selected = soft_drink.options[soft_drink.selectedIndex]

        soft_drink_price = int(selected.getAttribute("data-price"))

        sku = selected.getAttribute("data-sku")

        subtotal += soft_drink_price

        receipt_lines.append(f"{selected.text} - SKU: {sku}")

    vat = subtotal * 0.12
    total = subtotal + vat

    receipt = "<h4>Receipt</h4>"

    if len(receipt_lines) == 0:

        receipt += """
             <p>No items selected.</p>
        """

    else:

        for item in receipt_lines:

            receipt += f"""
                <p>{item}</p>
            """

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

    document.getElementById("receipt").innerHTML = receipt