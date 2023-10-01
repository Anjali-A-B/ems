// script.js

document.addEventListener('DOMContentLoaded', function () {
    // Select the filter dropdown element
    const filterDropdown = document.getElementById('filter-status');

    // Select all leave request items
    const leaveItems = document.querySelectorAll('.leave-item');

    // Event listener for filter dropdown changes
    filterDropdown.addEventListener('change', function () {
        const selectedStatus = filterDropdown.value;

        // Loop through leave items and hide/show based on the selected status
        leaveItems.forEach(function (item) {
            const status = item.getAttribute('data-status');

            if (selectedStatus === 'all' || selectedStatus === status) {
                item.style.display = 'list-item'; // Show the item
            } else {
                item.style.display = 'none'; // Hide the item
            }
        });
    });
});
