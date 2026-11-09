# aerospace/readiness/attitude_rules.py

def check_attitude_limits(report, spacecraft):

    limits = spacecraft.attitude_limits

    if limits is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "attitude limits undefined",
        )
        return

    if limits.max_tilt_deg is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "maximum touchdown tilt unknown",
        )

    if limits.max_rate_dps is None:
        report.add_gap(
            "blocking",
            spacecraft.name,
            "maximum touchdown angular rate unknown",
        )