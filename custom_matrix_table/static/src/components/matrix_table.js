/** @odoo-module */
import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class MatrixDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.actionService = useService("action");

        this.state = useState({
            sph_values: [],
            cyl_values: [],
            values_dict: {},
            upload_batch: '',
        });

        onWillStart(async () => {
            const result = await this.orm.call('sph.cyl.matrix', 'get_matrix_data', []);
            console.log("Got data from backend:", result);
            this.state.sph_values = result.sph_values;
            this.state.cyl_values = result.cyl_values;
            this.state.values_dict = result.values_dict;
            this.state.partner_name = result.partner_name;
            this.state.date = result.date;
            this.state.customer_ref = result.customer_ref;
            this.state.upload_batch = result.upload_batch;
        });
    }

    getCellValue(sph, cyl) {
        const key = `${sph},${cyl}`;
        return this.state.values_dict[key] || 0;
    }

    async onCellInput(ev) {
        const td = ev.target;
        const sph = td.dataset.sph;
        const cyl = td.dataset.cyl;
        const newValue = parseFloat(td.innerText.trim());

        // Optional: validate the input
        if (isNaN(newValue)) {
            td.classList.add('text-danger');
            return;
        } else {
            td.classList.remove('text-danger');
        }

        const key = `${sph},${cyl}`;
        this.state.values_dict[key] = newValue;

        // Update backend
        try {
            console.log("Updating backend...");
            console.log(`Updating with: sph=${sph}, cyl=${cyl}, value=${newValue}`);
            await this.orm.call('sph.cyl.matrix', 'update_matrix_cell', [sph, cyl, newValue]);
            console.log("Updating with value:", newValue);
            td.classList.add('modified');
            setTimeout(() => td.classList.remove('modified'), 1000);
            console.log("Updated backend successfully.");
        } catch (error) {
            console.error("Failed to update backend:", error);
        }
    }

    uploadData() {
        console.log("Upload data clicked");
        this.resetMatrixData();
        this.actionService.doAction({
            name: "Upload Data",
            type: 'ir.actions.act_window',
            res_model: 'import.sph.cyl.matrix.wizard',
            view_mode: 'form',
            view_type: 'form',
            views: [[false, "form"]],
            target: 'new'
        });
    }

    resetMatrixData() {
        this.state.partner_id = false;
        this.state.partner_name = '';
        this.state.date = '';
        this.state.customer_ref = '';
        this.state.sph_values = [];
        this.state.cyl_values = [];
        this.state.values_dict = {};
    }

    approved() {
        console.log("Approved clicked");
            console.log("Approved button clicked");
            const uploadBatch = this.state.upload_batch;

            if (!uploadBatch) {
                console.warn("No upload batch number found.");
                return;
            }

            this.orm.call("sph.cyl.matrix", "mark_approved", [uploadBatch])
                .then(() => {
                    console.log("Matrix marked as approved successfully.");
                })
                .catch((error) => {
                    console.error("Error approving matrix:", error);
                });
    }

    prepare_sale_order() {
        console.log("Prepare sale order clicked");
    }

}

MatrixDashboard.template = "MatrixDashboard";
registry.category("actions").add("menu_matrix_view", MatrixDashboard);
