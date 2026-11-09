# aerospace/readiness/landing_gear_rules.py

def check_landing_gear(report, spacecraft):

    gear = spacecraft.landing_gear

    if gear is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "landing gear definition missing",
        )
        return

    if gear.footprint_radius_m is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "landing footprint radius unknown",
        )

    if gear.foot_plane_y_m is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "landing footpad plane unknown",
        )

    if gear.engine_clearance_m is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "engine clearance unknown",
        )

    if gear.rated_vertical_speed_mps is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "rated touchdown vertical speed unknown",
        )

    if gear.rated_horizontal_speed_mps is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "rated touchdown horizontal speed unknown",
        )