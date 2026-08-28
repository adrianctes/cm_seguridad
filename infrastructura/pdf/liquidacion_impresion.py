from decimal import Decimal
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.units import mm

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


class LiquidacionImpresion:

    def __init__(self, data, ruta):

        self.data = data
        self.ruta = ruta

    # =====================================================
    # FECHA
    # =====================================================

    def formatear_fecha(self, fecha):

        if not fecha:
            return "-"

        try:

            dt = datetime.fromisoformat(
                str(fecha)
            )

            return dt.strftime(
                "%d/%m/%Y %H:%M"
            )

        except Exception:

            return str(fecha)

    # =====================================================
    # MONEDA
    # =====================================================

    def moneda(self, valor):

        if valor is None:
            return "$ 0,00"

        try:

            valor = Decimal(
                str(valor)
            )

            return f"$ {valor:,.2f}"

        except Exception:

            return "$ 0,00"

    # =====================================================
    # GENERAR PDF
    # =====================================================

    def generar(self):

        doc = SimpleDocTemplate(

            self.ruta,

            pagesize=A4,

            rightMargin=15 * mm,
            leftMargin=15 * mm,
            topMargin=15 * mm,
            bottomMargin=15 * mm,
        )

        styles = getSampleStyleSheet()

        titulo = ParagraphStyle(
            "Titulo",
            parent=styles["Heading1"],
            fontSize=16,
            leading=20,
            alignment=TA_LEFT,
            spaceAfter=8,
        )

        subtitulo = ParagraphStyle(
            "Subtitulo",
            parent=styles["Normal"],
            fontSize=10,
            leading=13,
        )

        normal = ParagraphStyle(
            "NormalLiquidacion",
            parent=styles["Normal"],
            fontSize=9,
            leading=11,
        )

        derecha = ParagraphStyle(
            "Derecha",
            parent=normal,
            alignment=TA_RIGHT,
        )

        elementos = []

        # =================================================
        # TITULO
        # =================================================

        elementos.append(
            Paragraph(
                "LIQUIDACIÓN DE HABERES",
                titulo
            )
        )

        elementos.append(
            Spacer(1, 4)
        )

        # =================================================
        # CABECERA
        # =================================================

        cabecera = [

            [
                Paragraph("<b>Fecha:</b>", normal),
                Paragraph(
                    self.formatear_fecha(
                        self.data.get("fecha")
                    ),
                    normal
                ),

                Paragraph("<b>Período:</b>", normal),
                Paragraph(
                    str(
                        self.data.get(
                            "periodo",
                            ""
                        )
                    ),
                    normal
                ),
            ],

            [
                Paragraph("<b>Modalidad:</b>", normal),
                Paragraph(
                    str(
                        self.data.get(
                            "modalidad",
                            ""
                        )
                    ),
                    normal
                ),

                Paragraph("<b>Número:</b>", normal),
                Paragraph(
                    str(
                        self.data.get(
                            "numero",
                            ""
                        )
                    ),
                    normal
                ),
            ],

            [
                Paragraph("<b>Legajo:</b>", normal),
                Paragraph(
                    str(
                        self.data.get(
                            "legajo_id",
                            ""
                        )
                    ),
                    normal
                ),

                Paragraph(
                    "<b>Apellido y Nombre:</b>",
                    normal
                ),

                Paragraph(
                    str(
                        self.data.get(
                            "ayn",
                            ""
                        )
                    ),
                    normal
                ),
            ],
        ]

        tabla_cabecera = Table(

            cabecera,

            colWidths=[
                25 * mm,
                45 * mm,
                35 * mm,
                65 * mm,
            ]
        )

        tabla_cabecera.setStyle(
            TableStyle([

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#CBD5E1")
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor("#F8FAFC")
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    6
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    6
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),
            ])
        )

        elementos.append(
            tabla_cabecera
        )

        elementos.append(
            Spacer(1, 10)
        )

        # =================================================
        # CONCEPTOS
        # =================================================

        elementos.append(
            Paragraph(
                "<b>Conceptos liquidados</b>",
                subtitulo
            )
        )

        elementos.append(
            Spacer(1, 5)
        )

        datos = [

            [
                "Código",
                "Concepto",
                "Cantidad",
                "Valor",
                "Haberes",
                "Retención",
                "Total",
            ]
        ]

        for item in self.data.get(
            "lineas",
            []
        ):

            cantidad = Decimal(
                str(
                    item.get(
                        "cantidad",
                        0
                    )
                )
            )

            valor = Decimal(
                str(
                    item.get(
                        "valor",
                        0
                    )
                )
            )

            haber = Decimal(
                str(
                    item.get(
                        "haber",
                        0
                    )
                )
            )

            retencion = Decimal(
                str(
                    item.get(
                        "retencion",
                        0
                    )
                )
            )

            total = Decimal(
                str(
                    item.get(
                        "total",
                        0
                    )
                )
            )

            datos.append([

                item.get(
                    "codigo",
                    ""
                ),

                item.get(
                    "concepto",
                    ""
                ),

                f"{cantidad:,.2f}",
                f"{valor:,.2f}",
                f"{haber:,.2f}",
                f"{retencion:,.2f}",
                f"{total:,.2f}",
            ])

        tabla_detalle = Table(

            datos,

            colWidths=[

                22 * mm,
                50 * mm,
                20 * mm,
                27 * mm,
                27 * mm,
                27 * mm,
                27 * mm,
            ],

            repeatRows=1
        )

        tabla_detalle.setStyle(
            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#E2E8F0")
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#CBD5E1")
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),

                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8
                ),

                (
                    "ALIGN",
                    (2, 1),
                    (-1, -1),
                    "RIGHT"
                ),

                (
                    "ALIGN",
                    (2, 0),
                    (-1, 0),
                    "RIGHT"
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),
            ])
        )

        elementos.append(
            tabla_detalle
        )

        elementos.append(
            Spacer(1, 10)
        )

        # =================================================
        # TOTALES
        # =================================================

        totales = [

            [
                Paragraph(
                    "<b>Total Haberes:</b>",
                    normal
                ),

                Paragraph(
                    self.moneda(
                        self.data.get(
                            "total_haberes"
                        )
                    ),
                    derecha
                ),
            ],

            [
                Paragraph(
                    "<b>Total Retenciones:</b>",
                    normal
                ),

                Paragraph(
                    self.moneda(
                        self.data.get(
                            "total_retenciones"
                        )
                    ),
                    derecha
                ),
            ],

            [
                Paragraph(
                    "<b>Neto a Cobrar:</b>",
                    normal
                ),

                Paragraph(
                    f"<b>{self.moneda(self.data.get('total_neto'))}</b>",
                    derecha
                ),
            ],
        ]

        tabla_totales = Table(

            totales,

            colWidths=[
                55 * mm,
                40 * mm
            ],

            hAlign="RIGHT"
        )

        tabla_totales.setStyle(
            TableStyle([

                (
                    "LINEABOVE",
                    (0, 2),
                    (-1, 2),
                    1,
                    colors.black
                ),

                (
                    "ALIGN",
                    (1, 0),
                    (1, -1),
                    "RIGHT"
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),
            ])
        )

        elementos.append(
            tabla_totales
        )

        # =================================================
        # GENERAR
        # =================================================

        doc.build(
            elementos
        )