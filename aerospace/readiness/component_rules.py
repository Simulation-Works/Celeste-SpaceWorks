# aerospace/readiness/component_rules.py

from spacecraft.components import Engine

from .engine_rules import check_engine
from engineering.readiness.provenance import check_provenance

def check_components(report, spacecraft):

    for component in spacecraft.components:

        check_provenance(
            report,
            component.name,
            component.provenance,
            "component",
        )

        if isinstance(component, Engine):
            check_engine(report, component)