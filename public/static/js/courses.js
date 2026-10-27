
document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.getElementById("courseSearchForm");
    const searchInput = document.getElementById("courseSearch");
    const clearButton = document.getElementById("clearSearch");
    const courseTable = document.getElementById("courseTable");
    const courseCount = document.getElementById("courseCount");
    const totalCourseCount = document.getElementById("totalCourseCount");
    const searchMessage = document.getElementById("courseSearchMessage");

    if (!searchInput || !courseTable) {
        console.error("Course search: required HTML elements were not found.");
        return;
    }

    const tableBody = courseTable.querySelector("tbody");

    if (!tableBody) {
        return;
    }

    // Keep only actual course rows, excluding the empty-state row.
    const rows = Array.from(tableBody.querySelectorAll("tr")).filter(
        row => row.querySelector(".course-name") !== null
    );

    const total = rows.length;

    if (totalCourseCount) {
        totalCourseCount.textContent = total;
    }

    function searchCourses() {
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

        if (courseCount) {
            courseCount.textContent = visible;
        }

        if (searchMessage) {
            searchMessage.hidden = visible !== 0 || total === 0;
        }
    }

    // Search button
    if (searchForm) {
        searchForm.addEventListener("submit", function (event) {
            event.preventDefault();
            searchCourses();
        });
    }

    // Filter as the user types
    searchInput.addEventListener("input", searchCourses);

    // Clear search
    if (clearButton) {
        clearButton.addEventListener("click", function () {
            searchInput.value = "";
            searchCourses();
            searchInput.focus();
        });
    }

    // Initialize the displayed count
    searchCourses();
});
