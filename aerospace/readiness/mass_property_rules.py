# aerospace/readiness/mass_property_rules.py

from spacecraft.mass_properties import mass_properties


def check_mass_properties(report, spacecraft):

    props = mass_properties(spacecraft)

    if props.com_m is None:

        report.add_gap(
            "blocking",
            spacecraft.name,
            "center of mass unknown",
        )

        for name in props.missing_com:
            report.add_gap(
                "warning",
                name,
                "component center of mass unknown",
            )

    if props.inertia_kgm2 is None:

        report.add_gap(
            "blocking",
            spacecraft.name,
            "vehicle inertia unknown",
        )

        for name in props.missing_inertia:
            report.add_gap(
                "warning",
                name,
                "component inertia unknown",
            )