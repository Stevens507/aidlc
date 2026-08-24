# 7. GOBERNANZA

El proceso deja constancia de quién decidió qué. Esa constancia es lo que responde a un auditor o al oficial de cumplimiento de un cliente.

La política de gobernanza de IA del grupo fija la regla que gobierna todo lo demás:

> Todo código generado por IA pasa revisión humana antes de integrarse. El merge lo ejecuta siempre una persona identificable.

La responsabilidad de cada cambio recae siempre en una persona con nombre; ningún agente es Accountable de nada, nunca.

Esa regla se sostiene sobre lo que el ciclo va dejando escrito. Los artefactos no se descartan al cerrar cada fase: la prueba lleva al código, el código al requisito y el requisito a la historia de usuario que lo originó. AWS señala esa trazabilidad de punta a punta como el requisito crítico para la revisión regulatoria, y es lo que permite reconstruir después por qué el sistema hace lo que hace.

Lo que no salió bien también queda registrado. Toda escalación, incidente o sorpresa relevante produce un post-mortem corto con número correlativo. No es burocracia: sus conclusiones se convierten en cambios concretos, sea una regla, una skill o una verificación del CI.
