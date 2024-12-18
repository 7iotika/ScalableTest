.. _task_2:

Task 2. REST API Description
============================

Here should be a text description of the API and a downloadable .json file with a structured description, and ideally a link to a swagger.

But I've spent too much time on this assignment, so here is only some source data.


.. _task_2_user_get:

User

Method: GET

Endpoint: /api/external/user

Request: 
Parameter	Description	Values
user_id - (optional) Unique user  identifier. - String, Seven characters long, Examples: “3453255”
from - (optional) Pagination start timestamp. - Integer, Timestamp in nanoseconds
to	(optional) Pagination end timestamp. - Integer, Timestamp in nanoseconds
limit - (optional) Limit to records returned. - Integer, From 10 to 1000, Default: 1000
provider_id - (optional) Unique identifier of the partner a user bound to. - String, Four characters long, Examples: “2323”


Response:
Parameter	Description	Values
user_id - Unique user identifier. - String, Seven characters long, Example: “3453255”
provider_id - Unique identifier of the partner a user bound to. - String, Four characters long, Example: “2323”
status - User service state. - String, Values: “active”, “inactive”, “idle”
type - User type. - String, “basic”, “guest”, “company”, “advanced”, “admin”
sub_status - User status. - String, “signed”, “unsigned”, “absent” 
zone - Region of residence. - String, Two letters of lower case (Alpha-2 code, ISO 3166), Examples: “ru”, “us”, “gb”

Example: 
curl -X GET {host}/api/external/user?user_id=5478485&limit=100

.. _task_2_partner_get:

Partner

Method: GET

Endpoint: /api/partner

Request: 
Parameter	Description	Values
provider_id	(required) Unique partner identifier.	String
Four characters long
Example: “2323”
status	(optional) Partner operation state.	String
Values: “active”, “stopped”

Response:
Parameter	Description	Values
provider_id	Unique partner identifier.	String
Four characters long
Example: “2323”
status	Partner operation state.	String
Values: “active”, “stopped”

Example: 
curl -X GET -H "Authorization: Basic YXBkdXJlcjphcGlkl2Q=" {host}/api/partner?provider_id=6578

…
