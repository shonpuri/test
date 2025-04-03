odoo.define('sph_cyl_matrix.MatrixWidget', function (require) {
    "use strict";

    const { Component } = owl;
    const { useRef, onMounted, onWillUnmount } = owl.hooks;

    class MatrixWidget extends Component {
        setup() {
            this.tableRef = useRef("table");

            onMounted(() => this.setupHover());
            onWillUnmount(() => this.cleanupHover());
        }

        setupHover() {
            this.highlightCells = (event, isOver) => {
                const cell = event.target;
                if (!cell.closest('td, th')) return;

                const row = cell.closest('tr');
                const colIndex = cell.cellIndex;

                // Highlight row
                row.querySelectorAll('th, td').forEach(el =>
                    el.classList.toggle('highlight-row', isOver)
                );

                // Highlight column
                this.tableRef.el.querySelectorAll(`tr td:nth-child(${colIndex + 1}), tr th:nth-child(${colIndex + 1})`)
                    .forEach(el => el.classList.toggle('highlight-col', isOver));
            };

            this.tableRef.el.addEventListener('mouseover', e => this.highlightCells(e, true));
            this.tableRef.el.addEventListener('mouseout', e => this.highlightCells(e, false));
        }

        cleanupHover() {
            if (this.tableRef.el) {
                this.tableRef.el.removeEventListener('mouseover', this.highlightCells);
                this.tableRef.el.removeEventListener('mouseout', this.highlightCells);
            }
        }
    }

    MatrixWidget.template = "sph_cyl_matrix.MatrixWidget";

    // Register the widget
    const { registry } = require('web.field_registry');
    registry.add('matrix_widget', MatrixWidget);

    return MatrixWidget;
});