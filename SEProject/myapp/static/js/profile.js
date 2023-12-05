// This script will handle dynamic updates to the profile page, including order history.

document.addEventListener('DOMContentLoaded', function () {

    // Assume that you have a function to retrieve order history
    const orderHistory = getOrderHistory();

    // Display order history
    displayOrderHistory(orderHistory);
});


// Function to retrieve order history (replace with actual implementation)
function getOrderHistory() {
    // Assume that you have a mechanism to store and retrieve order history, such as from a server or local storage
    // For demonstration purposes, returning a hardcoded array
    return [
        { id: 1, total: 25.99, items: ['Biryani', 'Sushi Rolls'], date: '2023-01-01' },
        { id: 2, total: 15.99, items: ['Pad Thai'], date: '2023-02-05' },
        // Add more order history items as needed
    ];
}

// Function to display order history
function displayOrderHistory(orderHistory) {
    const orderList = document.getElementById('order-list');

    orderHistory.forEach(order => {
        const orderItem = document.createElement('li');
        orderItem.className = 'order-item';
        orderItem.innerHTML = `
            <p><strong>Order ID:</strong> ${order.id}</p>
            <p><strong>Total:</strong> $${order.total.toFixed(2)}</p>
            <p><strong>Items:</strong> ${order.items.join(', ')}</p>
            <p><strong>Date:</strong> ${order.date}</p>
        `;
        orderList.appendChild(orderItem);
    });
}
