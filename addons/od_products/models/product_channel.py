import random
from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"
    progress_amazon = fields.Integer(string="Amazon progress", compute="_compute_progress_amazon")
    progress_ebay = fields.Integer(string="eBay progress", compute="_compute_progress_ebay")
    progress_lt = fields.Integer(string="LT progress", compute="_compute_progress_lt")
    progress_lv = fields.Integer(string="LV progress", compute="_compute_progress_lv")
    progress_ee = fields.Integer(string="EE progress", compute="_compute_progress_ee")

    def _compute_progress(self, required_fields: list, progress_field: str):
        for rec in self:
            progress = 0
            for field in required_fields:
                if rec[field]:
                    progress += 100/len(required_fields)
            rec[progress_field] = progress

    @api.depends("uom_id", "list_price", "image_1920", "weight")
    def _compute_progress_amazon(self):
        required_fields = ["uom_id", "list_price", "image_1920", "weight"]
        self._compute_progress(required_fields, "progress_amazon")


    @api.depends("uom_id")
    def _compute_progress_ebay(self):
        required_fields = ["uom_id"]
        self._compute_progress(required_fields, "progress_ebay")


    @api.depends("uom_id")
    def _compute_progress_lt(self):
        required_fields = ["uom_id"]
        self._compute_progress(required_fields, "progress_lt")


    @api.depends("uom_id")
    def _compute_progress_lv(self):
        required_fields = ["uom_id"]
        self._compute_progress(required_fields, "progress_lv")


    @api.depends("uom_id")
    def _compute_progress_ee(self):
        required_fields = ["uom_id"]
        self._compute_progress(required_fields, "progress_ee")
