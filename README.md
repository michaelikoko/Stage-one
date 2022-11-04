# STAGE ONE TASK FOR HNG9 INTERNSHIP
Create an **(GET)** api endoint that returns the following  json response:
{ "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }   
- SlackUsername should be a **string** datatype and your slack username
- Backend should be a **boolean** datatype
- Age should be an  **integer** datatype
- Bio(description about yourself) should be a **string** datatype

# STAGE TWO TASK FOR HNG INTERNSHIP
- Using the same server setup from stage one
- Create an (POST) api endoint that takes the following sample json:
- { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
- Operation can either be addition, subtraction or mutiplication
- x can be a number and Integer datatype
- y can be a number and Integer datatype
- Based on the operation sent, perform a simple arithmetic operation on x and y
- Return a response with the result of the operation and your slack username
- { “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }

Bonus
We will send in a random string to the "operation_type" field . This string will be an operation written in words, for example “Can you please add the following numbers together - 13 and 25.”
This string will not be revealed ahead of time. On marking day, we will reveal the string and test it against all scripts