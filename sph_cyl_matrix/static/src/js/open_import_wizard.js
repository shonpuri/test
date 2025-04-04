/** @odoo-module */

import { registry } from "@web/core/registry"
import { loadJS } from "@web/core/assets"
const { Component, onWillStart, useRef, onMounted } = owl

export class OwlMatrixDashboard extends Component {
    setup(){

    }
}

OwlSalesDashboard.template = "owl.MatrixDashboard"
export const OwlMatrixDashboard = {
    component: OwlMatrixDashboard,
};

registry.category("actions").add("owl.matrix_dashboard", OwlMatrixDashboard)










//import { registry } from "@web/core/registry";
//import { browser } from "@web/core/browser";
//import { _t } from "@web/core/l10n";
//import { doAction } from "@web/core/actions";
//
//console.log("JS Loaded: open_import_wizard");
//
//function setupImportButton() {
//    console.log("DOM ready - waiting for #upload_button");
//    const btn = document.querySelector('#upload_button');
//    if (btn) {
//        btn.addEventListener('click', () => {
//            console.log("Import button clicked!");
//            doAction({
//                type: 'ir.actions.act_window',
//                res_model: 'import.sph.cyl.matrix.wizard',
//                view_mode: 'form',
//                target: 'new',
//            });
//        });
//    } else {
//        console.warn("#upload_button not found");
//    }
//}
//
//// Wait for DOMContentLoaded
//browser.addEventListener("DOMContentLoaded", setupImportButton);
