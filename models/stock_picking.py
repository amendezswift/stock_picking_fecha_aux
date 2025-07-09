from datetime import timedelta
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    fecha_entrega_date = fields.Date(
        string='Fecha Entrega (solo fecha)',
        compute='_compute_fecha_entrega_date',
        store=True,
        index=True,
    )

    @api.depends('scheduled_date')
    def _compute_fecha_entrega_date(self):
        for record in self:
            if record.scheduled_date:
                # En Odoo, scheduled_date es un objeto datetime en UTC
                dt_utc = record.scheduled_date
                # Restamos 6 horas para pasar de UTC a UTC-6 (hora de Guatemala)
                dt_local = dt_utc - timedelta(hours=6)
                # Guardamos solo la parte de fecha
                record.fecha_entrega_date = dt_local.date()
            else:
                record.fecha_entrega_date = False
