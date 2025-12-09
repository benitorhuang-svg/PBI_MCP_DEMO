---
description: Deploy semantic model to Power BI Fabric workspace
---

# Deploy to Power BI Fabric Workflow

This workflow deploys the semantic model to Power BI Service / Microsoft Fabric.

## Prerequisites
- Azure AD authentication configured
- Power BI Premium/Fabric workspace access
- Power BI Desktop running with Demo.pbip open

## Steps

1. Ensure Power BI Desktop is connected
Check that the MCP connection is active.

2. Deploy to Fabric workspace
Use the following command pattern (replace WORKSPACE_NAME with your workspace):
```
mcp_powerbi-modeling-mcp_database_operations with:
{
  "operation": "DeployToFabric",
  "deployToFabricRequest": {
    "targetWorkspaceName": "YOUR_WORKSPACE_NAME"
  }
}
```

3. Verify deployment
Log into Power BI Service and check the workspace for the "Demo" semantic model.

## Notes
- First deployment will trigger Azure AD authentication
- Subsequent deployments will overwrite the existing model
- Configure scheduled refresh in Power BI Service after deployment

## Alternative: Manual Publish
1. In Power BI Desktop, click "Publish"
2. Select target workspace
3. Wait for publish to complete
