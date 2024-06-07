from owrx.controllers.admin import AuthorizationMixin
from owrx.controllers.template import WebpageController
from owrx.breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbMixin
from owrx.service import Services
import json
import re

import logging

logger = logging.getLogger(__name__)


class ServiceController(AuthorizationMixin, WebpageController):
    def indexAction(self):
        self.serve_template("services.html", **self.template_variables())

    def template_variables(self):
        variables = super().template_variables()
        variables["services"] = self.renderServices()
        return variables

    @staticmethod
    def renderServices():
        return """
                <table class='table'>
                    <tr>
                        <th>Service</th>
                        <th>SDR Profile</th>
                        <th>Frequency</th>
                    </tr>
                    {services}
                </table>
        """.format(
            services="".join(ServiceController.renderService(c) for c in Services.listAll())
        )

    @staticmethod
    def renderService(c):
        # Choose units based on frequency
        freq = c["freq"]
        if freq >= 1000000000:
            freq = freq / 1000000000
            unit = "GHz"
        elif freq >= 30000000:
            freq = freq / 1000000
            unit = "MHz"
        elif freq >= 1000:
            freq = freq / 1000
            unit = "kHz"
        else:
            unit = "Hz"
        # Removing trailing zeros, converting mode to upper case
        freq = re.sub(r"\.?0+$", "", "{0}".format(freq))
        # Format row
        return "<tr><td>{0}</td><td>{1} {2}</td><td>{3}{4}</td></tr>".format(
            c["mode"].upper(), c["sdr"], c["band"], freq, unit
        )
