import base64
import xlrd
import uuid
from odoo import models, fields, api

class ImportSPHCYLMatrixWizard(models.TransientModel):
    _name = "import.sph.cyl.matrix.wizard"
    _description = "Import Lens Order Matrix from Excel"

    upload_batch = fields.Char('Batch Code', readonly=True, copy=False, )

    file = fields.Binary(string="Upload Excel File", required=True, widget='sph_cyl_upload')

    date = fields.Date(string="Date")
    partner_id = fields.Many2one("res.partner", string="Customer")
    customer_ref = fields.Char(string="Customer PO/Ref")

    filename = fields.Char(string="Filename", readonly=True)
    sheet_name = fields.Selection([], string="Select Sheet")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)


    def get_random_uuid(self):
        return uuid.uuid4().hex[:10].upper()

    @api.onchange("file")
    def _onchange_file(self):
        """ Extract filename and sheet names from the uploaded file """
        if self.file:
            # Extract filename from context (Odoo provides it automatically)
            self.filename = self._context.get("filename", "Unknown File")

            # Decode file and read sheets
            file_content = base64.b64decode(self.file)
            try:
                wb = xlrd.open_workbook(file_contents=file_content)
                sheet_names = wb.sheet_names()  # Get all sheet names
            except Exception as e:
                sheet_names = []
                print(f"Error reading Excel file: {e}")

            # Set sheet selection options dynamically
            self.sheet_name = False  # Reset selection
            return {"domain": {"sheet_name": [(s, s) for s in sheet_names]}}


    def import_sph_cyl_matrix(self):
        print("Import function triggered")  # Debugging

        file_content = base64.b64decode(self.file)
        wb = xlrd.open_workbook(file_contents=file_content)
        sheet = wb.sheet_by_index(0)
        upload_batch = self.get_random_uuid()

        # **Extract SPH values (First row, skipping first column)**
        sph_values = []
        for col in range(1, sheet.ncols):
            try:
                sph_values.append(float(sheet.cell_value(0, col)))
            except ValueError:
                sph_values.append(None)  # Invalid SPH values marked as None

        print(f"Extracted SPH values: {sph_values}")  # Debugging

        # **Extract CYL values and process matrix**
        for row in range(1, sheet.nrows):
            try:
                cyl_value = float(sheet.cell_value(row, 0))  # First column is CYL
            except ValueError:
                print(f"Skipping row {row+1}, invalid CYL value: {sheet.cell_value(row, 0)}")
                continue

            print(f"Processing CYL value: {cyl_value}")

            for col in range(1, sheet.ncols):
                try:
                    value = int(sheet.cell_value(row, col)) if sheet.cell_value(row, col) else 0
                except ValueError:
                    value = 0

                if sph_values[col - 1] is None:
                    continue

                print(f"Creating record: SPH={sph_values[col - 1]}, CYL={cyl_value}, Value={value}")

                # Find matching product
                product = self.env["product.template"].search([
                    ("cylindrical_value", "=", sph_values[col - 1]),
                    ("spherical_value", "=", cyl_value),
                    ("manufacturing_ok", "=", True)
                ], limit=1)

                print(f"Found product: {product.name if product else 'None'}")


                self.env["sph.cyl.matrix"].create({
                    "date": self.date,
                    "partner_id": self.partner_id.id,
                    "customer_ref": self.customer_ref,
                    "sph": sph_values[col - 1],
                    "cyl": cyl_value,
                    "value": value,
                    "upload_batch": upload_batch,
                    "product_id": product.id if product else False
                })

        print("Import completed successfully!")
        # Close wizard and reload the product template form

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

