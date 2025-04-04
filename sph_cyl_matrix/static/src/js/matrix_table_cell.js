document.addEventListener("DOMContentLoaded", function () {
    const tableCells = document.querySelectorAll(".editable-cell");

    tableCells.forEach(cell => {
        cell.addEventListener("input", function () {
            this.classList.add("modified");
        });
    });

    // Save changes button
    document.getElementById("save_matrix").addEventListener("click", function () {
        alert("Changes saved successfully!");
        tableCells.forEach(cell => {
            cell.classList.remove("modified");
        });
    });

    // Export to CSV
    document.getElementById("export_csv").addEventListener("click", function () {
        exportTableToCSV('sph_cyl_matrix.csv');
    });

    // Export to Excel
    document.getElementById("export_excel").addEventListener("click", function () {
        exportTableToExcel('sph_cyl_matrix.xlsx');
    });

    function exportTableToCSV(filename) {
        let csv = [];
        let rows = document.querySelectorAll("table tr");

        rows.forEach(row => {
            let cols = row.querySelectorAll("td, th");
            let rowData = [];
            cols.forEach(col => rowData.push(col.innerText));
            csv.push(rowData.join(","));
        });

        let csvFile = new Blob([csv.join("\n")], { type: "text/csv" });
        let link = document.createElement("a");
        link.download = filename;
        link.href = window.URL.createObjectURL(csvFile);
        link.click();
    }

    function exportTableToExcel(filename) {
        let table = document.querySelector("table");
        let tableHTML = table.outerHTML.replace(/ /g, "%20");

        let a = document.createElement("a");
        a.href = "data:application/vnd.ms-excel," + tableHTML;
        a.download = filename;
        a.click();
    }
});
