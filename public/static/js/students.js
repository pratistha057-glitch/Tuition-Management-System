document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("searchInput");
    const tableBody = document.getElementById("studentTableBody");
    const visibleCountText = document.getElementById("visibleCountText");
    const totalCountText = document.getElementById("totalCountText");
    const noResults = document.getElementById("noResults");
    if (!searchInput || !tableBody) return;

    const rows = Array.from(tableBody.querySelectorAll("tr"))
        .filter(row => !row.classList.contains("empty-database-row"));

    function updateResults() {
        const query = searchInput.value.toLowerCase().trim();
        let visibleCount = 0;
        rows.forEach(row => {
            const matches = row.innerText.toLowerCase().includes(query);
            row.style.display = matches ? "" : "none";
            if (matches) visibleCount++;
        });
        if (visibleCountText) visibleCountText.textContent = visibleCount;
        if (totalCountText) totalCountText.textContent = rows.length;
        if (noResults) noResults.style.display = rows.length > 0 && visibleCount === 0 ? "block" : "none";
    }
    searchInput.addEventListener("input", updateResults);
    updateResults();
});
