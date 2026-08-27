from application.liquidacion.item_liquidacion import ItemLiquidacion


class LiquidacionBuilder:

    def construir(self, legajo_conceptos, novedades):

        items = []

        # Conceptos fijos del legajo
        for lc in legajo_conceptos:

            concepto = lc.concepto
            clasificacion = concepto.clasificacion_concepto

            items.append(
                ItemLiquidacion(
                    concepto_id=concepto.id,

                    codigo=concepto.codigo,
                    concepto=concepto.nombre,

                   #clasificacion_id=clasificacion.id,
                    clasificacion_codigo=clasificacion.codigo,
                    clasificacion_nombre=clasificacion.nombre,
                    clasificacion_tipo=clasificacion.tipo,
            
                    cantidad=lc.cantidad,
                    valor=lc.valor,

                    tipo_calculo=concepto.tipo_calculo,
                    formula=concepto.formula,

                    es_novedad=False,
                    orden=concepto.orden
                )
            )

        # Novedades del período
        for nov in novedades:

            concepto = nov.concepto

            clasificacion = concepto.clasificacion_concepto

            items.append(
                ItemLiquidacion(
                    concepto_id=concepto.id,

                    codigo=concepto.codigo,
                    concepto=concepto.nombre,

                    #clasificacion_id=clasificacion.id,
                    clasificacion_codigo=clasificacion.codigo,
                    clasificacion_nombre=clasificacion.nombre,
                    clasificacion_tipo=clasificacion.tipo,

                    cantidad=nov.cantidad,
                    valor=nov.valor,

                    tipo_calculo=concepto.tipo_calculo,
                    formula=concepto.formula,

                    es_novedad=True,
                    orden=concepto.orden
                )
            )

        return sorted(items, key=lambda x: x.orden)