// Function to increase the quantity in the cart
function increaseQuantity(button) {
    var quantityElement = button.parentElement.querySelector('.quantity');
    var quantity = parseInt(quantityElement.innerText, 10);
    quantityElement.innerText = quantity + 1;
  
    updateTotal();
  }
  
  // Function to decrease the quantity in the cart
  function decreaseQuantity(button) {
    var quantityElement = button.parentElement.querySelector('.quantity');
    var quantity = parseInt(quantityElement.innerText, 10);
  
    if (quantity > 1) {
      quantityElement.innerText = quantity - 1;
      updateTotal();
    }
  }
  
  // Function to update the total amount
  function updateTotal() {
    var cartItems = document.querySelectorAll('.cart-item');
    var total = 0;
  
    cartItems.forEach(function (item) {
      var quantity = parseInt(item.querySelector('.quantity').innerText, 10);
      var price = parseFloat(item.querySelector('.item-price').innerText.slice(1));
      total += quantity * price;
    });
  
    document.querySelector('.cart-total p').innerText = 'Total: $' + total.toFixed(2);
  }
  
  // Function to handle the "Add to Cart" button click
  function addToCart(button) {
    // Assuming the price is $12.99, you can adjust this based on your actual item price
    var price = 12.99;
    
    var cartItem = button.parentElement;
    var itemName = cartItem.querySelector('.item-name').innerText;
    var quantity = parseInt(cartItem.querySelector('.quantity').innerText, 10);
  
    // Add the item to the cart (you might want to send this data to a server in a real application)
    console.log('Added to cart:', itemName, 'Quantity:', quantity);
  
    updateTotal();
  }
  
  // Function to initialize the event listeners
  function init() {
    var increaseButtons = document.querySelectorAll('.quantity-btn.increase');
    var decreaseButtons = document.querySelectorAll('.quantity-btn.decrease');
    var addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    increaseButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            increaseQuantity(button);
        });
    });

    decreaseButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            decreaseQuantity(button);
        });
    });

    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            addToCart(button);
        });
    });
  }
  