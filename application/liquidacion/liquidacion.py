from datetime import date
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple

# --- Modalidades de Pago ---
class ModalidadPago(Enum):
    BASICO = "BASICO"
    JORNAL_DIARIO = "JORNAL_DIARIO"
    POR_HORA = "POR_HORA"

# --- Novedades del Mes ---
@dataclass
class NovedadesMes:
    dias_trabajados: int = 0
    horas_trabajadas: float = 0.0
    inasistencias: int = 0

# --- Mapeo de Conceptos Básicos ---
MAPEO_CONCEPTOS = {
    ModalidadPago.BASICO: ("001", "Sueldo Básico Mensual"),
    ModalidadPago.JORNAL_DIARIO: ("002", "Jornales Trabajados"),
    ModalidadPago.POR_HORA: ("003", "Horas Normales Trabajadas")
}

def calcular_recibo_completo(
    legajo: str,
    nombre: str,
    fecha_ingreso: date,
    modalidad: ModalidadPago,
    tarifa_base: float,
    novedades: NovedadesMes,
    fecha_liquidacion: date
) -> Dict:
    
    # 1. CALCULAR HABER BÁSICO SEGÚN MODALIDAD
    codigo_concepto, desc_concepto = MAPEO_CONCEPTOS[modalidad]
    
    if modalidad == ModalidadPago.MENSUALIZADO:
        dias_a_pagar = max(0, 30 - novedades.inasistencias)
        haber_basico = (tarifa_base / 30) * dias_a_pagar
        unidades = f"{dias_a_pagar} días"
        
    elif modalidad == ModalidadPago.JORNAL_DIARIO:
        haber_basico = novedades.dias_trabajados * tarifa_base
        unidades = f"{novedades.dias_trabajados} días"
        
    elif modalidad == ModalidadPago.POR_HORA:
        haber_basico = novedades.horas_trabajadas * tarifa_base
        unidades = f"{novedades.horas_trabajadas} hs"

    # 2. CALCULAR ANTIGÜEDAD (Años enteros cumplidos)
    anios = fecha_liquidacion.year - fecha_ingreso.year
    if (fecha_liquidacion.month, fecha_liquidacion.day) < (fecha_ingreso.month, fecha_ingreso.day):
        anios -= 1
    anios = max(0, anios)
    
    porc_antiguedad = 0.01 * anios  # 1% por año
    monto_antiguedad = haber_basico * porc_antiguedad

    # 3. BASE REMUNERATIVA TOTAL
    total_remunerativo = haber_basico + monto_antiguedad

    # 4. DEDUCCIONES DE LEY (Sobre el Total Remunerativo)
    jubilacion = total_remunerativo * 0.11
    pami = total_remunerativo * 0.03
    obra_social = total_remunerativo * 0.03
    total_deducciones = jubilacion + pami + obra_social

    # 5. NETO A COBRAR
    neto = total_remunerativo - total_deducciones

    # Devuelve la estructura completa del recibo de sueldo
    return {
        "legajo": legajo,
        "nombre": nombre,
        "modalidad": modalidad.value,
        "lineas": [
            {"codigo": codigo_concepto, "concepto": desc_concepto, "unidades": unidades, "remunerativo": round(haber_basico, 2), "deduccion": 0.0},
            {"codigo": "040", "concepto": "Adicional Antigüedad", "unidades": f"{anios}%", "remunerativo": round(monto_antiguedad, 2), "deduccion": 0.0},
            {"codigo": "501", "concepto": "Jubilación", "unidades": "11%", "remunerativo": 0.0, "deduccion": round(jubilacion, 2)},
            {"codigo": "502", "concepto": "Ley 19.032 (PAMI)", "unidades": "3%", "remunerativo": 0.0, "deduccion": round(pami, 2)},
            {"codigo": "503", "concepto": "Obra Social", "unidades": "3%", "remunerativo": 0.0, "deduccion": round(obra_social, 2)},
        ],
        "totales": {
            "remunerativo": round(total_remunerativo, 2),
            "deducciones": round(total_deducciones, 2),
            "neto_a_cobrar": round(neto, 2)
        }
    }


# --- DEMOSTRACIÓN DE LIQUIDACIÓN MENSUAL ---
FECHA_LIQ = date(2026, 10, 31)

# Case 1: Mensualizado
r1 = calcular_recibo_completo("LEG-01", "Ana Pérez", date(2021, 3, 15), ModalidadPago.MENSUALIZADO, 850000.0, NovedadesMes(inasistencias=0), FECHA_LIQ)

# Case 2: Jornalero
r2 = calcular_recibo_completo("LEG-02", "Carlos Ruiz", date(2022, 5, 20), ModalidadPago.JORNAL_DIARIO, 35000.0, NovedadesMes(dias_trabajados=22), FECHA_LIQ)

# Case 3: Por Hora
r3 = calcular_recibo_completo("LEG-03", "Lucas Gómez", date(2025, 1, 10), ModalidadPago.POR_HORA, 4500.0, NovedadesMes(horas_trabajadas=160.0), FECHA_LIQ)

for r in [r1, r2, r3]:
    print(f"Empleado: {r['nombre']} ({r['modalidad']})")
    print(f"Total Remunerativo: ${r['totales']['remunerativo']:,.2f} | Deducciones: ${r['totales']['deducciones']:,.2f} | NETO: ${r['totales']['neto_a_cobrar']:,.2f}\n")




    import ast
import operator
from enum import Enum
from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict, Optional, Any


# ==============================================================================
# 1. ENUMERACIONES Y ROLES DE NEGOCIO (CONTRATO INMUTABLE)
# ==============================================================================

class FrecuenciaPago(Enum):
    MENSUAL = "MENSUAL"
    QUINCENAL = "QUINCENAL"


class ModalidadPago(Enum):
    MENSUALIZADO = "MENSUALIZADO"
    JORNAL_DIARIO = "JORNAL_DIARIO"
    POR_HORA = "POR_HORA"


class TipoConcepto(Enum):
    REMUNERATIVO = "REMUNERATIVO"
    NO_REMUNERATIVO = "NO_REMUNERATIVO"
    DEDUCCION = "DEDUCCION"


class RolNegocio(Enum):
    """
    Identificador sistémico inmutable. El usuario puede cambiar el código (ej: '040' por '199'),
    pero el motor busca la regla mediante esta enumeración.
    """
    BASICO_MENSUAL = "BASICO_MENSUAL"
    BASICO_JORNAL = "BASICO_JORNAL"
    BASICO_HORA = "BASICO_HORA"
    ADICIONAL_ANTIGUEDAD = "ADICIONAL_ANTIGUEDAD"
    PREMIO_PRESENTISMO = "PREMIO_PRESENTISMO"
    RETENCION_JUBILACION = "RETENCION_JUBILACION"
    RETENCION_PAMI = "RETENCION_PAMI"
    RETENCION_OBRA_SOCIAL = "RETENCION_OBRA_SOCIAL"
    CONCEPTO_GENERICO = "CONCEPTO_GENERICO"


# ==============================================================================
# 2. EVALUADOR SEGURO DE FÓRMULAS USANDO AST (ABSTRACT SYNTAX TREES)
# ==============================================================================

class EvaluadorFormulasAST:
    """
    Parsea y evalúa fórmulas matemáticas almacenadas como texto de forma 100% segura,
    sin usar eval() directo de Python.
    """
    OPERADORES = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def evaluar(self, formula_str: str, contexto_variables: Dict[str, float]) -> float:
        if not formula_str or not formula_str.strip():
            return 0.0
        try:
            tree = ast.parse(formula_str, mode='eval')
            return float(self._evaluar_nodo(tree.body, contexto_variables))
        except Exception as e:
            print(f"[ERROR AST] No se pudo evaluar la fórmula '{formula_str}': {e}")
            return 0.0

    def _evaluar_nodo(self, nodo: ast.AST, contexto: Dict[str, float]) -> float:
        # 1. Números Literales
        if isinstance(nodo, ast.Constant):
            if isinstance(nodo.value, (int, float)):
                return float(nodo.value)
            raise ValueError(f"Constante no permitida: {nodo.value}")

        # 2. Variables de Dominio (ej: haber_basico, anios_antiguedad)
        elif isinstance(nodo, ast.Name):
            if nodo.id in contexto:
                return float(contexto[nodo.id])
            raise NameError(f"Variable de dominio no reconocida: '{nodo.id}'")

        # 3. Operaciones Binarias (ej: a * b, a + b)
        elif isinstance(nodo, ast.BinOp):
            tipo_op = type(nodo.op)
            if tipo_op in self.OPERADORES:
                left = self._evaluar_nodo(nodo.left, contexto)
                right = self._evaluar_nodo(nodo.right, contexto)
                return self.OPERADORES[tipo_op](left, right)
            raise TypeError(f"Operador binario no soportado: {tipo_op.__name__}")

        # 4. Operaciones Unarias (ej: -a)
        elif isinstance(nodo, ast.UnaryOp):
            tipo_op = type(nodo.op)
            if tipo_op in self.OPERADORES:
                operand = self._evaluar_nodo(nodo.operand, contexto)
                return self.OPERADORES[tipo_op](operand)
            raise TypeError(f"Operador unario no soportado: {tipo_op.__name__}")

        else:
            raise TypeError(f"Estructura de fórmula no permitida: {type(nodo).__name__}")


# ==============================================================================
# 3. DICCIONARIO DE VARIABLES DE DOMINIO
# ==============================================================================

class DiccionarioVariables:
    """Expone un contexto de variables seguras para las fórmulas."""
    def __init__(self):
        self._variables: Dict[str, float] = {}

    def registrar(self, nombre: str, valor: float):
        self._variables[nombre] = float(valor)

    def obtener_contexto(self) -> Dict[str, float]:
        return self._variables.copy()


# ==============================================================================
# 4. ENTIDADES DEL SISTEMA (TABLAS SQL)
# ==============================================================================

@dataclass
class Concepto:
    """Representa una fila de la tabla SQL 'conceptos'."""
    id: int
    codigo: str              # Código visible configurable (ej: '010', '199', '501')
    nombre: str              # Descripción visible
    tipo: TipoConcepto
    rol_negocio: RolNegocio  # Identificador funcional para el motor
    formula: str             # Expresión matemática paramétrica
    orden: int = 100         # Orden de prelación de cálculo


@dataclass
class Empleado:
    """Entidad Legajo / Empleado."""
    id: int
    legajo: str
    nombre: str
    cuil: str
    fecha_ingreso: date
    tarifa_base: float      # Sueldo Mensual, Valor Jornal o Valor Hora
    frecuencia: FrecuenciaPago
    modalidad: ModalidadPago

    def calcular_anios_antiguedad(self, fecha_ref: date) -> int:
        """Calcula los años enteros cumplidos a la fecha de liquidación."""
        anios = fecha_ref.year - self.fecha_ingreso.year
        if (fecha_ref.month, fecha_ref.day) < (self.fecha_ingreso.month, self.fecha_ingreso.day):
            anios -= 1
        return max(0, anios)


@dataclass
class NovedadPeriodo:
    """Registros de la tabla 'novedades_periodo' (variables del mes)."""
    empleado_id: int
    rol_negocio: RolNegocio
    unidad_valor: float  # Inasistencias, Días trabajados u Horas trabajadas


# ==============================================================================
# 5. ESTRUCTURA DEL RECIBO DE SUELDO
# ==============================================================================

@dataclass
class LineaRecibo:
    codigo: str
    nombre: str
    unidades: str
    tipo: TipoConcepto
    monto: float


class ReciboSueldo:
    def __init__(self, empleado: Empleado, periodo: str):
        self.empleado = empleado
        self.periodo = periodo
        self.lineas: List[LineaRecibo] = []

    def agregar_linea(self, concepto: Concepto, unidades: str, monto: float):
        if monto > 0:
            self.lineas.append(LineaRecibo(
                codigo=concepto.codigo,
                nombre=concepto.nombre,
                unidades=unidades,
                tipo=concepto.tipo,
                monto=round(monto, 2)
            ))

    @property
    def total_remunerativo(self) -> float:
        return sum(l.monto for l in self.lineas if l.tipo == TipoConcepto.REMUNERATIVO)

    @property
    def total_no_remunerativo(self) -> float:
        return sum(l.monto for l in self.lineas if l.tipo == TipoConcepto.NO_REMUNERATIVO)

    @property
    def total_deducciones(self) -> float:
        return sum(l.monto for l in self.lineas if l.tipo == TipoConcepto.DEDUCCION)

    @property
    def neto_a_cobrar(self) -> float:
        return (self.total_remunerativo + self.total_no_remunerativo) - self.total_deducciones

    def imprimir_recibo(self):
        print("=" * 88)
        print(f" RECIBO DE HABERES | Período: {self.periodo}")
        print(f" Legajo: {self.empleado.legajo:<8} | Empleado: {self.empleado.nombre:<25} | CUIL: {self.empleado.cuil}")
        print(f" Modalidad: {self.empleado.modalidad.value:<12} | Antigüedad: {self.empleado.calcular_anios_antiguedad(date.today())} años")
        print("-" * 88)
        print(f"{'Cód':<6} | {'Concepto':<30} | {'Unid.':<8} | {'Hab. Remun.':>12} | {'Hab. No Rem.':>12} | {'Deducciones':>12}")
        print("-" * 88)

        for l in self.lineas:
            rem = f"${l.monto:,.2f}" if l.tipo == TipoConcepto.REMUNERATIVO else ""
            norem = f"${l.monto:,.2f}" if l.tipo == TipoConcepto.NO_REMUNERATIVO else ""
            ded = f"${l.monto:,.2f}" if l.tipo == TipoConcepto.DEDUCCION else ""
            print(f"{l.codigo:<6} | {l.nombre:<30} | {l.unidades:<8} | {rem:>12} | {norem:>12} | {ded:>12}")

        print("-" * 88)
        print(f" SUBTOTALES:{'':<35} | ${self.total_remunerativo:>12,.2f} | ${self.total_no_remunerativo:>12,.2f} | ${self.total_deducciones:>12,.2f}")
        print("=" * 88)
        print(f" NETO A COBRAR (CBU):{'':<47} | ${self.neto_a_cobrar:>12,.2f}")
        print("=" * 88 + "\n")


# ==============================================================================
# 6. MOTOR DE LIQUIDACIÓN CON INYECCIÓN DE VARIABLES Y AST
# ==============================================================================

class MotorLiquidacion:
    MAPEO_MODALIDAD_ROL = {
        ModalidadPago.MENSUALIZADO: RolNegocio.BASICO_MENSUAL,
        ModalidadPago.JORNAL_DIARIO: RolNegocio.BASICO_JORNAL,
        ModalidadPago.POR_HORA: RolNegocio.BASICO_HORA
    }

    def __init__(self, catalogo_conceptos: List[Concepto]):
        self.catalogo = sorted(catalogo_conceptos, key=lambda c: c.orden)
        self.evaluador = EvaluadorFormulasAST()

    def _obtener_concepto_por_rol(self, rol: RolNegocio) -> Optional[Concepto]:
        for c in self.catalogo:
            if c.rol_negocio == rol:
                return c
        return None

    def liquidar(self, empleado: Empleado, novedades: List[NovedadPeriodo], periodo: str, fecha_liquidacion: date) -> ReciboSueldo:
        recibo = ReciboSueldo(empleado, periodo)
        dict_vars = DiccionarioVariables()

        # Novedades del empleado
        mapa_novedades = {n.rol_negocio: n.unidad_valor for n in novedades if n.empleado_id == empleado.id}

        # Contexto inicial de variables
        anios_antiguedad = empleado.calcular_anios_antiguedad(fecha_liquidacion)
        dict_vars.registrar("tarifa_base", empleado.tarifa_base)
        dict_vars.registrar("anios_antiguedad", anios_antiguedad)

        # ----------------------------------------------------------------------
        # PASO 1: CÁLCULO DEL HABER BÁSICO (SEGÚN MODALIDAD)
        # ----------------------------------------------------------------------
        rol_basico_esperado = self.MAPEO_MODALIDAD_ROL[empleado.modalidad]
        concepto_basico = self._obtener_concepto_por_rol(rol_basico_esperado)

        haber_basico = 0.0
        if concepto_basico:
            if empleado.modalidad == ModalidadPago.MENSUALIZADO:
                inasistencias = mapa_novedades.get(RolNegocio.BASICO_MENSUAL, 0)
                dias_a_pagar = max(0, 30 - int(inasistencias))
                dict_vars.registrar("dias_a_pagar", dias_a_pagar)
                
                haber_basico = self.evaluador.evaluar(concepto_basico.formula, dict_vars.obtener_contexto())
                recibo.agregar_linea(concepto_basico, f"{dias_a_pagar} días", haber_basico)

            elif empleado.modalidad == ModalidadPago.JORNAL_DIARIO:
                dias_trabajados = mapa_novedades.get(RolNegocio.BASICO_JORNAL, 0)
                dict_vars.registrar("dias_trabajados", dias_trabajados)
                
                haber_basico = self.evaluador.evaluar(concepto_basico.formula, dict_vars.obtener_contexto())
                recibo.agregar_linea(concepto_basico, f"{int(dias_trabajados)} días", haber_basico)

            elif empleado.modalidad == ModalidadPago.POR_HORA:
                horas_trabajadas = mapa_novedades.get(RolNegocio.BASICO_HORA, 0.0)
                dict_vars.registrar("horas_trabajadas", horas_trabajadas)
                
                haber_basico = self.evaluador.evaluar(concepto_basico.formula, dict_vars.obtener_contexto())
                recibo.agregar_linea(concepto_basico, f"{horas_trabajadas} hs", haber_basico)

        dict_vars.registrar("haber_basico", haber_basico)

        # ----------------------------------------------------------------------
        # PASO 2: ADICIONAL POR ANTIGÜEDAD (VALIDACIÓN DERECHO >= 1 AÑO)
        # ----------------------------------------------------------------------
        concepto_antiguedad = self._obtener_concepto_por_rol(RolNegocio.ADICIONAL_ANTIGUEDAD)
        if concepto_antiguedad and anios_antiguedad >= 1:
            monto_antiguedad = self.evaluador.evaluar(concepto_antiguedad.formula, dict_vars.obtener_contexto())
            recibo.agregar_linea(concepto_antiguedad, f"{anios_antiguedad}%", monto_antiguedad)

        dict_vars.registrar("total_remunerativo", recibo.total_remunerativo)

        # ----------------------------------------------------------------------
        # PASO 3: DEDUCCIONES DE LEY (SOBRE BASE REMUNERATIVA ACUMULADA)
        # ----------------------------------------------------------------------
        for rol_ded in [RolNegocio.RETENCION_JUBILACION, RolNegocio.RETENCION_PAMI, RolNegocio.RETENCION_OBRA_SOCIAL]:
            concepto_ded = self._obtener_concepto_por_rol(rol_ded)
            if concepto_ded:
                monto_deduccion = self.evaluador.evaluar(concepto_ded.formula, dict_vars.obtener_contexto())
                recibo.agregar_linea(concepto_ded, "", monto_deduccion)

        return recibo


# ==============================================================================
# 7. EJECUCIÓN DEL LOTE DE PRUEBA
# ==============================================================================

if __name__ == "__main__":
    FECHA_LIQUIDACION = date(2026, 10, 31)

    # Catálogo de Conceptos con Fórmulas de Texto (Código de antigüedad '199')
    tabla_conceptos_bd = [
        Concepto(1, "010", "Sueldo Básico Mensual", TipoConcepto.REMUNERATIVO, RolNegocio.BASICO_MENSUAL, formula="(tarifa_base / 30) * dias_a_pagar", orden=10),
        Concepto(2, "012", "Jornales Trabajados", TipoConcepto.REMUNERATIVO, RolNegocio.BASICO_JORNAL, formula="dias_trabajados * tarifa_base", orden=10),
        Concepto(3, "015", "Horas Normales Trabajadas", TipoConcepto.REMUNERATIVO, RolNegocio.BASICO_HORA, formula="horas_trabajadas * tarifa_base", orden=10),
        
        # Concepto de antigüedad parametrizado con código "199" y fórmula paramétrica
        Concepto(4, "199", "Adicional Antigüedad Convenio", TipoConcepto.REMUNERATIVO, RolNegocio.ADICIONAL_ANTIGUEDAD, formula="haber_basico * (0.01 * anios_antiguedad)", orden=20),
        
        Concepto(5, "501", "Jubilación (Ley 24.241)", TipoConcepto.DEDUCCION, RolNegocio.RETENCION_JUBILACION, formula="total_remunerativo * 0.11", orden=50),
        Concepto(6, "502", "Ley 19.032 - PAMI", TipoConcepto.DEDUCCION, RolNegocio.RETENCION_PAMI, formula="total_remunerativo * 0.03", orden=50),
        Concepto(7, "503", "Obra Social", TipoConcepto.DEDUCCION, RolNegocio.RETENCION_OBRA_SOCIAL, formula="total_remunerativo * 0.03", orden=50),
    ]

    # Empleados
    emp_mensual = Empleado(1, "LEG-101", "Ana Martínez", "27-35111222-4", date(2021, 3, 15), 850000.0, FrecuenciaPago.MENSUAL, ModalidadPago.MENSUALIZADO)
    emp_jornal = Empleado(2, "LEG-102", "Carlos Ruiz", "20-38444555-9", date(2022, 6, 10), 35000.0, FrecuenciaPago.MENSUAL, ModalidadPago.JORNAL_DIARIO)
    emp_hora = Empleado(3, "LEG-103", "Lucas Gómez", "20-42999888-3", date(2026, 1, 10), 4500.0, FrecuenciaPago.MENSUAL, ModalidadPago.POR_HORA)

    # Novedades del período
    novedades_mes = [
        NovedadPeriodo(empleado_id=2, rol_negocio=RolNegocio.BASICO_JORNAL, unidad_valor=22),   # Carlos trabajó 22 días
        NovedadPeriodo(empleado_id=3, rol_negocio=RolNegocio.BASICO_HORA, unidad_valor=160.0)   # Lucas trabajó 160 hs
    ]

    motor = MotorLiquidacion(catalogo_conceptos=tabla_conceptos_bd)

    # Generación e impresión de Recibos
    r1 = motor.liquidar(emp_mensual, novedades_mes, "10/2026", FECHA_LIQUIDACION)
    r1.imprimir_recibo()

    r2 = motor.liquidar(emp_jornal, novedades_mes, "10/2026", FECHA_LIQUIDACION)
    r2.imprimir_recibo()

    r3 = motor.liquidar(emp_hora, novedades_mes, "10/2026", FECHA_LIQUIDACION)
    r3.imprimir_recibo()