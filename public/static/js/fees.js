
document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.getElementById("feeSearchForm");
    const searchInput = document.getElementById("feeSearch");
    const clearButton = document.getElementById("clearSearch");
    const feeTable = document.getElementById("feeTable");
    const feeCount = document.getElementById("feeCount");
    const totalFeeCount = document.getElementById("totalFeeCount");
    const searchMessage = document.getElementById("feeSearchMessage");

    if (!searchInput || !feeTable) {
        console.error("Fee search: required HTML elements were not found.");
        return;
    }

    const tableBody = feeTable.querySelector("tbody");

    if (!tableBody) {
        return;
    }

    // Keep only actual fee rows, excluding the empty-state row.
    const rows = Array.from(tableBody.querySelectorAll("tr")).filter(
        row => row.querySelector(".course-name") !== null
    );

    const total = rows.length;

    if (totalFeeCount) {
        totalFeeCount.textContent = total;
    }

    function searchFees() {
        const query = searchInput.value.trim().toLowerCase();
        let visible = 0;

        rows.forEach(function (row) {
            const text = row.textContent.toLowerCase();
            const matches = text.includes(query);

            row.style.display = matches ? "" : "none";

            if (matches) {
                visible++;
            }
        });

        if (feeCount) {
            feeCount.textContent = visible;
        }

        if (searchMessage) {
            searchMessage.hidden = visible !== 0 || total === 0;
        }
    }

    // Search button
    if (searchForm) {
        searchForm.addEventListener("submit", function (event) {
            event.preventDefault();
            searchFees();
        });
    }

    // Filter as the user types
    searchInput.addEventListener("input", searchFees);

    // Clear search
    if (clearButton) {
        clearButton.addEventListener("click", function () {
            searchInput.value = "";
            searchFees();
            searchInput.focus();
        });
    }

    // Initialize the displayed count
    searchFees();
});
