# spacecraft_definition.py
from engineering.readiness.report import DefinitionReport
from engineering.readiness.provenance import check_provenance

from .landing_gear_rules import check_landing_gear
from .attitude_rules import check_attitude_limits
from .mass_property_rules import check_mass_properties
from .component_rules import check_components


def assess_spacecraft_definition(spacecraft):

    report = DefinitionReport()

    check_provenance(
        report,
        spacecraft.name,
        spacecraft.provenance,
        "vehicle-level data",
    )

    check_landing_gear(report, spacecraft)

    check_attitude_limits(report, spacecraft)

    check_mass_properties(report, spacecraft)

    check_components(report, spacecraft)

    return report