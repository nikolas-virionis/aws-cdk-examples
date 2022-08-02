#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { CdkWorkshopNikolasStack } from '../lib/cdk-workshop-nikolas-stack';

const app = new cdk.App();
new CdkWorkshopNikolasStack(app, 'CdkWorkshopNikolasStack');
