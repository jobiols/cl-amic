# Copyright 2019 jeo Software
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from openerp import api, models

_logger = logging.getLogger(__name__)


class IssueCoverReport(models.AbstractModel):
    """ Abstract Model for report template.

        for `_name` model, please use:
        `report.` as prefix then add `module_name.report_name`.
    """
    _name = 'report.qc.issue.issue_cover_report_template'

    @api.model
    def _get_child_vals(self, record, level, qty, uom):
        """Get bom.line values.

        :param record: mrp.bom.line record
        :param level: level of recursion
        :param qty: quantity of the product
        :param uom: unit of measurement of a product
        """
        child = {
            'pname': record.product_id.name_get()[0][1],
            'pcode': record.product_id.default_code,
            'puom': record.product_uom_id,
            'uname': record.product_uom_id.name,
            'level': level,
            'code': record.bom_id.code,
        }
        qty_per_bom = record.bom_id.product_qty
        if uom:
            if uom != record.bom_id.product_uom_id:
                qty = uom._compute_quantity(qty, record.bom_id.product_uom_id)
            child['pqty'] = (record.product_qty * qty) / qty_per_bom
        else:
            # for the first case, the ponderation is right
            child['pqty'] = (record.product_qty * qty)
        return child

    # def get_children(self, records, level=0):
    #     result = []

    #     def _get_rec(records, level, qty=1.0, uom=False):
    #         for l in records:
    #             child = self._get_child_vals(l, level, qty, uom)
    #             result.append(child)
    #             if l.child_line_ids:
    #                 level += 1
    #                 _get_rec(l.child_line_ids, level, qty=child['pqty'],
    #                          uom=child['puom'])
    #                 if level > 0:
    #                     level -= 1
    #         return result

    #     children = _get_rec(records, level)

    #     return children

    @staticmethod
    def to_image(image):
        """ Si el mimetype es pdf lo convierte a imagen
        """
        if image == 'application/pdf':
            return convert_from_bytes(image.datas)
        return image

    @api.multi
    def get_report_values(self, docids, data=None):

        #import wdb;wdb.set_trace()


        """ Datos a imprimir
                OT = data['ot']
                producto_final = data['final_product_name']
                product_qty = data['product_qty']
                final_product_uom = data['final_product_uom']

                raw_data = data['raw_data']
                raw_data = [{'product_name':'materia prima uno',
                             'product_qty': 123,
                             'product_uom': 'Un'}]
        """
        issues = self.env['qc.issue'].browse(docids)

#        domain = [('res_id', '=', bom.id)]
#        attachs = self.env['mrp.bom.document'].search(domain, order='sequence,id')

        return {
            'doc_ids': docids,
            'doc_model': 'qc.issue',
            'docs': issues,
            #'get_children': self.get_children,
            'data': data,
            #'attachs': attachs,
            #'to_image': self.to_image
        }
