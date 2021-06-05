def migrate(cr, version):
    """ Agrgamos dos registros faltantes.
    """
    cr.execute("""
    -- Faltaba el id=1
    INSERT INTO
        qc_issue (id, product_id, product_qty, product_uom, inspector_id,company_id)
        values (1,5,0,1,8,1);

    -- Faltaba el id = 50
    INSERT INTO
        hr_employee(id, resource_id)
        values (50,42)
    """)
