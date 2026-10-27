document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.getElementById("studentSearchForm");
    const searchInput = document.getElementById("studentSearch");
    const searchButton = searchForm
        ? searchForm.querySelector('button[type="submit"]')
        : null;
    const clearButton = document.getElementById("clearSearch");
    const studentTable = document.getElementById("studentTable");
    const studentCount = document.getElementById("studentCount");
    const totalStudentCount = document.getElementById("totalStudentCount");

    if (!searchInput || !studentTable) {
        console.error("Student search: required HTML elements were not found.");
        return;
    }

    const tableBody = studentTable.querySelector("tbody");

    if (!tableBody) {
        return;
    }

    const rows = Array.from(tableBody.querySelectorAll("tr")).filter(
        row => row.querySelector(".student-profile") !== null
    );

    const total = rows.length;

    if (totalStudentCount) {
        totalStudentCount.textContent = total;
    }

    // Add a message for searches with no matching students.
    let noResultsRow = tableBody.querySelector(".search-no-results");

    if (!noResultsRow) {
        noResultsRow = document.createElement("tr");
        noResultsRow.className = "search-no-results";
        noResultsRow.style.display = "none";

        const cell = document.createElement("td");
        cell.colSpan = 7;
        cell.className = "no-students";
        cell.textContent = "No matching students found.";

        noResultsRow.appendChild(cell);
        tableBody.appendChild(noResultsRow);
    }

    function searchStudents() {
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

        noResultsRow.style.display = visible === 0 ? "" : "none";

        if (studentCount) {
            studentCount.textContent = visible;
        }
    }

    if (searchForm) {
        searchForm.addEventListener("submit", function (event) {
            event.preventDefault();
            searchStudents();
        });
    }

    searchInput.addEventListener("input", searchStudents);

    if (clearButton) {
        clearButton.addEventListener("click", function () {
            searchInput.value = "";
            searchStudents();
            searchInput.focus();
        });
    }

    // Ensure the button is usable and the initial count is correct.
    if (searchButton) {
        searchButton.disabled = false;
    }

    searchStudents();
});