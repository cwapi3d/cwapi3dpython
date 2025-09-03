document$.subscribe(function () {
    var tables = document.querySelectorAll("article table:not([class])")

    
    tables.forEach(function (table) {
        table.querySelectorAll('tr').forEach(row => {
            if(row.children[3]) row.children[3].style.display = 'none'; // Hide the 4th column
        })
        new Tablesort(table) // Initialize Tablesort on the table
    })
})