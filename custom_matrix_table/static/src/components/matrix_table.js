/** @odoo-module */

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { useEnv } from "@odoo/owl";

export class MatrixDashboard extends Component {
    setup(props) {
        this.orm = useService("orm");
        this.actionService = useService("action");


        this.state = useState({
            sph_values: [],
            cyl_values: [],
            values_dict: {},
        });

        onWillStart(async () => {
            const result = await this.orm.call('sph.cyl.matrix', 'get_matrix_data', []);
            console.log("Got data from backend:", result);
            this.state.sph_values = result.sph_values;
            this.state.cyl_values = result.cyl_values;
            this.state.values_dict = result.values_dict;
        });



        // Define reactive state
//        this.state = useState({
//            sph_values: ["-2.00", "-1.75", "-1.50"],  // or fetched from DB
//            cyl_values: ["-0.25", "-0.50", "-0.75"],  // or fetched from DB
//            values_dict: {
//                "-2.00,-0.25": 5,
//                "-2.00,-0.50": 2,
//                "-1.75,-0.25": 10,
//                "-1.50,-0.75": 3,
//                // Add more as needed
//            },
//        });

        // Optional: fetch data from backend
        // onWillStart(async () => {
        //     const result = await this.orm.call('your.model.name', 'your_method', []);
        //     this.state.sph_values = result.sph_values;
        //     this.state.cyl_values = result.cyl_values;
        //     this.state.values_dict = result.values_dict;
        // });
    }
    getCellValue(sph, cyl) {
        const key = `${sph},${cyl}`;
        return this.state.values_dict[key] || 0;
    }

    uploadData() {
        console.log("Upload data clicked");
        var self = this;
        self.actionService.doAction({
            name: "Upload Data",
            type: 'ir.actions.act_window',
            res_model: 'import.sph.cyl.matrix.wizard',
            view_mode: 'form',
            view_type: 'form',
            views: [[false, "form"]],
            target: 'new'
        })

    }

    exportExcel() {
        console.log("Export clicked");
    }

    saveChanges() {
        console.log("Save clicked");
    }
}

// Register the component
MatrixDashboard.template = "MatrixDashboard";
registry.category("actions").add("menu_matrix_view", MatrixDashboard);
