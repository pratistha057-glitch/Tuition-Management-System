
document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("student-search");
    const studentRows = document.querySelectorAll(".student-row");
    const noSearchResults = document.getElementById("no-search-results");

    const totalStudents = document.getElementById("total-students");
    const presentStudents = document.getElementById("present-students");
    const absentStudents = document.getElementById("absent-students");

    // Search students by ID or name.
    searchInput.addEventListener("input", function () {
        const searchText = searchInput.value.trim().toLowerCase();
        let visibleRows = 0;

        studentRows.forEach(function (row) {
            const studentId = row.querySelector(".student-id").textContent.toLowerCase();
            const studentName = row.querySelector(".student-name").textContent.toLowerCase();

            const matches =
                studentId.includes(searchText) ||
                studentName.includes(searchText);

            row.hidden = !matches;

            if (matches) {
                visibleRows++;
            }
        });

        noSearchResults.hidden =
            searchText === "" || visibleRows > 0;
    });

    // Count attendance for all students, not just search results.
    function updateAttendanceCounts() {
        let presentCount = 0;
        let absentCount = 0;

        studentRows.forEach(function (row) {
            const selectedStatus = row.querySelector(
                'input[type="radio"]:checked'
            );

            if (selectedStatus) {
                if (selectedStatus.value === "Present") {
                    presentCount++;
                } else if (selectedStatus.value === "Absent") {
                    absentCount++;
                }
            }
        });

        totalStudents.textContent = studentRows.length;
        presentStudents.textContent = presentCount;
        absentStudents.textContent = absentCount;
    }

    // Update the counts when a status is changed.
    document.getElementById("attendance-form").addEventListener(
        "change",
        function (event) {
            if (event.target.matches('input[type="radio"]')) {
                updateAttendanceCounts();
            }
        }
    );

    // Show the initial counts when the page loads.
    updateAttendanceCounts();
});
