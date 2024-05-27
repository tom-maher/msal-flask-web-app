import os

AUTHORITY = "https://login.microsoftonline.com/<<tenantId>>"

# Application (client) ID of app registration
CLIENT_ID = "<<clientId>>"

# Application (client) secret of app registration
CLIENT_SECRET = "<<clientSecret>>"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer

GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0/me'  # This resource requires no admin consent
ARM_API_ENDPOINT = 'https://management.azure.com/subscriptions?api-version=2022-12-01'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
GRAPH_API_SCOPE = ["User.Read"]
ARM_API_SCOPE = ["https://management.azure.com//user_impersonation"]
                      
# Tells the Flask-session extension to store sessions in the filesystem
SESSION_TYPE = "filesystem"
# In production, your setup may use multiple web servers behind a load balancer,
# and the subsequent requests may not be routed to the same web server.
# In that case, you may either use a centralized database-backed session store,
# or configure your load balancer to route subsequent requests to the same web server
# by using sticky sessions also known as affinity cookie.
# [1] https://www.imperva.com/learn/availability/sticky-session-persistence-and-cookies/
# [2] https://azure.github.io/AppService/2016/05/16/Disable-Session-affinity-cookie-(ARR-cookie)-for-Azure-web-apps.html
# [3] https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#configure-general-settings
