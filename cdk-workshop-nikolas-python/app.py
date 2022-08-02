#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_workshop_nikolas_python.cdk_workshop_nikolas_python_stack import CdkWorkshopNikolasPythonStack


app = cdk.App()
CdkWorkshopNikolasPythonStack(app, "cdk-workshop-nikolas-python")

app.synth()
