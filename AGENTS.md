# SIGES - Instrucciones para IA

## Objetivo

Este proyecto es el backend del Sistema Integral de Gestión de Seguridad (SIGES).

Está desarrollado principalmente con:

- Python
- FastAPI
- SQLAlchemy
- MariaDB

## Arquitectura

El proyecto utiliza una arquitectura organizada en capas:

- `api/`: endpoints HTTP y entrada de la aplicación.
- `application/`: servicios y lógica de aplicación.
- `domain/`: entidades, interfaces y reglas del dominio.
- `infrastructura/`: acceso a base de datos, repositorios e infraestructura externa.
- `core/`: configuración, seguridad, middleware y dependencias.

## Reglas generales

Antes de modificar código:

1. Analizar primero la implementación existente.
2. No cambiar la arquitectura sin autorización.
3. No mover lógica de negocio a los endpoints.
4. Respetar las interfaces de repositorio existentes.
5. No eliminar código simplemente porque parezca innecesario sin verificar su uso.
6. Si se encuentra código incompleto, inconsistente o sospechoso, informarlo antes de modificarlo.
7. No asumir que una funcionalidad está implementada solamente porque existe un archivo para ella.

## Liquidación de haberes

El proceso principal sigue aproximadamente este flujo:

API
→ `ProcesoLiquidacionService`
→ `LiquidacionBuilder`
→ `ItemLiquidacion`
→ `MotorLiquidacion`
→ `CalculadorFactory`
→ calculador correspondiente
→ `ResultadoBuilder`

### ItemLiquidacion

`ItemLiquidacion` es el objeto de trabajo utilizado durante el proceso de liquidación.

Contiene información del concepto, clasificación, cantidad, valor, tipo de cálculo, fórmula y resultado.

### Tipos de cálculo

Actualmente:

- `FIJO`: implementado.
- `FORMULA`: implementado.
- `PORCENTUAL`: pendiente de implementación.

No asumir que `PORCENTUAL` está implementado.

### Clasificación

La clasificación utiliza:

- `C`: haber.
- `D`: descuento/retención.

### Orden de cálculo

El orden de cálculo es importante porque las fórmulas pueden utilizar resultados de conceptos calculados anteriormente.

Actualmente la prioridad definida es:

1. `FIJO`
2. `PORCENTUAL`
3. `FORMULA`

Dentro de cada grupo se utiliza el campo `orden`.

No modificar este orden sin analizar previamente las dependencias entre conceptos.

### Fórmulas

Las fórmulas son procesadas mediante `FormulaEngine`.

`FormulaEngine` utiliza `ast` y `Decimal` para evaluar expresiones.

No reemplazar este mecanismo por `eval()` sin una revisión explícita de seguridad y diseño.

Las fórmulas pueden utilizar resultados de conceptos calculados previamente.

## Regla para cambios

Cuando se solicite una modificación:

1. Explicar brevemente qué archivos se van a modificar.
2. Explicar el impacto del cambio.
3. Mantener el comportamiento existente que no esté relacionado con el cambio.
4. No realizar refactorizaciones adicionales no solicitadas.
5. Si existe una inconsistencia en el código, señalarla antes de corregirla.

## Estilo de trabajo

Priorizar cambios pequeños, claros y fáciles de revisar.

Antes de implementar una funcionalidad nueva, analizar primero cómo funciona actualmente el flujo relacionado.

## Seguridad y archivos sensibles

No leer, modificar ni incluir en respuestas:

- `.env`
- contraseñas
- tokens
- claves secretas
- credenciales
- claves privadas

No modificar:

- `venv/`
- `__pycache__/`

No solicitar ni exponer secretos para realizar tareas de desarrollo.
Si una configuración sensible es necesaria, solicitar solamente el nombre de la variable o un valor ficticio.

## Restricción de alcance de los cambios

1. Modificá únicamente los archivos y componentes necesarios para cumplir el pedido explícito del usuario.
2. No crees archivos temporales, auxiliares o de prueba, como `_tmp_calcul.py`, salvo que el usuario lo autorice expresamente.
3. No agregues funcionalidades, refactorizaciones, mejoras ni cambios adicionales que no hayan sido solicitados.
4. No modifiques otros módulos, endpoints, modelos, repositorios o servicios que no estén directamente relacionados con el cambio solicitado.
5. Antes de modificar un archivo, verificá que sea necesario para cumplir el pedido.
6. Conservá la arquitectura, las convenciones, los nombres y el comportamiento existente que no formen parte del cambio solicitado.
7. No renombres campos, funciones, variables ni tablas fuera del alcance explícito del pedido.
8. No modifiques la base de datos, no generes migraciones ni ejecutes operaciones destructivas, salvo autorización expresa.
9. Si detectás un problema adicional, informalo, pero no lo corrijas sin autorización.
10. Si el cambio solicitado requiere una modificación adicional imprescindible, explicá el motivo antes de realizarla.
11. Al finalizar, informá brevemente los archivos modificados y los cambios realizados.
12. No afirmes que ejecutaste pruebas si no las ejecutaste.

**Regla principal:** cumplí exactamente el pedido del usuario, con el menor conjunto de cambios posible. No amplíes el alcance por iniciativa propia.