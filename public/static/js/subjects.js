
const searchForm = document.getElementById("subjectSearchForm");
const searchInput = document.getElementById("subjectSearch");
const clearButton = document.getElementById("clearSubjectSearch");
const tableRows = document.querySelectorAll("#subjectTable tbody tr");
const subjectCount = document.getElementById("subjectCount");

function filterSubjects() {
    const query = searchInput.value.toLowerCase().trim();
    let visibleCount = 0;

    tableRows.forEach(function(row) {
        // Keep the empty-state row unchanged.
        if (row.querySelector(".subject-empty")) {
            return;
        }

        const matches = row.textContent.toLowerCase().includes(query);

        row.style.display = matches ? "" : "none";

        if (matches) {
            visibleCount++;
        }
    });

    subjectCount.textContent = visibleCount;
}

if (searchForm && searchInput && clearButton && subjectCount) {
    searchForm.addEventListener("submit", function(event) {
        event.preventDefault();
        filterSubjects();
    });

    searchInput.addEventListener("input", filterSubjects);

    clearButton.addEventListener("click", function() {
        searchInput.value = "";
        filterSubjects();
        searchInput.focus();
    });
}
