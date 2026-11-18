(function () {
    var STATUS = { '🟢': 'green', '🟡': 'yellow', '🟠': 'orange', '🔴': 'red', '⚪': 'white' };

    function enhance() {
        var section = document.getElementById('chapter-map');
        if (!section) return;
        var rows = Array.from(section.querySelectorAll('table tbody tr'));

        rows.forEach(function (row) {
            var cells = row.querySelectorAll('td');
            if (cells.length < 2) return;
            var maturity = STATUS[cells[1].textContent.trim()];
            if (maturity) row.dataset.maturity = maturity;
            if (cells[0].querySelector('strong')) row.dataset.chapter = 'true';
        });

        rows.filter(function (r) { return r.dataset.chapter; }).forEach(function (chRow) {
            var sectionRows = [];
            var sibling = chRow.nextElementSibling;
            while (sibling && !sibling.dataset.chapter) {
                sectionRows.push(sibling);
                sibling = sibling.nextElementSibling;
            }
            if (!sectionRows.length) return;

            var btn = document.createElement('button');
            btn.className = 'ch-toggle';
            btn.setAttribute('aria-expanded', 'false');
            btn.setAttribute('aria-label', 'Unterkapitel ein-/ausblenden');
            var firstCell = chRow.querySelector('td');
            firstCell.insertBefore(btn, firstCell.firstChild);

            sectionRows.forEach(function (r) { r.hidden = true; });

            function toggle() {
                var expanded = btn.getAttribute('aria-expanded') === 'true';
                btn.setAttribute('aria-expanded', String(!expanded));
                sectionRows.forEach(function (r) {
                    r.hidden = expanded;
                    r.classList.toggle('ch-open', !expanded);
                });
            }

            btn.addEventListener('click', function (e) {
                e.stopPropagation();
                toggle();
            });

            chRow.addEventListener('click', function (e) {
                if (e.target.closest('a') || e.target.closest('button')) return;
                toggle();
            });
        });
    }

    document.readyState === 'loading'
        ? document.addEventListener('DOMContentLoaded', enhance)
        : enhance();
})();
